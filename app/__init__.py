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
#app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
#profile_dir='profile/'

app.config.from_object('instance.config.ProductionConfig')
#app.config.from_object('instance.config.DevelopmentConfig')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://back:back@localhost/test_database'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://back:3NKHG9Oa@79.137.174.84/back'
      #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

#profiler_ = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

cache_ = MemcachedCache(['127.0.0.1:11211'])
#cache = Cache(app, config = {'CACHE_TYPE': 'simple'})
jsonrpc = JSONRPC( app, '/api/')


app.config.from_pyfile('../config.py')


from celery import Celery

#def make_celery(app):
#  celery = Celery(
#    app.import_name,
#    backend = app.config['result_backend'],
#    broker = app.config['broker_url']
#  )
#  celery.conf.update(app.config)

#  class ContextTask(celery.Task):
#    def __call__(self, *args, **kwargs):
#      with app.app_context():
#        return self.run(*args, **kwargs)

#  celery.Task = ContextTask
#  return celery


from .views import *
from .models import *
