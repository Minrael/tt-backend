CREATE TABLE users (
	user_id   SERIAL PRIMARY KEY,
	name      TEXT NOT NULL
		  CHECK (length(name) < 32),
	nick      TEXT NOT NULL
		  CHECK (length(name) < 32),
	avatar    TEXT DEFAULT NULL
);


CREATE TABLE chats (
	chat_id         SERIAL PRIMARY KEY,
	is_group_chat   BOOLEAN DEFAULT FALSE,
	topic           TEXT NOT NULL,
	last_message    TEXT NOT NULL
);

CREATE TABLE messages (
	message_id   SERIAL PRIMARY KEY,
	user_id      INTEGER NOT NULL
		     REFERENCES users(user_id),
	content      TEXT NOT NULL
		     CHECK (length(content) < 65536),
	added_at     TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE members (
	member_id              SERIAL PRIMARY KEY,
	user_id                INTEGER NOT NULL
		               REFERENCES users(user_id),
	chat_id                INTEGER NOT NULL
		               REFERENCES chats(chat_id),
	new_messages           TEXT NOT NULL,
	last_read_message_id   INTEGER NOT NULL
);

CREATE TABLE attachment (

);
