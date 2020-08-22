# --------------------------------------------------------
# Author: SamiHei
# 
# Wrapper for handling:
#    - User database
#    - User data structures
#
# --------------------------------------------------------


import json
import re

from data_structures.user import User
from db.database import DatabaseModule


class Users:


    def __init__(self, db_name):
        self.db = DatabaseModule(db_name)


    '''
    Simple check to see if any of the fields are empty
    '''
    def check_if_user_valid(self, user):
        if user.first_name is "":
            return False
        elif user.last_name is "":
            return False
        elif user.email is "":
            return False
        return True


    '''
    Return false if email is already used
    '''
    def check_if_email_unique(self, user):
        users_data = self.db.get_users()
        for user_data in users_data:
            if user.email in user_data:
                return False
        return True


    '''
    Checks the email format using regex
    '''
    def check_if_email_valid(self, user):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if(re.search(regex, user.email)):
            return True
        return False


    '''
    Uses the database module to get all users from the database
    '''
    def get_all_users(self):
        return self.db.get_users()


    '''
    Uses the database module to create new user

    Arguments:
       - user = User data structure object
    '''
    def create_user(self, user):
        self.db.create_user(user)

