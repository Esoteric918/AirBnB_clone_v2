#!/usr/bin/python3
"""FLASK"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnd', strict_slashes=False)
def hbnb_route():
    """HBNB"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')