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
    return flask.g.dbconn

def _rollback_db(sender, exception, **extra):
    if hasattr(flask.g, 'dbconn'):
       conn = flask.g.dbconn
       conn.rollback()
       conn.close()
       delattr(flask.g, 'dbconn')

def get_cursor():
    return get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)

def query_one(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        return str(cur.fetchone())

def query_all(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        row = [index[0] for index in cur.fetchall()]
        return row

def insert_into_bd(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)


#flask.got_request_exception.connect(_rollback_db, app)



#TODO _commit_db

#def commit_db():

