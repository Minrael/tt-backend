from flask import Flask

from flask_jsonrpc import JSONRPC

from werkzeug.contrib.cache import SimpleCache
from werkzeug.contrib.cache import MemcachedCache
from werkzeug.contrib.profiler import ProfilerMiddleware

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_cache import Cache

#import boto3
#import config

app = Flask(__name__)

app.config['PROFILE']=True
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
#profile_dir='profile/'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://back:back@localhost/back_orm'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

#profiler_ = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

cache_ = MemcachedCache(['127.0.0.1:11211'])
#cache = Cache(app, config = {'CACHE_TYPE': 'simple'})
jsonrpc = JSONRPC( app, '/api/')


app.config.from_pyfile('../config.py')



from .views import *
from .models import *
