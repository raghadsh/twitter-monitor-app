from flask import Flask
from flask import  Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
@app.route('/')
def hello_world():
  return 'Hello from new flask !'
if __name__ == '__main__':
  app.run()