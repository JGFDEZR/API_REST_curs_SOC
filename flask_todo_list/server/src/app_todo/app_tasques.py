#!usr/bin/python3 #------cabecera-----#

import tasca
import persistencia_tasca_sqlite
import persistencia_tasca_mysql
import json

RUTA_BD = "todo_list.db"

class App_tasques():
    def __init__(self):
        config = self.llegeix_configuracio()
        try:
            self._database = config["database"]
        except:
            self._database = None
        print(f"Base de dades: {self._database}")
        if self._database == "sqlite":
            self._persistencia_tasques = persistencia_tasca_sqlite.Persistencia_tasca_sqlite(RUTA_BD)
        elif self._database == "mysql":
            self._persistencia_tasques = persistencia_tasca_mysql.Persistencia_tasca_mysql()
        else:
            raise Exception("Base de dades no encontrada!")
        
    def llegeix_configuracio(self): #configurar un json para la ruta
        ruta_config = "./config.json"
        resultat = {}
        try:
            with open(ruta_config) as f: #open= abre la ruta(fitxer)
                resultat = json.load(f)
        except BaseException as ex:
            print("No he trobat el fitxer de configuracio")
        return resultat

    def afegeix_tasca(self, tasca_nova):
        tasca_nova.persistencia = self._persistencia_tasques
        tasca_nova.desa() # se guarda ella sola

    def llegir_tasques(self):
        return self._persistencia_tasques.get_list()  # devuelve la lista de tascas.
    
    def modifica_tasca(self, tasca):
        return self._persistencia_tasques.modifica_tasca(tasca)
    
    def esborra_tasca(self, id):
        return self._persistencia_tasques.esborra_tasca(id)