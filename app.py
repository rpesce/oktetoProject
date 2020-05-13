from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://okteto:okteto@mongodb:27017/okteto"
mongo = PyMongo(app)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route("/", methods=["GET"])
def get_messages():
    messages = []
    for m in mongo.db.messages.find():
        messages.append({"message": m["message"], "user": m["user"]})
    return jsonify(messages=messages)


@app.route("/", methods=["POST"])
def post_message():
    content = request.json
    mongo.db.messages.insert_one({"message": content["message"], "user": content["user"]})
    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)