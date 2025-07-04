import os, gridfs, pika, json
from flask import Flask, request
from flask_pymongo import PyMongo
from auth import validate 
from auth_svc import access
from storage import util

server = Flask(__name__)
server.config["MONGO_URI"] = "mongodb://host.minikube.internal:27017/videos"

mongo = PyMongo(server)
fs = gridfs.GridFS(mongo.db)

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()

@server.route("/login", methods=["POST"])  # Fixed typo from "loging" to "login"
def login():
    token, err = access.login(request)
    if not err:
        return token
    else:
        return err

@server.route("/upload", methods=["POST"])  # Fixed "service" to "server"
def upload():
    access, err = validate.token(request)
    if err:  # Added error check
        return err
        
    access = json.loads(access)
    if access["admin"]:
        if len(request.files) != 1:  # Simplified file count check
            return "Exactly one file required", 400
            
        for _, f in request.files.items():
            err = util.upload(f, fs, channel, access)
            if err:
                return err
        return "Success!", 200
    else:    
        return "Not Authorized", 401

@server.route("/download", methods=["GET"])
def download():
    pass

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8080)
