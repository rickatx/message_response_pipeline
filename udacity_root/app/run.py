import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from sklearn.externals import joblib
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql_table('CategorizedMessages', engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    #
    # #xtract data needed for visuals
    #
    
    # Distribution of message categorization status
    # -- Frequency of number of per-message categorizations
    categ_counts = df.loc[:, 'related':].sum(axis=1).value_counts().sort_index()
    # -- Bar plot value
    categ_status_names = ['Unrelated', 'Related, No Categ', 'Categorized']
    categ_status_counts = [categ_counts[0], categ_counts[1], categ_counts[2:].sum()]
    total_counts = sum(categ_status_counts)
    pct_text = [f'  {(100*x/total_counts):.1f}% of Total' for x in categ_status_counts]
    
    # Counts of applications of category tags to messages
    num_categorizations = df.loc[:, 'request':].sum(axis=0)
    num_categorizations = num_categorizations.sort_values(ascending=False)
    category_names = num_categorizations.index
    categ_applied_count = num_categorizations.values
    
    # create 
    graphs = [
        {
            'data': [
                Bar(
                    x=categ_status_names,
                    y=categ_status_counts,
                    hovertext=pct_text
                )
            ],

            'layout': {
                'title': 'Distribution of Message Categorization Status',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Status"
                }
            }
        },
        {
            'data': [
                Bar(
                    x=category_names,
                    y=categ_applied_count
                )
            ],

            'layout': {
                'title': 'Category Tag Application Counts',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Category",
                    'tickangle': 33,
                    'automargin': "true"
                }
            }
        }
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()