import unittest
from users import Credentials


class CredentialTest(unittest.TestCase):
   
    def setUp(self):
        '''
        method run before each test
        '''
        self.new_account = Credentials("instagram","benjamin","myPassword")

    def tearDown(self):
        '''
        method run after each test
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test to check for correct initialization
        '''
        self.assertEqual(self.new_account.init_account,"instagram")
        self.assertEqual(self.new_account.account_username,"linda")
        self.assertEqual(self.new_account.account_password,"myPassword")


    def test_save_account(self):
        '''
        test method that checks if new account has been saved
        '''
        self.new_account.save_accounts()
        self.assertEqual(len(Credentials.credentials_list),1)

        
    def test_delete(self):
        '''
        test method to check if an account has been deleted
        '''
        self.new_account.save_accounts()
        new2_account = Credentials("Twitter", "Bob", "Sagers")
        new2_account.save_accounts()
        self.new_account.delete_passwords()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def test_dislay(self):
        '''
        test method to check whether accounts are displayed
        '''
        self.new_account.save_accounts()
        new2_account = Credentials("Facebook","Peter", "peter")
        new2_account.save_accounts()
        self.assertEqual(Credentials.display_passwords(),Credentials.credentials_list)

if __name__ == "__main__":
    unittest.main()