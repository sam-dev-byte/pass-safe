class User: 

    """
    Create new instance of users
    """

    users_list = []


def __init__(self,init_username,init_password):

    self.init_username = init_username
    self.init_password = init_password


def save_users(self):

    """
    Method to save users and their password to the user_list.
    """
    
    User.users_list.append(self)


class Credentials:

    """
    Creates new accounts Credentials of a user.
    """

    credentials_list = []

def __init__ (self,init_account,account_username,account_password):

    self.init_account = init_account
    self.account_username = account_username
    self.account_password = account_password

def save_account(self):

    """
    method to save account
    """

    Credentials.credentials_list.append(self)

def delete_passwords(self):

    """
    Method to delete password accounts
    """

    Credentials.credentials_list.remove(self)

@classmethod
def display_passwords(cls):

    """
    Method to display passwords saved
    """

    return cls.credentials_list


@classmethod
def search_passwords(cls, search_accounts):
    
    """
    Method to search for saved passwords accounts
    """

    for account in cls.credentials_list:
        if account.init_account == search_accounts:
            return account 