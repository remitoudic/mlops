from flask import Flask , request, jsonify
from predict import *

app=  Flask("duration-prediction")
@app.route('/predict', methods=["POST"])
def prediction_endpoint(): 

    ride = request.get_json()

    features=  prepare_feature(ride)
    pred= predict(features)
    result={
        'duration':pred
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)