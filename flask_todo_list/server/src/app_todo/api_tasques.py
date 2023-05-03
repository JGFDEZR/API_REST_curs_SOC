#!usr/bin/python3     #-----cabecera-----#

import flask
import app_tasques
import tasca
import json
import usuari

app = flask.Flask(__name__)
core_app = app_tasques.App_tasques()

@app.route("/tasks<id>", methods = ["DELETE"])
def delete_task(id):
    resultat = core_app.esborra_tasca(id)
    return "", 204

@app.route("/tasks", methods = ["POST", "GET", "PUT"])
def tasks():
    if flask.request.method == "POST":
        usuari_autoritzat = get_usuari_from_api_key()
        if not usuari_autoritzat:
            return "", 403
        info_body = flask.request.get_data()  #info_body = '{"title": "hola"}'  -> str
        tasca_nova = json.loads(info_body)    #tasca_nova = {"title": "hola"}  -> dictionary
        objecte_tasca = tasca.Tasca(None, tasca_nova["title"])  # Object_Tasca -> tasca.Tasca
        objecte_tasca.propietari = usuari_autoritzat
        resultat = core_app.afegeix_tasca(objecte_tasca)
        return "", 201
    elif flask.request.method == "PUT":
        info_body = flask.request.get_data()  #info_body = '{"title": "hola"}'  -> str
        tasca_nova = json.loads(info_body)    #tasca_nova = {"title": "hola"}  -> dictionary
        objecte_tasca = tasca.Tasca(
            None, tasca_nova["title"], 
            tasca_nova["done"], 
            tasca_nova["id"])  # Object_Tasca -> tasca.Tasca
        resultat = core_app.modifica_tasca(objecte_tasca)
        return "", 204
    elif flask.request.method == "GET":
        usuari_autoritzat = get_usuari_from_api_key()
        if not usuari_autoritzat:
            return "", 403
        llista_jsons = []
        llista_tasques = core_app.llegir_tasques(usuari_autoritzat)
        for t in llista_tasques:
            tasca_json = str(t)                         #tasca_json -> str
            tasca_diccionary = json.loads(tasca_json)   #tasca diccionary -> diccionary
            llista_jsons.append(tasca_diccionary)       #array de diccionaries
        return flask.jsonify(llista_jsons), 200         #retorna json + Content-type: aplication/json

@app.route('/registre', methods =['POST']) # ruta nueva para el registro
def registre():
    info_body = flask.request.get_data()  #info_body = '{"title": "hola"}'  -> str
    usuari_nou = json.loads(info_body)    #tasca_nova = {"title": "hola"}  -> dictionary
    objecte_usuari = usuari.Usuari(
        None, usuari_nou["nom"], 
        usuari_nou["nick"], 
        usuari_nou["password"]
        )  # Object_usuari -> usuari.Usuari
    resultat = core_app.registre(objecte_usuari)
    if resultat:
        return "", 201
    return "", 400

@app.route('/login', methods=['POST'])
def login():
    info_body = flask.request.get_data()  #info_body = '{"title": "hola"}'  -> str
    usuari_nou = json.loads(info_body)    #tasca_nova = {"title": "hola"}  -> dictionary
    objecte_usuari = usuari.Usuari(
        None, None, 
        usuari_nou["nick"], 
        usuari_nou["password"]
        )  # Object_usuari -> usuari.Usuari
    resultat = core_app.login(objecte_usuari.nick, objecte_usuari.password)
    if resultat:
        return flask.jsonify({"api_key": resultat}), 201
    return "", 403

def get_usuari_from_api_key():
    x_api_key = None #api inicializada
    if 'x-api-key' in flask.request.headers: #leemos cabeceras
        x_api_key = flask.request.headers['x-api-key']
    else:
        return None
    usuari_autoritzat = core_app.llegeix_usuari_amb_api_key(x_api_key)
    if not usuari_autoritzat:
        return None
    return usuari_autoritzat

app.run(
    host="0.0.0.0",
    debug=False)