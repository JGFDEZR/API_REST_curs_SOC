#!usr/bin/python3

import json

class Tasca():
    """
     Tasca.py conté la clase Tasca que és la clase principal de la  nostra api
    """

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, valor):
        self._id = valor

    @property                 #persistencia para conectar con la base de datos
    def persistencia(self):
        return self._persistencia
    
    @persistencia.setter
    def persistencia(self, valor):
        self._persistencia = valor

    @property
    def titol(self):
        return self._titol
    
    @titol.setter
    def titol(self, valor):
        self._titol = valor

    @property
    def done(self):
        return self._done       

    @done.setter
    def done(self, valor):
        self._done = valor

    def __init__(self, persistencia, titol, done=False, id=None):
        # assert issubclass(type(persistencia), src.app_todo.persistencia_tasca.Persistencia_tasca) 
        
        
        """
          la funció strip() treu els espais sobrants 
          del darrera i del començament d'una cadena de text.
        """
        self._persistencia = persistencia
        self._titol = str(titol).strip()
        self._done = done
        self._id = id

    def desa(self):
        resultat = self._persistencia.desa(self)
        if resultat:
            self.id = resultat.id
        return resultat


    def __str__(self):
        resultat = {'id': self._id, 'titol': self._titol, 'done': self._done}
        return json.dumps(resultat)