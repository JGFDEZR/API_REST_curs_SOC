#!usr/bin/python3 #------cabecera-----#

import app_tasques
import tasca

def main():
    t = None
    la_app = app_tasques.App_tasques()

    la_app.afegeix_tasca(tasca.Tasca(None, "Escombrar las escales")) # creamos nueva tasca
    la_app.afegeix_tasca(tasca.Tasca(None, "Portar el cotxe a la ITV"))

    for t in la_app.llegir_tasques(): # bucle para leer las tascas que hemos hecho
        print(t)

    if t:
        t.done = True
        la_app.modifica_tasca(t)
        print("Tasca modificada")

    if t:
        la_app.esborra_tasca(t.id)
        print("Tasca esborrada")

if __name__ == "__main__":
    main()

