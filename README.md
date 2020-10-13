# Disaster Response Messages ETL/ML Pipelines
> ETL and ML pipelines for processing/flagging disaster response messages.

## Project Description
Inputs to the ETL pipeline are messages received during a disaster, and categorizations of the need expressed by the messages
(e.g., "shelter", "medical_help", "food", "aid_related", etc.) The ETL pipeline transforms the data into a format suitable
as input to a supervised learning algorithm.

The ML pipeline reads the data generated by the ETL pipeline and trains a model. The purpose of the model is to predict
the needs expressed by new messages so that messages can be automatically classified during a live disaster response.

Finally, a web app both displays some statistics on the dataset used for training, and allows the user to experiment with the 
trained model by entering arbitrary (English language) message text, and seeing the need categories predicted by the model.

## File Descriptions
The source code for the ETL and ML pipelines as well as usage examples and tests are in the two iPython notebooks in the main directory:
- `ETL_Pipeline_Preparation.ipynb`
- `ML_Pipeline_Preparation.ipynb`

Python scripts used to run the pipelines are autogenerated from these notebooks using [nbdev](https://github.com/fastai/nbdev).

These scripts and other code and resources needed for the web app are under the `udacity_root` folder.

## How to use:
1. Run the following commands in the project's `udacity_root` directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains the classifier and saves it for future use
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the `app` subdirectory to run the web app.
    `python run.py`

3. Go to http://localhost:3001/


