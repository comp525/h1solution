"""
h1.py
Mihaela
Created Feb 28, 2018
Updated Sep 18, 2018
"""

from math import pi, ceil
from random import randint

def circle_area(radius):
    """
    Calculates the area of a circle with given radius
    radius: non-negative float
    Returns: float
    """
    return pi * radius ** 2

def is_even(number):
    """
    Checks if number is even
    number: integer
    Returns: True if number is even, False otherwise
    """
    if number % 2 == 0:
        return True
    return False

def sum_of_1_to_n(n):
    """
    Calculates the sum of integers from 1 to given n
    Returns: integer
    """
    sum = 0
    for num in range(n + 1):
        sum = sum + 1
    return sum

def miles_per_gallon(miles, gallons):
    """
    Calcuates miles per gallons
    miles: positive float
    gallons: positive float
    Returns: float
    """
    return miles / gallons


def sum_ten_random_1_10_interval( ):
    """
    Returns sum of ten random integers in [1, 10] interval
    """
    sum = 0
    for count in range(1, 11):
        r = randint(1, 10)
        sum = sum + r
    return sum

def average_odd_1_to_n(n):
    """
    Calculates the average of odd integers between 1 and given n
    n: positive integer
    Returns: integer
    """
    sum = 0
    count = 0
    for num in range(1, n + 1):
        if not is_even(num):
            sum = sum + num
            count = count + 1
    return sum // count


def average_random_1_to_10(n):
    """
    Calcuate the average of random numbers between 1 and 10 (inclusive) 
    geneerated n times
    n: positive integer - how many times random numbers are generated
    Returns: integer
    """
    total = 0
    for count in range(n + 1):
        total = total + randint(1, 10)
    avg = total / n
    return avg



