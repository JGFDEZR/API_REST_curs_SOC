#!/usr/bin/python3

import flask

app = flask.Flask(__name__)

@app.route("/")
def main():
    return "hola mon"

app.run()

