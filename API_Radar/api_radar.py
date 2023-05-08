#!usr/bin/python3

import json
import flask



app = flask.Flask(__name__)

@app.route("/radar/<vel_coche>/<vel_permitida>", methods=['GET'])
def calcula_velocidad(vel_coche, vel_permitida):
    valor_vel_coche = float(vel_coche)
    valor_vel_permitida = float(vel_permitida)
    
    if valor_vel_coche <= valor_vel_permitida:
        resultat = "correcto"
    elif valor_vel_coche <= valor_vel_permitida + (valor_vel_permitida * 0.1):
        resultat = "Marge de seguretat"
    else:
        resultat = "Multa!"

    return flask.jsonify({"resultat": resultat})





def main():
    app.run()

if __name__ == "__main__":
    main()

