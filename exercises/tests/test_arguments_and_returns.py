from exercises.arguments_and_returns import describe_pet, multiple_sum, show_profile

def test_describe_pet_defaults():
    assert describe_pet("Buddy") == "Buddy is a dog."

def test_multiple_sum():
    assert multiple_sum(1, 2, 3, 4) == 10

def test_show_profile():
    result = show_profile(name="Bob", city="Paris")
    assert "Name: Bob" in result
    assert "City: Paris" in result
