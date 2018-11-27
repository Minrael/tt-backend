from flask import request, abort, jsonify, json
from app import app, jsonrpc
from .models import *


@app.route('/')

@app.route('/messages/')
def messages():
  message_id = int(request.args.get('message_id'))
  messages = model.list_messages_by_chat(message_id)
  return jsonify(messages)

#@app.route('/search_users/')
#def search_users():
#  id = search_user()
#  response = app.response_class( response = id, status=200 )
#  return response

@app.route('/<string:name>')
def index(name="world"):
    return "Hello, {}!".format( name )

@app.route('/user/<string:username>')
def user_profile(username):
  return 'User %s' % username

@app.route('/list_chats/')
def list_chats():
  user_chats_array = ['Football', '204', 'Cyclades']
  user_chats = json.dumps(user_chats_array)
  response = app.response_class(
      response = user_chats,
      mimetype='application/json',
      status=200

  )
  return response

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

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method =='GET':
      return """<html><head></head><body>
      <form method="POST" action="/form/">
         <input name="first_name" >
         <input name="last_name" >
         <input type="submit" >
      </form>
</body></html>
"""
    else:
      rv = jsonify(request.form)
      return rv


@app.route('/contacts/add/', methods=['GET', 'POST'])
def new_contact():
    if request.method =='GET':
      return """<html><head></head><body>
      <form method="POST" action="/form/">
         <input name="contact_name" >
         <input type="submit" >
      </form>
</body></html>
"""
    else:
      return 




@app.route('/chats/create_pers_chat/', methods=['GET', 'POST'])
def create_pers_chat():
    if request.method =='GET':
      return """<html><head></head><body>
      <form method="POST" action="/chats/create_pers_chat/">
         <input name="friend_name" >
         <input type="submit" >
      </form>
</body></html>
"""
    else:
      rv = jsonify(request.form)
      return rv
      return 

@app.route('/chats/create_group_chat/', methods=['GET', 'POST'])
def create_group_chat():
    if request.method =='GET':
      return """<html><head></head><body>
      <form method="POST" action="/form/">
         <input name="chat_name" >
         <input type="submit" >
      </form>
</body></html>
"""
    else:
      rv = jsonify(request.form)
      return rv
      return 

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


#@app.route('/chats/add/', methods=['GET', 'POST'])
#def new_chat():

#return 



