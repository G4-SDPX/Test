import unittest
from test_app import reverse_str

class TestWord(unittest.TestCase):
    
    def test_reverse(self):
        self.assertEqual(reverse_str(('Hello'), 'olleH'))
        self.assertEqual(reverse_str('World'), 'dlroW')
        # self.assertEqual(Revers_string("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")


if __name__ == '__main__':
    unittest.main()
