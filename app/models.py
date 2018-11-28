from .db import *

def list_chats_db():
	return query_all("""	
	SELECT chat_id, topic 
	FROM chats 
        """)

def create_chat(topic):
    insert_into_bd("""	
	INSERT INTO chats ( is_group_chat, topic, last_message )
	VALUES (false, %(topic)s, '0');
    """, topic = str(topic))

    commit_db()


#Search user id by nick
def search_user(nick):
	return query_all("""	
	SELECT user_id 
	FROM users 
	WHERE nick = %(nick)s;
        """, nick = str(nick))

def all_users_name():
	return query_all("""	
	SELECT name 
	FROM users 
        """)

def list_messages_by_chat(user_id, limit):
  return query_all("""
     SELECT message_id
     FROM messages
     WHERE user_id = %(user_id)s
     LIMIT %(limit)s;
  """, user_id = int(user_id), limit = int(limit))
