from app import db

#class Person(db.Model):
#    id = db.Column(db.Integer, unique = True, nullable=False, primary_key=True)
#    username = db.Column('nickname', db.String(90), unique = True, nullable=False)
#    first_name = db.Column('second_name', db.String(90), unique = True, nullable=True)

#    def __init__(self, username, first_name = ''):
#        self.username=username
#        self.first_name = first_name


class User(db.Model):
    id = db.Column(db.Integer, unique = True, nullable=False, primary_key=True)
    name = db.Column(db.String(90), unique = True, nullable=False)
    nick = db.Column(db.String(90), unique = True, nullable=False)

    message = db.relationship('Message', backref = 'user', lazy=True)
    member = db.relationship('Member', backref = 'user', lazy=True)

    def __init__(self, name, nick):
        self.name=name
        self.nick = nick

class Chat(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    is_group_chat = db.Column(db.Boolean, unique = True, nullable=False)
    topic = db.Column(db.String(90), unique = True, nullable=False)
    last_message = db.Column(db.String(90), unique = True, nullable=False)

    message = db.relationship('Message', backref = 'chat_y', lazy=True)
    member = db.relationship('Member', backref = 'chat', lazy=True)

    def __init__(self, is_group_chat, topic, last_message):
        self.is_group_chat=is_group_chat
        self.topic = topic
        self.last_message = last_message

class Message(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.String(500))

    member = db.relationship('Member', backref = 'message', lazy=True)

    def __init__(self, content):
        self.content = content

class Member(db.Model):
    id = db.Column(db.Integer, unique = True, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))
    new_messages = db.Column(db.String(90), unique = True, nullable=False)#counter
    last_read_message_id = db.Column(db.Integer, db.ForeignKey('message.id'))



