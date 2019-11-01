import unittest
from solution import makeChange

class TestMakeChange(unittest.TestCase):

    def test_denominations(self):
        self.assertEqual(makeChange(25), 1)
        self.assertEqual(makeChange(10), 1)
        self.assertEqual(makeChange(5), 1)
        self.assertEqual(makeChange(1), 1)
    
    def test_four_pennies(self):
        self.assertEqual(makeChange(4), 4)
    
    def test_higher_number(self):
        self.assertEqual(makeChange(31), 3)

    if __name__ == '__main__':
        unittest.main()