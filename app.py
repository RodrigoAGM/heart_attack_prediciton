import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import time
from server.predict_model import Model

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
model = None


@app.route('/hello')
@cross_origin()
def hello():
    return 'Hello from Enzo Lizama, Rodrigo Guadalupe and Camilo Silva!'


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    post_data = request.data.decode("utf-8")
    data = json.load(post_data)
    
    start = time.time()
    res = model.predict(data)
    end = time.time()

    return {"response": "Chino pto", "probability": 100}


if __name__ == "__main__":
    model = Model()
    app.run(host='localhost')
