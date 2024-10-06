import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client_instance:
        yield client_instance

def test_home(client):
    """Test the home page route."""
    response = client.get('/')
    assert response.data == b'Hello, DevOps World!'
