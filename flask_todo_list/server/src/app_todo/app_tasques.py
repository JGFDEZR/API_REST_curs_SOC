#!usr/bin/python3 #------cabecera-----#

import tasca
import persistencia_tasca_sqlite

RUTA_BD = "todo_list.db"

class App_tasques():
    def __init__(self):
        self._persistencia_tasques = persistencia_tasca_sqlite.Persistencia_tasca_sqlite(RUTA_BD)

    def afegeix_tasca(self, tasca_nova):
        tasca_nova.persistencia = self._persistencia_tasques
        tasca_nova.desa() # se guarda ella sola

    def llegir_tasques(self):
        return self._persistencia_tasques.get_list()  # devuelve la lista de tascas.
    
    def modifica_tasca(self, tasca):
        return self._persistencia_tasques.modifica_tasca(tasca)
    
    def esborra_tasca(self, id):
        return self._persistencia_tasques.esborra_tasca(id)