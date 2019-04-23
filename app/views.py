from flask import request, abort, jsonify, json
from app import app, jsonrpc, cache_, db #, profiler_
import json
import time
from .models import *
import random

import socket

from .models import UserUser
from .models import Chat

from functools import wraps
from flask import g, request, redirect, url_for

#Caching function
def item_name(name_for_cache):
  def get_my_item(function):
    def wrapper( *args, **kwargs):
      rv = cache_.get(name_for_cache)
      if rv is None:
        rv = function(*args, **kwargs)
        cache_.set(name_for_cache, rv, timeout=5*60)
      print(rv)
      return rv
    return wrapper
  return get_my_item

#@app.route('url_viewer')
#def url_viewer():
#  urls =['https://mail.ru', 'https://ya.ru', 'https://google.com']
#  url = random.choice(urls)
#  sock = socket.socket()
  #sock.timeout(5)


#Index page
@app.route('/')
def index_page():
  #time.sleep( 2 )
  return "Hello!"

#Users profile
@app.route('/user/<string:username>')
def user_profile(username):
  return 'User %s' % username

#Create new user. Nick is unique
@app.route('/user/create_new_user/', methods=['GET', 'POST'])
def create_new_user():
    if request.method =='GET':
      return """<html><head></head><body>
      <form method="POST" action="/create/user/">
         <input name="name" >
         <input name="nick" >
         <input type="submit" >
      </form>
      </body></html>
      """
    else:
      name = request.form['name']
      nick = request.form['nick']
      user = UserUser(name, nick)
      db.session.add(user)
      db.session.commit()
    
    return jsonify(request.form)

#Adds new chat in chats(group=false)
@app.route('/chats/create_pers_chat/', methods=['GET', 'POST'])
def create_pers_chat():
    if request.method =='GET':
      return """<html><head></head><body>
      <form method="POST" action="/chats/create_pers_chat/">
         <input name="chat_name" >
         <input type="submit" >
      </form>
      </body></html>
      """
    else:
      topic = request.form['chat_name']
      chat = Chat(False, topic)
#      member = Member(user, chat)
      db.session.add(chat)
      db.session.commit()
      cache_.delete('list_chats')
      return chat.topic

#Adds new chat in chats(group=true)
@app.route('/chats/create_group_chat/', methods=['GET', 'POST'])
def create_group_chat():
    if request.method =='GET':
      return """<html><head></head><body>
      <form method="POST" action="/chats/create_group_chat/">
         <input name="chat_name" >
         <input type="submit" >
      </form>
      </body></html>
      """
    else:
      topic = request.form['chat_name']
      chat = Chat(True, topic)
      db.session.add(chat)
      db.session.commit()
      cache_.delete('list_chats')
      return chat.topic

def chat_to_json(chat):
  res = {}
  res['id'] = chat.id
  res['topic'] = chat.topic
  return res
   
#Shows the list of chats topics(topic FROM chats) using cache
@app.route('/list_chats/')
@item_name('list_chats')
def list_chats():
  user_chats = Chat.query.all()
  return jsonify([ chat_to_json(chat) for chat in user_chats])


@app.route('/search_user_by_nick/', methods=['GET', 'POST'])
def search_user_by_nick():
    if request.method =='GET':
      return """<html><head></head><body>
      <form method="POST" action="/search_user_by_nick/">
         <input name="user_nick" >
         <input type="submit" >
      </form>
      </body></html>
      """
    else:
      u_nick = request.form['user_nick']
      found_user_id = Chat.query.filter(User.nick(u_nick)).all()
      response = app.response_class(
          response = found_user_id,
          mimetype='application/json',
          status=200
      )
    return response

#@app.route('/create/<string:name>')
#def create_user(name):
#    first_name = random.choice(["Tom", "Jerry", "Mike"])
#    person = Person(name, first_name)
#    db.session.add(person)
#    db.session.commit()
#    return first_name





#Shows the list of users as JSON
@app.route('/all_users/')
def all_users():
      response = app.response_class(
          response = json.dumps(all_users_name()),
          mimetype='application/json',
          status=200
      )
      return response




#Shows 10 last messages of chat, user_id=1
@app.route('/messages/')
def messages():
  messages = list_messages_by_chat(1, 10)
  return jsonify(messages)


#Static json 
@app.route('/list_contacts/')
def list_contacts():
  user_contacts_array = ['Vitek', 'Theodore', 'Nikitos', 'Vovan']
  user_contacts = json.dumps(user_contacts_array)
  response = app.response_class(
      response = user_contacts,
      mimetype='application/json',
      status=200

  )
  return response



#@app.route('/<string:name>')
#def index(name="world"):
#    return "Hello, {}! Random: {}".format( name, get_random( 10 ) )



#@app.route('/contacts/add/', methods=['GET', 'POST'])
#def new_contact():
#    if request.method =='GET':
#      return """<html><head></head><body>
#      <form method="POST" action="/form/">
#         <input name="contact_name" >
#         <input type="submit" >
#      </form>
#</body></html>
#"""
#    else:
#      return 

#@app.route('/chats/add_members_to_group_chat/', methods=['GET', 'POST'])
#def add_members_to_group_chat():

#@app.route('/chats/leave_group_chat/', methods=['GET', 'POST'])
#def leave_group_chat():

#@app.route('/chats/send_message/', methods=['GET', 'POST'])
#def send_message():

#@app.route('/chats/read_message/', methods=['GET', 'POST'])
#def read_message():

#@app.route('/chats/upload_file/', methods=['GET', 'POST'])
#def upload_file():

#Shows 10 last messages of chat, user_id=1
#@app.route('/messages/')
#def messages():
  #message_id = int(request.args.get('message_id'))
  #messages = list_messages_by_chat(1, 10)    #user_id=1 limit=10
  #return jsonify(messages)



#12-11-18

#@jsonrpc.method( 'api.upload_file' )
#def upload_file( Bucket=config.S3_BUCKET_NAME, Key=filename, Body=b64content ):

#( Bucket=config.S3_BUCKET_NAME, Key=filename, Body=b64content )
 # return b64content

#@jsonrpc.method( 'api.download_file' )
#def download_file( b64content, filename):
#  response = s3_client.get_object( Bucket=config.S3_BUCKET_NAME, Key=filename)
#  print( response.get('Body'), dir( response ))
#  return response.get('Body')



#def profile( function):
#  def wrapper(*args, **kwargs):
#    profile_filename = "{}.prof".format( function.__name__)
#    profiler = profiler_
#    result = profiler.runcall(function, *args, **kwargs)
#    profiler.damp_stats(profile_filename)
#    return result
#  return wrapper


#def login_required(f):
#    @wraps(f)
#    def decorated_function(*args, **kwargs):
#        if g.user is None:
#            return redirect(url_for('login', next=request.url))
#        return f(*args, **kwargs)
#    return decorated_function


#@app.route('/secret_page/')
#@login_required
#def secret_page():
#    pass

