#! /usr/bin/python3

# --------------------------------------------------------
# Author: SamiHei
# 
# This file contains scripts
#    -To create the database (sqlite3) and tables
#    -Create and/or set other environmental requirements
# --------------------------------------------------------

import os
import sqlite3

from db.database import DatabaseModule


db_name = "database.db"
db = DatabaseModule(db_name)


def main():
    
    # Create database if not existing already
    try:
        if not (os.path.isfile(db_name)):
            con = db.create_connection()
            db.create_tables(con)
        else:
            print("Database already exists!")
    except sqlite3.Error as e:
        print(e)
    finally:
        con.close()

    # Create and/or set environmental requirements


if __name__ == '__main__':
    main()
