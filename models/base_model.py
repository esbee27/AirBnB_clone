#!/usr/bin/python3
"""A superclass"""

from uuid import uuid4y


class BaseModel:
    """A super class"""
    def __init__(self, *args, *kwargs):
        "Instabtiates the class"""
        if kwargs:
            for key, value in kwargs.items():
                if (key == "created_at") or (key == "updated_at"):
                    value = datetime.strptime(value, %Y-%m-%dT%H:%M:%S.%f)
                elif key == "__class__":
                    value =
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string reoresetation of the class"""
        return ({[]} {()} {}.format(self.class.__name__, self.id, self.__dict__))

    def save(self):
        """Updates updated_at with the current date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictiinary representation"""
        dic = self.__dict__
        dic['created_at'] = self.created_at
        dic['updated_at'] = self.updated_at
        dic['__class__'] = self.__class__.__name__
        return dic
