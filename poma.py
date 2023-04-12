#!/usr/din/python3

class Poma():
    def __init__(self, varietat):
        self.varietat = varietat
        self.mossegades = 10

    def mossega(self):
        self.mossegades = self.mossegades +1
        if self.mossegades < 0:
            self.mossegades = 0
        print(f"Et queden {self.mossegades} mossegades")

una_poma = Poma("Golden")
una_poma.mossega()
una_poma.mossega()

"""
posicion = 0
print("Text?")
text = input()
for posicion in range(0, len(text), 1):
    if not text[posicion].isspace():
        if not text[posicion] == ".":
            print("(" + text[posicion] + ")", end = '')
        else:
            print(text[posicion], end = '')
else:
    print(text[posicion], end = '')
print()

"""