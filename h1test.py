"""
Testing functions for h1.py
Mihaela
9/18/2018
"""

import unittest

from h1 import circle_area, is_even, miles_per_gallon
from h1 import average_odd_1_to_n
    
from math import pi

class TestHomework1(unittest.TestCase):
    """
    Test class has testing functions for h1.py functions
    """

    def test_circle_area(self):
        """
        Tests h1.circle_area( )
        """
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(10), pi * 100)
        self.assertEqual(circle_area(0), 0)

    def test_is_even(self):
        """
        Tests h1.is_even( )
        """
        self.assertEqual(is_even(2), True)
        self.assertEqual(is_even(1), False)
        self.assertEqual(is_even(0), True)

    def test_miles_per_gallon(self):
        """
        Tests h1.miles_per_gallon( )
        """
        self.assertEqual(miles_per_gallon(100, 10), 10)
        self.assertEqual(miles_per_gallon(200, 10), 20)
        self.assertEqual(miles_per_gallon(300, 10),30)

    def sum_of_1_to_n(n):
        """
        Tests h1.sum_of_1_to_n( )
        """
        self.assertEqual(sum_of_1_to_n(1), 1)
        self.assertEqual(sum_of_1_to_n(10), 55)
        self.assertEqual(sum_of_1_to_n(100), 5250)


    def test_average_odd_1_to_n(self):
        """
        Tests h1.average_odd_1_to_n( )
        """
        self.assertEqual(average_odd_1_to_n(1), 1)
        self.assertEqual(average_odd_1_to_n(6), 3)        
        self.assertEqual(average_odd_1_to_n(10), 5)

if __name__ == '__main__':
    unittest.main( )