from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://database:27017/")
db = client["projectdb"]
collection = db["messages"]

@app.route("/send", methods=["POST"])
def send_message():
    msg = request.json["message"]
    collection.insert_one({"message": msg})
    return {"status": "Message saved successfully"}

app.run(host="0.0.0.0", port=5000)
