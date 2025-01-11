import pytest
from login import signup, login, users_db  # Replace `your_module` with your actual module name

# Test the signup function with valid and invalid email/password
def test_signup_valid():
    """
    Test signup with valid email and password.
    """
    email = "test@example.com"
    password = "validPassword123"
    
    signup(email, password)
    
    # Check if the user is successfully added to the users_db
    assert email in users_db
    assert users_db[email] == password

def test_signup_invalid_email():
    """
    Test signup with invalid email format.
    """
    with pytest.raises(ValueError, match="Invalid email format"):
        signup("invalid-email", "validPassword123")

def test_signup_short_password():
    """
    Test signup with a short password.
    """
    with pytest.raises(ValueError, match="Password must be at least 8 characters long"):
        signup("test@example.com", "short")

# Test the login function with valid and invalid credentials
def test_login_valid():
    """
    Test login with correct credentials.
    """
    email = "test@example.com"
    password = "validPassword123"
    
    signup(email, password)  # First signup the user
    result = login(email, password)  # Then attempt to login
    
    assert result == True  # Login should be successful

def test_login_invalid_email():
    """
    Test login with a non-existing email.
    """
    with pytest.raises(ValueError, match="User not found"):
        login("nonexistent@example.com", "somePassword")

def test_login_invalid_password():
    """
    Test login with an incorrect password.
    """
    email = "test@example.com"
    password = "validPassword123"
    wrong_password = "incorrectPassword"
    
    signup(email, password)  # First signup the user
    with pytest.raises(ValueError, match="Incorrect password"):
        login(email, wrong_password)
