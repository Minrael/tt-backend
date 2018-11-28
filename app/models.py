from .db import query_one





def list_chats2():
	pass

def create_chat2():
	pass

#def search_user():
#	return query_one("""	

#	SELECT user_id 
#	FROM users 
#	WHERE nick='All';
#	LIMIT %(limit)s;

#""")

def list_messages_by_chat(message_id, limit):
  return query_one("""
     SELECT user_id
     FROM messages
     WHERE message_id = %(message_id)s
     LIMIT %(limit)s
  """, message_id = int(message_id), limit = int(limit))
