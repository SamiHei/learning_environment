# --------------------------------------------------------
# Author: SamiHei
# 
# DatabaseModule contains
#    - Create database
#    - Create table(s)
#    - Database methods
# --------------------------------------------------------


import sqlite3


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
            connection.close()


    '''
    Decorator function for creating tables

    Wraps connection, commit and close to this function which is used in every table creation
    '''
    def create_table_decor(func):
        def wrapper(self, connection):
            try:
                c = connection.cursor()
                func(self, c)
                connection.commit()
            except sqlite3.Error as e:
                print(e)
            finally:
                c.close()
        return wrapper


    '''
    SQLite3 statement to create users table
    '''
    @create_table_decor
    def create_users_table(self, c):
        c.execute('''
                  CREATE TABLE users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   first_name TEXT,
                   last_name TEXT, 
                   email TEXT);''')

