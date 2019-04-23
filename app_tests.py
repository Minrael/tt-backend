import unittest

from app import app

class AppTest(unittest.TestCase):

    def setUp(self): 
        self.app = app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(b'Hello, world!', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("text/html", rv.mimetype)   

    def test_list_chats(self):
        rv = self.app.get('/list_chats/')
        self.assertEqual(b'["Football", "204", "Cyclades"]', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)  

    def test_list_contacts(self):
        rv = self.app.get('/list_contacts/')
        self.assertEqual(b'["Vitek", "Theodore", "Nikitos", "Vovan"]', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)     

    def test_create_pers_chat_post(self):
        rv = self.app.post('/chats/create_pers_chat/', data = {"friend_name": "Marina"})
        self.assertEqual(b'{"friend_name":"Marina"}\n', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype) 

    def test_create_group_chat_get(self):
        rv = self.app.post('/chats/create_pers_chat/', data = {"chat_name":"Helloween"})
        self.assertEqual(b'{"chat_name":"Helloween"}\n', rv.data)
        self.assertEqual(200, rv.status_code)
        self.assertEqual("application/json", rv.mimetype)  

if __name__ == "__main__":
     unittest.main()
    
