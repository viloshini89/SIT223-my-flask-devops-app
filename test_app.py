"""
This module contains the tests for the Flask application.
"""

import pytest
from app import app

@pytest.fixture
def client_instance():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client_instance):
    """Test the home page route."""
    response = client_instance.get('/')
    assert response.data == b'Hello, DevOps World!'
