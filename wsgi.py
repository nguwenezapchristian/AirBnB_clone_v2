#!/usr/bin/python3
"""
a file that will serve as the entry point for our application.
This will tell our Gunicorn server how to interact with the application.
"""
from web_flask.0-hello_route import app


if __name__ == "__main__":
    app.run()
