import unittest
from app import my_function


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_hello(self):
        self.assertEqual(my_function(), "Hello World!")

    def test_not_hello(self):
        self.assertNotEqual(my_function(), "Hello World!X")

