#!/usr/bin/env python3
"""
arguments_and_returns.py
GNU GPLv3 License
Explains positional, keyword, and arbitrary function arguments.
"""

def describe_pet(pet_name, animal_type="dog"):
    """
    Describe a pet using default and keyword arguments.

    Args:
        pet_name (str)
        animal_type (str)

    Returns:
        str: A description sentence.
    """
    return f"{pet_name.title()} is a {animal_type.lower()}."

def multiple_sum(*args):
    """
    Calculate the sum of any number of numeric arguments.

    Args:
        *args: Variable length argument list.

    Returns:
        int or float: Sum of all provided values.
    """
    return sum(args)

def show_profile(**kwargs):
    """
    Display person profile information using keyword arguments.

    Args:
        **kwargs: Arbitrary keyword arguments.

    Returns:
        str: A formatted string description.
    """
    profile = [f"{key.capitalize()}: {value}" for key, value in kwargs.items()]
    return " | ".join(profile)

if __name__ == "__main__":
    print(describe_pet("Milo"))
    print("Sum of numbers:", multiple_sum(1, 2, 3))
    print(show_profile(name="Ada", age=30, city="London"))
