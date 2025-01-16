from add import *

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
def test_get_greeting():
    """
    Test the get_greeting function with different inputs.
    """
    assert get_greeting("Alice") == "Hello, Alice!", "Should be 'Hello, Alice!'"
    assert get_greeting("Bob") == "Hello, Bob!", "Should be 'Hello, Bob!'"
    assert get_greeting("Charlie") == "Hello, Charlie!", "Should be 'Hello, Charlie!'"
    assert get_greeting("David") == "Hello, David!", "Should be 'Hello, David!'"
def test_log_nums():
    """ 
    Test the log_nums function with different inputs.
    """
    assert log_nums(10, 100) == (2.302585092994046, 4.605170185988092), "Should be (2.302585092994046, 4.605170185988092)"
    assert log_nums(1, 1) == (0.0, 0.0), "Should be (0.0, 0.0)"
    assert log_nums(2, 2) == (0.6931471805599453, 0.6931471805599453), "Should be (0.6931471805599453, 0.6931471805599453)"
    assert log_nums(10, 10) == (2.302585092994046, 2.302585092994046), "Should be (2.302585092994046, 2.302585092994046)"
def test_sqrt_nums():
    """ 
    Test the sqrt_nums function with different inputs.
    """
    assert sqrt_nums(10, 100) == (3.1622776601683795, 10.0), "Should be (3.1622776601683795, 10.0)"
    assert sqrt_nums(1, 1) == (1.0, 1.0), "Should be (1.0, 1.0)"
    assert sqrt_nums(2, 2) == (1.4142135623730951, 1.4142135623730951), "Should be (1.4142135623730951, 1.4142135623730951)"
    assert sqrt_nums(10, 10) == (3.1622776601683795, 3.1622776601683795), "Should be (3.1622776601683795, 3.1622776601683795)"
def test_abs_nums():
    """
    Test the abs_nums function with different inputs.
    """
    assert abs_nums(-10, 100) == (10, 100), "Should be (10, 100)"
    assert abs_nums(-1, 1) == (1, 1), "Should be (1, 1)"
    assert abs_nums(2, -2) == (2, 2), "Should be (2, 2)"
    assert abs_nums(-10, -10) == (10, 10), "Should be (10, 10)"
def test_floor_nums():
    """
    Test the floor_nums function with different inputs.
    """
    assert floor_nums(10.5, 100.9) == (10, 100), "Should be (10, 100)"
    assert floor_nums(1.1, 1.9) == (1, 1), "Should be (1, 1)"
    assert floor_nums(2.9, 2.1) == (2, 2), "Should be (2, 2)"
    assert floor_nums(10.1, 10.5) == (10, 10), "Should be (10, 10)"
def test_ceil_nums():
    """
    Test the ceil_nums function with different inputs.
    """
    assert ceil_nums(10.5, 100.9) == (11, 101), "Should be (11, 101)"
    assert ceil_nums(1.1, 1.9) == (2, 2), "Should be (2, 2)"
    assert ceil_nums(2.9, 2.1) == (3, 3), "Should be (3, 3)"
    assert ceil_nums(10.1, 10.5) == (11, 11), "Should be (11, 11)"

