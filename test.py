import unittest
from users import User

class UserTest(unittest.TestCase):

 def setUp(self):
        '''
        method run before each user test
        '''
        self.new_user = User("Mary", "1234")

def tearDown(self):
        '''
        method called after each user test
        '''
        User.users_list = []

def test_init(self):
        '''
        test method to check if user class is initialize
        '''
        self.assertEqual(self.new_user.init_username,"Mary")
        self.assertEqual(self.new_user.init_password, "1234")
        
def test_save_user(self):
        '''
        test method to test if user has been saved
        '''
        self.new_user.save_users()
        self.assertEqual(len(User.users_list),1)

def test_user(self):
        '''
        test method to test if user has been save
        '''
        self.new_user.save_users()
        self.assertEqual(len(User.users_list),1)