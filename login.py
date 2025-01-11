import re

# Simple in-memory user storage for demonstration
users_db = {}

def is_valid_email(email):
    """
    Validate email format.
    """
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None

def is_valid_password(password):
    """
    Validate password (minimum 8 characters for demo purposes).
    """
    return len(password) >= 8

def signup(email, password):
    """
    Simulate a signup function.
    """
    if not is_valid_email(email):
        raise ValueError("Invalid email format")
    if not is_valid_password(password):
        raise ValueError("Password must be at least 8 characters long")
    
    # Save the user data (email and password)
    users_db[email] = password

def login(email, password):
    """
    Simulate a login function.
    """
    if email not in users_db:
        raise ValueError("User not found")
    if users_db[email] != password:
        raise ValueError("Incorrect password")
    return True
