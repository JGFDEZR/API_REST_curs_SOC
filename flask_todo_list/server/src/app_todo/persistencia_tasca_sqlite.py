#!usr/bin/python3

import sqlite3
import tasca

#para comenzar a guardar en la base de datos

class Persistencia_tasca_sqlite():
    def __init__(self, ruta):
        self._ruta = ruta
        self._conn = sqlite3.connect(self._ruta)

    def desa(self, tasca):  # GUARDAR UN REGISTRO
        titol = tasca.titol
        done  = tasca.done
        resultat = None

        consulta = "INSERT INTO tasques " \
                    + "(titol, done)" \
                    + f"VALUES('{titol}', {done});"
        
        cursor = self._conn.cursor()  # cursor, necesario para añadir, etc...
        try:      #para q no salga error(IntegrityError) cuando la tasca ya esté hecha
            cursor = cursor.execute(consulta)
            tasca.id = cursor.lastrowid
            resultat = tasca
        except sqlite3.IntegrityError:
            print("[X] IntegrityError: Aquesta tasca ja està registrada.")
        self._conn.commit()  #commit guarda los cambios en base datos
        cursor.close()
        return resultat
    
    def get_list(self):
        consulta = "SELECT titol, done, rowid FROM tasques;"
        cursor = self._conn.cursor()
        cursor.execute(consulta)
        llista = cursor.fetchall()
        resultat = []
        for registre in llista:
            tarea = tasca.Tasca(self, registre[0], registre[1], registre[2])
            resultat.append(tarea)
        return resultat
    


def main():
    persistencia = Persistencia_tasca_sqlite("deleteme.bd")
    una_tasca = tasca.Tasca(persistencia, "Fregar la escalera")
    print(persistencia.desa(una_tasca))
    tasques = persistencia.get_list()
    print("-----Llista de tasques----")
    for taska in tasques:
        print(taska)


if __name__=="__main__":
    main()
