from flask import Flask, Response, request
import json
from NamedEntity import *

app = Flask(__name__)

@app.route('/home')
def home():
    return "Hello World!"

@app.route("/predict_entity", methods=["POST"])
def predict_entity():
    text = request.json["text"]
    model = NamedEntityService()
    entity_dict = model.get_entities(text)
    return Response(json.dumps(entity_dict), status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run()



