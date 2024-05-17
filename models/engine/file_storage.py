#!/usr/bin/python3
"""Stores data in json format"""

class Fileorage:
    """Stores data"""
    __file_path = file.json
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
        for key in self.__objects:
            json_obj[key] = self.__object[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path))
        """
        for 
