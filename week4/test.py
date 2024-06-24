import predict
import requests
import json


ride={
   "PULocationID":10,
   "DOLocationID":10,
   "trip_distance":50
}

# features= predict.prepare_feature(ride)
# pred=predict.predict(features)
# print(pred)


url='http://0.0.0.0:9696/predict'
response=requests.post(url , json=ride)
print(response.json())