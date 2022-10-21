#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    "Return a message on client"
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    'displays HBNB'
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    'displays C followed by params text'
    return 'C {0}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    'displays Python followed by the value of the text'
    return 'Python {0}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n: int):
    'display “n is a number” only if n is an integer'
    return '{0} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n: int):
    'display a HTML page only if n is an integer:'
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numberOddOrEven(n: int):
    'display a HTML page only if n is an integer:'
    p = n % 2 == 0
    p = 'even' if p else 'odd'
    return render_template('6-number_odd_or_even.html', number=n, parity=p)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
