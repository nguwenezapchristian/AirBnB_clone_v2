#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask, abort, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    text_underscore_removed = text.replace('_', ' ')
    return f"C {escape(text_underscore_removed)}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_Python(text):
    text_underscore_removed = text.replace('_', ' ')
    return f"Python {escape(text_underscore_removed)}"


@app.route('/number/<n>', strict_slashes=False)
def display_num(n):
    if n.isdigit():
        return f"{n} is a number"
    else:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def display_HTML(n):
    if n.isdigit():
        return render_template('5-number.html', n=n)
    else:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def display_odd_even(n):
    if n.isdigit():
        if int(n) % 2 == 0:
            odd_even = "even"
        else:
            odd_even = "odd"
        return render_template(
                '6-number_odd_or_even.html',
                n=n, odd_or_even=odd_even
                )
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
