#!/usr/bin/python3
"""
a file that will serve as the entry point for our application.
This will tell our Gunicorn server how to interact with the application.
"""
from web_flask.0-hello_route import app as hello_app
from web_flask.6-number_odd_or_even import app as number_app


if __name__ == "__main__":
    hello_app.run(port=5000)
    number_app.run(port=5001)
