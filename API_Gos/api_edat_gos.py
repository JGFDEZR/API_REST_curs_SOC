#!/usr/bin/python3

"""
    api_edat_gos.py: api que calcula l'equivalencia d'etat del gossos amb els humans.
    
    El resultat tindrà la forma:
    {"edat del gos": 4, "equivalencia humana": 29}
"""

import json
import flask
import gos

app = flask.Flask(__name__)

@app.route("/equivalencia", methods=['GET']) # RUTA Y METODO
def calcula_equivalencia():
    body_text = flask.request.get_data()#bytes del body
    body_dict = json.loads(body_text)
    edat_gos = body_dict["edat"]
    un_gos = gos.Gos(float(edat_gos))
    un_gos.calcula_equivalencia()
    dict_gos = json.loads(str(un_gos))
    return flask.jsonify(dict_gos)

def main():
    app.run()


if __name__ == "__main__":
    main()