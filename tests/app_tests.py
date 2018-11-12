import unittest

from app import app

class AppTest(unittest.TestCase):

    def setUp(self): 
        self.app = app.test_client()       



if __name__ == "__main__":
     unittest.main()
    
