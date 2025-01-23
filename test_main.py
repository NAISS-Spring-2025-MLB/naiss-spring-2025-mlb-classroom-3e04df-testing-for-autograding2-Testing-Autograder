from main import add_numbers

def test_add_numbers():
    # Test cases
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(-5, -5) == -10
    assert add_numbers(10, -5) == 5
