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
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def nick(self):
        return self._nick
    
    @id.setter
    def nick(self, valor):
        self._nick = valor

    @property
    def password(self):
        return self._password
    
    @id.setter
    def password(self, valor):
        self._password = valor


    def __init__(self, id, nombre, nick, password):
        
        self._id = id
        self._nombre = nombre
        self._nick = nick
        self._password = password

    def desa(self):

        pass

    def get_usuari_by_nick(self, nick):

        pass

    def get_usuari_by_api_key(self, key):

        pass

    def autentica(self, usuari, password):

        pass

    def __str__(self):
        resultat = {'id': self._id, 'nombre': self._nombre, 'nick': self._nick, 'password': self._password}
        return json.dumps(resultat)