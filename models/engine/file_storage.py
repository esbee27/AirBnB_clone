#!/usr/bin/python3
"""Stores data in JSON format"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Stores data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary of __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)"""
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_obj = json.load(file)
                for key, value in json_obj.items():
                    class_name = value["__class__"]
                    cls = globals()[class_name]
                    self.__objects[key] = cls(**value)
