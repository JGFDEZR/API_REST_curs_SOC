#!usr/bin/python3

import json

class Usuari():

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, valor):
        self._nom = valor

    @property
    def nick(self):
        return self._nick
    
    @id.setter
    def nick(self, valor):
        self._nick = valor

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, valor):
        self._password = valor

    @property                 #persistencia para conectar con la base de datos
    def persistencia(self):
        return self._persistencia
    
    @persistencia.setter
    def persistencia(self, valor):
        self._persistencia = valor


    def __init__(self, persistencia, nom=None, nick=None, password=None, id=None):
        
        self._nom = nom
        self._nick = nick
        self._password = password
        self._id = id
        self._persistencia = persistencia

    def desa(self):

        resultat = self._persistencia.desa(self)
        if resultat:
            self.id = resultat.id
        return resultat

    def get_usuari_by_nick(self, nick):

        pass

    def get_usuari_by_api_key(self, key):

        pass

    def autentica(self, usuari, password):

        pass

    def __str__(self):
        resultat = {'id': self._id, 'nombre': self._nom, 'nick': self._nick, 'password': self._password}
        return json.dumps(resultat)