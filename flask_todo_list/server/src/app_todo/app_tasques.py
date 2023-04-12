#!usr/bin/python3 #------cabecera-----#

import tasca

class App_tasques():
    def __init__(self):
        self._llista = [] # creamos lista vacía para guardar.

    def afegeix_tasca(self, tasca_nova):
        self._llista.append(tasca_nova)  #append introduce en la lista, tasca_nova.

    def llegir_tasques(self):
        return self._llista  # devuelve la lista de tascas.