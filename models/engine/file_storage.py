#!/usr/bin/python3
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User

"""Stores data in json format"""

class Filestorage:
    """Stores data"""
    __file_path = "file.json"
    __object = {}

    def all(self):
        """Returns dictionary of __object
        """
        return self.__object
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + str(self.id)
        self.__object[key] = obj
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        
        json_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(json_object, file)
        """
        for key in self.__objects:
            json_obj[key] = self.__object[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file)"""
            
    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path))
        """
        if exists(self.__file_path):
            with open(self.__self_path, 'r') as file:
                json_obj = json.load(file)
                for key, value in json_obj.items():
                    class_name = value["__class__"]
                    cls = globals()[class_name]
                    self.__objects[key] = cls(**value)
