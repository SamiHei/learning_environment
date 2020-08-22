# --------------------------------------------------------
# Author: SamiHei
# 
# Wrapper for handling:
#    - User database
#    - User data structures
#
# --------------------------------------------------------


import json

from data_structures.user import User
from db.database import DatabaseModule


class Users:

    # Database (Name from config file?)
    def __init__(self, db_name):
        self.db = DatabaseModule(db_name)


    '''
    Stupid check to see if any of the fields are empty
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

