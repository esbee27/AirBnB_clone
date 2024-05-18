#!/usr/bin/python4
"""A superclass"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """A super class"""
    def __init__(self, *args, **kwargs):
        "Instabtiates the class"""
        if kwargs:
            for key, value in kwargs.items():
                if (key == "created_at") or (key == "updated_at"):
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    value = setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string reoresetation of the class"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictiinary representation"""
        dic = self.__dict__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        dic['__class__'] = self.__class__.__name__
        return dic
