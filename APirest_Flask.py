#!/usr/bin/python3

import flask

app = flask.Flask(__name__)

@app.route("/hola")
def hola():
    return '{"missatge": "Hola mon!"}'

@app.route("/adeu")
def adeu():
    return '{"missatge": "A10, mundo cruel!"}'

if __name__ == "__main__":
    app.run()