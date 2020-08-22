#! /usr/bin/python3

# --------------------------------------------------------
# Author: SamiHei
# 
# Run the program
#    - Creates the FastAPI
#    - Contains API endpoints
#
# TODO:
#    - Endpoints for updating user and delete user
#    - TODOs in comments
#
# DOCS:
#    - https://fastapi.tiangolo.com/
# --------------------------------------------------------


# Configs
from config import VERSION, DB_NAME, FAST_API_TITLE, FAST_API_DESCRIPTION

# Python packages
# from typing import Optional # Optional arguments for functions
from fastapi import FastAPI, HTTPException

# Local libs
from services.users import Users
from data_structures.user import User


# Create the FastAPI app
app = FastAPI(title=FAST_API_TITLE, description=FAST_API_DESCRIPTION,
              version=VERSION)

users = Users(DB_NAME)


'''
GET all users
'''
@app.get("/users")
def read_users():
    return users.get_all_users()


'''
Create users with POST request

Arguments:
    - user = User data structure

Returns:
    - user = Created user json body

Request body:
    {
      "first_name": "example"
      "last_name": "user"
      "email": "example.user@email.test"
    }

TODO:
   - Check that email is unique
   - Better verification for user overall
   - HTTP Error codes
'''
@app.post("/users", status_code=201)
async def create_user(user: User):
    if users.check_if_user_valid(user) is False:
        raise HTTPException(status_code=400, detail="Invalid JSON body")
    else:
        users.create_user(user)
    return user

