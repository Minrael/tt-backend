from app import db


class UserUser(db.Model):
    id = db.Column(db.Integer, unique = True, nullable=False, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    nick = db.Column(db.String(90), unique = True, nullable=False)

    message = db.relationship('Message', backref = 'user_user', lazy=True)
    member = db.relationship('Member', backref = 'user_user', lazy=True)

    def __init__(self, name, nick):
        self.name=name
        self.nick = nick

class Chat(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    is_group_chat = db.Column(db.Boolean, nullable=False)
    topic = db.Column(db.String(90), nullable=False)
    last_message = db.Column(db.String(90))

    message = db.relationship('Message', backref = 'chat_y', lazy=True)
    member = db.relationship('Member', backref = 'chat', lazy=True)


    def __init__(self, is_group_chat, topic):
        self.is_group_chat=is_group_chat
        self.topic = topic

class Message(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_user.id'))
    content = db.Column(db.String(500))

    member = db.relationship('Member', backref = 'message', lazy=True)

class Member(db.Model):
    id = db.Column(db.Integer, unique = True, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_user.id'))
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))
    new_messages = db.Column(db.Integer, nullable=False)
    last_read_message_id = db.Column(db.Integer, db.ForeignKey('message.id'))



