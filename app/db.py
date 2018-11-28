import flask
import psycopg2
import config
from config import BaseConfig
import psycopg2.extras
import config
from app import app

def get_connection():
    if not hasattr(flask.g, 'dbconn'):
        flask.g.dbconn = psycopg2.connect(
            database=BaseConfig.DB_NAME, host=BaseConfig.DB_HOST,
            user=BaseConfig.DB_USER, password=BaseConfig.DB_PASS)
    print(3)
    return flask.g.dbconn

def _rollback_db(sender, exception, **extra):
    if hasattr(flask.g, 'dbconn'):
       conn = flask.g.dbconn
       conn.rollback()
       conn.close()
       delattr(flask.g, 'dbconn')

def get_cursor():
    print(2)
    return get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)

def query_one(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        print(1)
        return cur.fetchone()

#flask.got_request_exception.connect(_rollback_db, app)



#TODO _commit_db

#def commit_db():

