import unittest
from test_app import Revers_string

class TestWord(unittest.TestCase):
    
    def test_reverse(self):
        self.assertEqual(Revers_string('Hello'), 'olleH')
        self.assertEqual(Revers_string('World'), 'dlroW')
        self.assertEqual(Revers_string("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")


if __name__ == '__main__':
    unittest.main()
