def calculate_age(birth_year):
    current_year = 2024
    age = current_year - birth_year
    return age
def test_calculate_age():
    assert calculate_age(1990) ==34
    assert calculate_age(2000) == 24
    assert calculate_age(1985) == 39