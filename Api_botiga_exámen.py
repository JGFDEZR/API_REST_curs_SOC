#!usr/bin/python3

"""
    Ens han encarregat crear una API REST que calculi el canvi que hem de donar com a caixers a una botiga quan ens paguen.
Hem de generar una única ruta i enviar-li dos paràmetres:

    El total del ticket.
    La quantitat que ens ha donat el client per realitzar el pagament.

La aplicació ha de retornar un JSON amb tres camps:

    total: Repeteix el total del ticket que ha enviat el client.
    pagat: Repeteix la quantitat que ha lliurat el client.
    canvi: Calcula el canvi a tornar: Pagat - Total

Nota tècnica: No tenir en compte cèntims d'Euro, treballar amb int no amb float.
Exemple de JSON retornat:
{"total": 35, "pagat": 40, "canvi": 5}
"""

import flask
import json

app = flask.Flask(__name__)

@app.route("/botiga/<total>/<pagat>", methods=['GET'])
def calcula_compta(total, pagat):
    total = int(total)
    pagat = int(pagat)
    canvi = total - pagat
    mensaje = None
    if total > pagat:
        mensaje = "Te falta dinero."
    elif total < pagat:
        mensaje = "Tu cambio."
    else:
        mensaje = "En paz."
           
    return flask.jsonify({
        "total": total, 
        "pagat": pagat, 
        "canvi": canvi,
        "resultat": mensaje})

def main():
    app.run()

if __name__ == "__main__":
    main()