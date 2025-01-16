# Function Definitions
import math
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
def power_numbers(a, b):
    """
    Raise a to the power of b and returns the result.
    """
    return a ** b
def get_greeting(name):
    """
    Returns a greeting message for the given name.
    """
    return f"Hello, {name}!"
def log_nums(a,b):
    """
    Returns the log of a and b
    """
    return math.log(a), math.log(b)
def sqrt_nums(a,b):
    """
    Returns the sqrt of a and b
    """ 
    return math.sqrt(a), math.sqrt(b)
def abs_nums(a,b):
    """
    Returns the absolute value of a and b
    """
    return abs(a), abs(b)
def floor_nums(a,b):
    """ 
    Returns the floor of a and b
    """ 
    return math.floor(a), math.floor(b)
def ceil_nums(a,b):
    """
    Returns the ceil of a and b
    """
    return math.ceil(a), math.ceil(b)
def mod_nums(a,b):
    """ 
    Returns the modulus of a and b
    """
    return a % b
def div_nums(a,b):
    """
    Returns the division of a and b
    """
    return a // b
def add_list(a):
    """
    Returns the sum of the list
    """
    return sum(a)
def multiply_list(a):
    """

    Returns the product of the list
    """
    result = 1
    for i in a:
        result = result * i
    return result   
def get_max(a):
    """
    Returns the maximum value of the list
    """
    return max(a)
def get_min(a):
    """
    Returns the minimum value of the list
    """
    return min(a)
def get_mean(a):
    """
    Returns the mean of the list
    """
    return sum(a) / len(a)
def get_median(a):
    """
    Returns the median of the list
    """
    n = len(a)
    a.sort()
    if n % 2 == 0:
        median1 = a[n//2]
        median2 = a[n//2 - 1]
        median = (median1 + median2) / 2
    else:
        median = a[n//2]
    return median
