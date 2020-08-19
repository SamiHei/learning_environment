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

    Arguments:
       connection = sqlite3.connect
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

    Arguments:
        connection = sqlite3 connection
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
    SQLite3 statement to CREATE users table
    '''
    @create_table_decor
    def create_users_table(self, c):
        c.execute('''
                  CREATE TABLE users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   first_name TEXT,
                   last_name TEXT, 
                   email TEXT UNIQUE);''')


    '''
    Decorator function for INSERT and UPDATE statements

    Wraps connection, commit and close to this function which is used in every insert

    Arguments:
        *args = Values to be given for the statement
    '''
    def set_data_decor(func):
        def wrapper(self, *args):
            try:
                con = self.create_connection()
                c = con.cursor()
                func(self, c, *args)
                con.commit()
            except sqlite3.Error as e:
                print(e)
            finally:
                c.close()
                con.close()
        return wrapper


    '''
    SQLite3 statement to INSERT user
    '''
    @set_data_decor
    def create_user(self, c, user):
        c.execute('''
                  INSERT INTO users (first_name, last_name, email)
                  VALUES(?, ?, ?);''', (user.get_first_name(), user.get_last_name(), user.get_email()))


    '''
    Decorator function for SELECT statements

    Wraps connection and close to this function which is used in every insert

    Arguments:
        *args = Values to be given for the statement

    Returns:
        Data from the SELECT statement
    '''
    def get_data_decor(func):
        def wrapper(self, *args):
            try:
                con = self.create_connection()
                c = con.cursor()
                data = func(self, c, *args)
            except sqlite3.Error as e:
                print(e)
            finally:
                c.close()
                con.close()
            return data
        return wrapper


    '''
    SQLite3 statement to GET all users

    Arguments:
        c = sqlite3 connection cursor

    Returns:
        Data from the SELECT statement
    '''
    @get_data_decor
    def get_users(self, c):
        c.execute('SELECT * from users')
        return c.fetchall()

