#!usr/bin/python3

import sqlite3
import tasca

#para comenzar a guardar en la base de datos

class Persistencia_tasca_sqlite():
    def __init__(self, ruta):
        self._ruta = ruta
        if not self.existeixen_taules():
            self.reset_database()
        

    def desa(self, tasca):  # GUARDAR UN REGISTRO
        self._conn = sqlite3.connect(self._ruta)
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
        self._conn.close()
        return resultat
    
    def get_list(self):
        self._conn = sqlite3.connect(self._ruta)
        consulta = "SELECT titol, done, rowid FROM tasques;"
        cursor = self._conn.cursor()
        cursor.execute(consulta)
        llista = cursor.fetchall()
        resultat = []
        for registre in llista:
            tarea = tasca.Tasca(self, registre[0], registre[1], registre[2])
            resultat.append(tarea)
        cursor.close()
        self._conn.close()
        return resultat
    
    def modifica_tasca(self, tasca):
        resultat = None
        self._conn = sqlite3.connect(self._ruta)
        titol = tasca.titol
        done  = tasca.done
        id = tasca.id
        consulta = f"update tasques set done={done}, titol='{titol}' where rowid={id};"
        cursor = self._conn.cursor()
        try:
            cursor.execute(consulta)
            resultat = tasca
        except sqlite3.IntegrityError:
            print("[X] IntegrityError: Aquest titol ja existeix.")
        self._conn.commit()
        cursor.close()
        self._conn.close()
        return resultat
    
    def esborra_tasca(self, id):
        self._conn = sqlite3.connect(self._ruta)
        consulta = f"delete from tasques where rowid= {id};"
        cursor = self._conn.cursor()
        cursor.execute(consulta)
        self._conn.commit()
        cursor.close()
        self._conn.close()


    def existeixen_taules(self):
        self._conn = sqlite3.connect(self._ruta)
        consulta = "SELECT * FROM tasques LIMIT 1;"
        cursor = self._conn.cursor()
        try:
            cursor.execute(consulta)
        except sqlite3.OperationalError:
            cursor.close()
            self._conn.close()
            return False
        cursor.close()
        self._conn.close()
        return True
    
    def reset_database(self):
        self._conn = sqlite3.connect(self._ruta)
        cursor = self._conn.cursor()  # cursor, necesario para añadir, etc...
        consulta = "DROP TABLE if exists tasques;"
        cursor = cursor.execute(consulta)
        consulta = "CREATE TABLE if not exists tasques(titol TEXT UNIQUE, done BOOLEAN);"
        cursor = cursor.execute(consulta)
        self._conn.commit()  #commit guarda los cambios en base datos
        cursor.close()
        self._conn.close()
      

           
    


def main():
    id = None
    titol = "Fer la bugada"
    persistencia = Persistencia_tasca_sqlite("deleteme.bd")
    una_tasca = tasca.Tasca(persistencia, titol)
    print(persistencia.desa(una_tasca))
    tasques = persistencia.get_list()
    print("-----Llista de tasques----")
    for taska in tasques:
        print(taska)
        if taska.titol == titol:
            id = taska.id
            taska.titol = "Refer la bugada"
            taska.done = True
            persistencia.modifica_tasca(taska)
            print("-------Taska modificada----")
    tasques = persistencia.get_list()
    print("\n\n--- Llista de tasques: ---")
    for taska in tasques:
        print(taska)
    if id:
        persistencia.esborra_tasca(id)
        print("---Taska esborrada---")



if __name__=="__main__":
    main()
