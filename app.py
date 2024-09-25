"""
This module is part of the Flask DevOps app.
It contains the basic Flask application setup.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """This function returns a greeting message for the home route."""
    return "Hello, DevOps World!"

if __name__ == '__main__':
    app.run(debug=True)
