#!/usr/bin/python3
"""This module starts a web flask application"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    """Function returns hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function returns hello hbnb"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
