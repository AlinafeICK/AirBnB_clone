#!/usr/bin/python3
""" Base Model """

from uuid import uuid4
from datetime import datetime
import models   # pylint: disable=import-error  

class BaseModel:
    id = ""
    created_at = datetime.now()
    updated_at = datetime.now()

def __init__(self, *args, **kwargs):
    super(CLASS_NAME, self).__init__(*args, **kwargs)

def save():
    pass
def to_json():
    pass

class user(BaseModel):
    pass

class state(BaseModel):
    pass

class city(BaseModel):
    pass

class place(BaseModel):
    pass    