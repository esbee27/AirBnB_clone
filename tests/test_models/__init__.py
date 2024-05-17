#!/usr/bin/python3
""" Unique filestorage engine of our Application"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.relod()
