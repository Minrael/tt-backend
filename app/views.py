from flask import request, abort, jsonify, json
from app import app

@app.route('/')
@app.route('/<string:name>')
def index(name="world"):
    return "Hello, {}!".format( name )

#@app.route('/form/', methods=['GET', 'POST'])
#def form():
#    if request.method =='GET':
#        return """<html>
#			<head></head>
#			<body>
#        		</body>
#		</html>"""
 #   else:
#        response = jsonify( )
#        return response



#@app.route('/user/<username>')
#  def user_profile(username):
#    return 'User %s' % username

@app.route('/chats/')
def chats():
  user_chats = jsonify('Football', '204', 'Cyclades')
  return user_chats

@app.route('/contacts/')
def contacts():
  user_contacts = jsonify('Vitek', 'Theodore', 'Nikitos', 'Vovan')
  return user_contacts

#@app.route('/contacts/add/')
#def new_contact():
#  user_contacts = jsonify('Vitek', 'Theodore', 'Nikitos', 'Vovan')
#  return user_contacts

#@app.route('/chats/create/', methods=['GET', 'POST'])
#def new_chat():

#return 




