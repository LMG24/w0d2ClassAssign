import unittest
from main import hello_world
from main import greet_person

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Welcome to Git!")

class TestGreetPerson(unittest.TestCase):
    def test_greet_person(self):
        self.assertEqual(hello_world("John"), "Hello, John!")

if __name__ == '__main__':
    unittest.main()