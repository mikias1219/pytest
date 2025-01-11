# Import the necessary classes from FastAPI's testing module
from fastapi.testclient import TestClient

# Import the FastAPI app instance from the 'main' module
from main import app

# Initialize the TestClient with the FastAPI app, which is used for making HTTP requests in tests
client = TestClient(app)


# Test case to verify retrieving an existing item with a valid token
def test_read_item():
    # Make a GET request to the /items/foo endpoint with a valid token in the headers
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Assert that the response JSON body contains the correct item data
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }


# Test case to verify retrieving an item with an invalid token
def test_read_item_bad_token():
    # Make a GET request to the /items/foo endpoint with an invalid token in the headers
    response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
    
    # Assert that the response status code is 400 (Bad Request) since the token is invalid
    assert response.status_code == 400
    
    # Assert that the response JSON body contains an error message about the invalid token
    assert response.json() == {"detail": "Invalid X-Token header"}


# Test case to verify retrieving a non-existent item
def test_read_nonexistent_item():
    # Make a GET request to the /items/baz endpoint with a valid token, but the item 'baz' doesn't exist
    response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
    
    # Assert that the response status code is 404 (Not Found) since the item does not exist
    assert response.status_code == 404
    
    # Assert that the response JSON body contains an error message indicating the item was not found
    assert response.json() == {"detail": "Item not found"}


# Test case to verify creating a new item with a valid token
def test_create_item():
    # Make a POST request to the /items/ endpoint with a valid token and item data in the request body
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    
    # Assert that the response status code is 200 (OK), indicating the item was successfully created
    assert response.status_code == 200
    
    # Assert that the response JSON body contains the data for the created item
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }


# Test case to verify creating an item with an invalid token
def test_create_item_bad_token():
    # Make a POST request to the /items/ endpoint with an invalid token and item data in the request body
    response = client.post(
        "/items/",
        headers={"X-Token": "hailhydra"},
        json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
    )
    
    # Assert that the response status code is 400 (Bad Request) since the token is invalid
    assert response.status_code == 400
    
    # Assert that the response JSON body contains an error message about the invalid token
    assert response.json() == {"detail": "Invalid X-Token header"}


# Test case to verify that trying to create an existing item returns a conflict error
def test_create_existing_item():
    # Make a POST request to the /items/ endpoint with a valid token and data for an already existing item
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={
            "id": "foo",
            "title": "The Foo ID Stealers",
            "description": "There goes my stealer",
        },
    )
    
    # Assert that the response status code is 409 (Conflict), as the item already exists
    assert response.status_code == 409
    
    # Assert that the response JSON body contains an error message about the item already existing
    assert response.json() == {"detail": "Item already exists"}
