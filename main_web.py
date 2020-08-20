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
#    - Wrapper between endpoints and database code
# --------------------------------------------------------

# DOCS: https://fastapi.tiangolo.com/

from typing import Optional # Optional arguments for functions

from fastapi import FastAPI
from pydantic import BaseModel

from db.database import DatabaseModule

# Create the FastAPI app (title, description and version from conf file?)
app = FastAPI(title="Simple learning environment", description="Environment for WEB API and test automation",
              version="0.0.1")

# Database (Name from config file?)
db = DatabaseModule("database.db")


@app.get("/users")
def read_users():
    return db.get_users()


#===== Examples for the usage of FastAPI from the FastAPI documentation =======================
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
#=============================================================================================
