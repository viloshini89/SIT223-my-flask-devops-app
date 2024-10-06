"""
This module contains the tests for the Flask application.
"""

import pytest
from app import app

@pytest.fixture
def flask_test_client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(flask_test_client):
    """Test the home page route."""
    response = flask_test_client.get('/')
    assert response.data == b'Hello, DevOps World!'
