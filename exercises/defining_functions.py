#!/usr/bin/env python3
"""
defining_functions.py
GNU GPLv3 License
Demonstrates how to define and call basic functions in Python.
"""

def greet(name):
    """
    Returns a personalized greeting message.

    Args:
        name (str): Name to greet.

    Returns:
        str: Greeting message.
    """
    return f"Hello, {name}! Welcome to Python."

def add_numbers(a, b):
    """
    Adds two numbers and returns the result.

    Args:
        a (int or float)
        b (int or float)

    Returns:
        int or float: Sum of a and b.
    """
    return a + b

if __name__ == "__main__":
    print(greet("Alice"))
    print("Sum:", add_numbers(3, 4))
