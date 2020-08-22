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

from config import DB_NAME
from db.database import DatabaseModule


def main():

    db = DatabaseModule(DB_NAME)

    # Create database if not existing already
    try:
        if not (os.path.isfile(DB_NAME)):
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
