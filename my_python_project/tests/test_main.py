import unittest
from app.utils import greet_user

class TestUtils(unittest.TestCase):
    def test_greet_user(self):
        self.assertEqual(greet_user("Alice"), "Hello, Alice! Welcome to Python 🚀")

if __name__ == "__main__":
    unittest.main()
