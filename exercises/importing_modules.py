#!/usr/bin/env python3
"""
importing_modules.py
GNU GPLv3 License
Showcases importing both built-in and custom modules.
"""

import math
import random
from exercises.custom_module_example import square, cube

def random_square():
    """
    Generate a random integer between 1 and 10 and return its square.
    """
    num = random.randint(1, 10)
    return square(num)

def calculate_circle_area(radius):
    """
    Calculate the area of a circle using the math module.

    Args:
        radius (float)
    Returns:
        float: Area of the circle.
    """
    return math.pi * radius ** 2

def random_choice_from_list(items):
    """Return a random element from a given list."""
    if not items:
        raise ValueError("The list cannot be empty.")
    return random.choice(items)

if __name__ == "__main__":
    sample_list = ["apple", "banana", "cherry"]
    print("Random square:", random_square())
    print("Area of circle:", calculate_circle_area(5))
    print("Random item:", random_choice_from_list(sample_list))
