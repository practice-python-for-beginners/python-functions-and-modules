import pytest
from exercises.importing_modules import random_square, calculate_circle_area, random_choice_from_list

def test_random_square():
    result = random_square()
    assert isinstance(result, int)
    assert result > 0

def test_calculate_circle_area():
    area = calculate_circle_area(2)
    assert round(area, 2) == 12.57  # πr² ≈ 12.566

def test_random_choice_from_list_valid():
    result = random_choice_from_list(["A", "B", "C"])
    assert result in ["A", "B", "C"]

def test_random_choice_from_list_empty():
    with pytest.raises(ValueError):
        random_choice_from_list([])
