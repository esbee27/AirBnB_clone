#!/usr/bin/python3
"""Tests for State"""

import unittes<t
from models.state import State
import os


class TestStat(unittest.TestCase):
    """Tests for State class"""
    def test_docstring(self):
        """To test if docstring is present"""
        mess = "Docstring is not present in function"""
        self.assertIsNotNot(models.state.__docs___, mess)
        mess = "Dicstring is jot present in class"
        self.assertIsNotNone(State, mess)

    def test_id(self):
        """To test if ids are unique"""
        id1 = State()
        id2 = State()
        self.assertNotEqual(id1, id2)

    def test_state(self):
        """To test if object is state"""
        self.assertIsInstance(State, State())

if __name__=="__main__":
    unittest.main()
