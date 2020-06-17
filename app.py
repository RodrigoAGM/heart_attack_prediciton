import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
from server.predict_model import Model

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:8080"}})
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
    data = json.loads(post_data)

    for key in data:
        data[key] = float(data[key])

    print(data)

    res = model.predict(data)
    message = "El paciente no sufrirá de un ataque al corazón"

    if res:
        message = "El paciente puede sufrir de un ataque al corazón"

    return {"response": message, "probability": model.mean}


if __name__ == "__main__":
    model = Model()
    app.run(host='localhost')
