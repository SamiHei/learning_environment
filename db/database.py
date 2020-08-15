# --------------------------------------------------------
# Author: SamiHei
# 
# DatabaseModule contains
#    - Create database
#    - Create table(s)
#    - Database methods
# --------------------------------------------------------


import sqlite3

# TODO: Maybe test something with decorators??
class DatabaseModule:


    def __init__(self, db_name):
        self.db_name = db_name


    """
    Creates connection to database and returns the connection (if db doesn't exist, creates it)
    
    Excepts sqlite3 Error
    """
    def create_connection(self):
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(e)


    """
    Creates the tables for database if doesn't exist already 

    connection : sqlite3.connect
    """
    def create_tables(self, connection):
        try:
            self.create_users_table(connection)
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()2


    """
    Creates table for user data structures

    connection : sqlite3.connect
    """
    def create_users_table(self, connection):
        try:
            c = connection.cursor()
            c.execute('''
                      CREATE TABLE users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       first_name TEXT,
                       last_name TEXT, 
                       email TEXT);''')
            connection.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            c.close()

