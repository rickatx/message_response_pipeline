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
