# Disaster Response Messages ETL/ML Pipelines
> ETL and ML pipelines for processing/flagging disaster response messages.


## How to use

Place the scripts `process_data.py` and `train_classifier.py` in the directory you wish to run them from. 

Example command line invocations:

```shell
$ python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db
```

```bash
$ python train_classifier.py ../data/DisasterResponse.db classifier.pkl
```

## How to use:
1. Run the following commands in the project's `udacity_root` directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the `app` subdirectory to run the web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
