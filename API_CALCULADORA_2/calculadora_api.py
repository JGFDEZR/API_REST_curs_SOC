#!/usr/bin/python3

import flask
import json

app = flask.Flask(__name__)#libreria flask   Flask=Clase flask

@app.route("/suma/<n1>/<n2>") #crea la ruta
def suma(n1, n2):
    valor_n1 = float(n1)
    valor_n2 = float(n2)
    res = {"resultat": valor_n1 + valor_n2 } #res=resultado --convertir a json
    return flask.jsonify(res) #función flask-json

@app.route("/resta")
def resta():
    body_text = flask.request.data  #recoger datos del body
    body_dict = json.loads(body_text) #convertir json a tipo variable(diccionario)
    valor_n1 = body_dict["n1"]
    valor_n2 = body_dict["n2"]
    res = {"resultat": valor_n1 - valor_n2}
    return flask.jsonify(res)


def main():
    app.run()  #orden para la ruta



if __name__ == "__main__":
    main()