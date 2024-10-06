# test_app.py

import pytest
from app import create_app

@pytest.fixture
def client_instance():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Disable the redefined-outer-name warning for this function
# pylint: disable=redefined-outer-name
def test_some_function(client_instance):
    # Example of a test function using the client_instance
    response = client_instance.get('/some_endpoint')
    assert response.status_code == 200
