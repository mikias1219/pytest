from add import add_numbers, devide_numbers, multiply_numbers, subtract_numbers,power_numbers
# Test Functions
def test_add_numbers():
    """
    Test the add_numbers function with different inputs.
    """
    assert add_numbers(2, 3) == 5, "Should be 5"
    assert add_numbers(-1, 1) == 0, "Should be 0"
    assert add_numbers(0, 0) == 0, "Should be 0"
    assert add_numbers(10, 20) == 30, "Should be 30"

def test_devide_numbers():
    """
    Test the devide_numbers function with different inputs.
    """
    assert devide_numbers(10, 2) == 5, "Should be 5"
    assert devide_numbers(3, 3) == 1, "Should be 1"
    assert devide_numbers(1, 2) == 0.5, "Should be 0.5"
    assert devide_numbers(10, 5) == 2, "Should be 2"
    
    try:
        devide_numbers(10, 0)
        assert False, "Should raise ValueError when dividing by zero"
    except ValueError:
        pass  # Test passed if ValueError is raised

def test_multiply_numbers():
    """
    Test the multiply_numbers function with different inputs.
    """
    assert multiply_numbers(2, 3) == 6, "Should be 6"
    assert multiply_numbers(-1, 1) == -1, "Should be -1"
    assert multiply_numbers(0, 0) == 0, "Should be 0"
    assert multiply_numbers(10, 20) == 200, "Should be 200"

def test_subtract_numbers():
    """
    Test the subtract_numbers function with different inputs.
    """
    assert subtract_numbers(2, 3) == -1, "Should be -1"
    assert subtract_numbers(-1, 1) == -2, "Should be -2"
    assert subtract_numbers(0, 0) == 0, "Should be 0"
    assert subtract_numbers(10, 20) == -10, "Should be -10"
def test_power_numbers():
    """
    Test the power_numbers function with different inputs.
    """
    assert power_numbers(2, 3) == 8, "Should be 8"
    assert power_numbers(2, 0) == 1, "Should be 1"
    assert power_numbers(0, 3) == 0, "Should be 0"
    assert power_numbers(10, 2) == 100, "Should be 100"