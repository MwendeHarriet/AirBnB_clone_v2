#!/usr/bin/python3
"""This script starts flask application"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    """Function returns hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function returns hello hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_time(text):
    """Function returns hello hbnb"""
    x = text.replace('_', ' ')
    st = "C " + x
    return st


@app.route('/python', defaults={'text': "is_cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_time(text):
    """Function returns hello hbnb"""
    x = text.replace('_', ' ')
    st = "Python " + x
    return st


@app.route('/number/<int:Number>', strict_slashes=False)
def N_time(Number):
    """Function returns hello hbnb"""
    st = str(Number) + " is a number"
    return st


@app.route('/number_template/<int:Number>', strict_slashes=False)
def N_r_time(Number):
    """Function returns hello hbnb"""
    return render_template('5-number.html', num=Number)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
