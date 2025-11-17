from exercises.defining_functions import greet, add_numbers

def test_greet():
    assert "Hello" in greet("Alice")
    assert "Alice" in greet("Alice")

def test_add_numbers():
    assert add_numbers(5, 7) == 12
    assert add_numbers(-2, 3) == 1
