#!/usr/bin/python3
"""FLASK"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_only():
    """HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """c_route"""
    return 'C {}' .format(text.replace("_", " "))


@app.route('/python')
@app.route('/python/<text>')
def python_route(text="is cool"):
    """python_route"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int>:n')
def number(n):
    if isinstance(n, int):
        return "{} is a number".format(int(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
