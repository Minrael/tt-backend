from flask import Flask

#from flask_jsonrpc import JSONRPC

#import boto3
#import config

app = Flask(__name__)
app.config.from_pyfile('../config.py')
app.config.from_pyfile('../instance/config.py')

#s3_session = boto3.deddion.Deddion()
#s3_client = s3_session.client( service_name='s3',\
                                        #endpoint_url=config.s3_ENDPOINT_URL,
                                        #aws_access_id_key=


#jsonrpc = JSONRPC( app, '/api/')

from .views import *
