#! /usr/bin/python3

# --------------------------------------------------------
# Author: SamiHei
# 
# Run the program
#    - Creates the FastAPI
#    - Contains API endpoints
# --------------------------------------------------------

# DOCS: https://fastapi.tiangolo.com/

from typing import Optional # Optional arguments for functions

from fastapi import FastAPI
from pydantic import BaseModel

# Create the FastAPI app
app = FastAPI()


#===== Examples for the usage of FastAPI =======================
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
#==============================================================

