#! /usr/bin/python3

# --------------------------------------------------------
# Author: SamiHei
# 
# Run the program
#    - Creates the FastAPI
#    - Contains API endpoints
#
# TODO:
#    - Config file for db name, host address etc?
#    - Commenting for endpoints
# --------------------------------------------------------

# DOCS: https://fastapi.tiangolo.com/

from typing import Optional # Optional arguments for functions

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from services.users import Users
from data_structures.user import User

# Create the FastAPI app (title, description and version from conf file?)
app = FastAPI(title="Simple learning environment", description="Environment for WEB API and test automation",
              version="0.0.1")

users = Users("database.db")


'''
Here some good commenting about this endpoint
'''
@app.get("/users")
def read_users():
    return users.get_all_users()


'''
Here some good commenting about this endpoint
'''
@app.post("/users")
async def create_user(user: User):
    if users.check_if_user_valid(user) is False:
        raise HTTPException(status_code=400, detail="Invalid JSON body data")
    else:
        users.create_user(user)
    return {"first_name": user.first_name, "last_name": user.last_name, "email": user.email}

