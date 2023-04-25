#!/usr/bin/python3

import flask
import algebra


app = flask.Flask(__name__)

@app.route("/calcula/<n1>/<n2>")
def calcula(n1, n2): 
    valor_n1 = float(n1)
    valor_n2 = float(n2)
    operacio = algebra.Algebra (valor_n1, valor_n2)  
    res = operacio.calcula()
    return flask.jsonify(res)


def main():
    app.run()

if __name__ == '__main__':
    main()