#/usr/bin/python3

"""
    api_edat_gos.py: api que calcula l'equivalencia d'etat del gossos amb els humans.
    
    El resultat tindrà la forma:
    {"edat del gos": 4, "equivalencia humana": 29}
"""

import flask

app = flask.Flask(__name__)

@app.route("/equivalencia/<edat_gos>", methods=['GET']) # RUTA Y METODO
def calcula_equivalencia(edat_gos):
    valor_edat_gos = float(edat_gos)
    if valor_edat_gos <= 2:
        resultat = valor_edat_gos * 10.5
    else:
        resultat = 21 + 4 * (valor_edat_gos - 2)
    return flask.jsonify({"edat del gos": valor_edat_gos, "equivalencia humana": resultat})


if __name__ == "__main__":
    app.run()