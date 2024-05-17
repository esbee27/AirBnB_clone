#!/usr/bin/python3
from base_model import BaseModel
""" class user that catch user details """
class User(BaseModel):
    """ Class user that inherit from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
