#!/usr/bin/python3

import json

class Algebra():
    def __init__(self, v1 = 0, v2 = 0):
        self._valor_1 = v1
        self._valor_2 = v2

    @property
    def valor_1(self):
        return self._valor_1
    
    @valor_1.setter
    def valor_1(self, valor):
        self._valor_1 = valor

    @property
    def valor_2(self):
        return self._valor_2
    
    @valor_2.setter
    def valor_2(self, valor):
        self._valor_2 = valor

    def calcula(self):
        preu_base = self._valor_1
        iva = self._valor_1 * self._valor_2 /100
        preu_total = preu_base + iva
        resultat = {
            "preu_base": preu_base,
            "iva": iva,
            "preu_total": preu_total
        }
        return resultat

        
        
    



    def __str__(self):
        resultat = {"resultat =": self.opera}
        return json.dumps(resultat)
