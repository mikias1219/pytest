# Function Definitions
def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    """
    return a + b

def devide_numbers(a, b):
    """
    Divide two numbers and returns the result.
    Raises a ValueError if dividing by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def multiply_numbers(a, b):
    """
    Multiply two numbers and returns the result.
    """
    return a * b
def subtract_numbers(a, b):
    """
    Subtract two numbers and returns the result.
    """
    return a - b