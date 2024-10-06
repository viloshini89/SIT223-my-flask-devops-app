import pytest
from app import app

@pytest.fixture
def client():
    # Set up the Flask app for testing
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, DevOps World!" in response.data
