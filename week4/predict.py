import pickle
import pandas as pd



with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

    categorical = ['PULocationID', 'DOLocationID']

def prepare_feature(ride): 
    features={}
    features['PU_DO']= f"{ride['PULocationID']}_{ride['DOLocationID']}"
    features['trip_distance']=ride['trip_distance']
    return features

def predict(feature):
    X = dv.transform(feature)
    preds= model.predict(X)
    return preds[0]

# app=  FastAPI()
# @app.get("/")
# def prediction_endpoint(request: Request): 
#     ride= request.json
#     features=  prepare_feature(ride)
#     pred= predict(features)
#     result={
#         'duration':pred
#     }
#     return result
