#!/usr/bin/python3
import unittest
import console
from console import HBNBCommand

class test_console(unittest:TestCase):
    """ class to test our command application"""
    def create(self):
        return HBNBCommand()

    def test_quit(self):
        command = self.create()
        self.assertTrue(command.onecmd("quit"))

    def test_EOF(self):
        command =self.create()
        self.assertTrue(command.onecmd("EOF")
