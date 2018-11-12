from flask import request, abort, jsonify, json
from app import app

@app.route('/')
@app.route('/<string:name>')
def index(name="world"):
    return "Hello, {}!".format( name )

@app.route('/user/<string:username>')
def user_profile(username):
  return 'User %s' % username

@app.route('/chats/')
def chats():
  user_chats = ['Football', '204', 'Cyclades']
  user_chs = json.dumps(user_chats)
  response = app.response_class(
      response = user_chs,
      mimetype='application/json',
      status=200

  )
  return response

@app.route('/contacts/')
def contacts():
  user_contacts = ['Vitek', 'Theodore', 'Nikitos', 'Vovan']
  user_cs = json.dumps(user_contacts)
  response = app.response_class(
      response = user_cs,
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
      print(5)
      abort(404) 


@app.route('/chats/add/', methods=['GET', 'POST'])
def new_chat():
    if request.method =='GET':
      return """<html><head></head><body>
      <form method="POST" action="/form/">
         <input name="chat_name" >
         <input type="submit" >
      </form>
</body></html>
"""
    else:
      #request.form['chat_name']
      return 
      print(6)
      abort(404) 


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
      #request.form['chat_name']
      return 
      print(6)
      abort(404) 

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




