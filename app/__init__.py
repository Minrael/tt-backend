from flask import Flask

from flask_jsonrpc import JSONRPC

#import boto3
#import config

app = Flask(__name__)
jsonrpc = JSONRPC( app, '/api/')

app.config.from_pyfile('../config.py')
#app.config.from_pyfile('../instance/config.py')


from .views import *
