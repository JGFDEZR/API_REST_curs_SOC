#!usr/bin/python3

import sqlite3


RUTA_BD = "una_base_dades.bd"  # mayúsculas porque será constante

def esborra_taules(conn): #conn = conexión
    consulta = "DROP table if exists tasques;"
    cursor = conn.cursor()  # cursor, necesario para borrar, etc...
    cursor.execute(consulta)
    conn.commit()  #commit guarda los cambios en base datos
    cursor.close()

def crea_taules(conn): #conn = conexión
    consulta = """CREATE table if not exists tasques(
    title text,
    done boolean
    );"""
    cursor = conn.cursor()  # cursor, necesario para crear, etc...
    cursor.execute(consulta)
    conn.commit()  #commit guarda los cambios en base datos
    cursor.close()
def afegir_tasques(conn, titol, done=False):
    consulta = f"INSERT INTO tasques (title, done) VALUES('{titol}', {done});"
    cursor = conn.cursor()  # cursor, necesario para añadir, etc...
    cursor.execute(consulta)
    conn.commit()  #commit guarda los cambios en base datos
    cursor.close()

def main():
    print("Obrint conexió amb base de dades")
    conn = sqlite3.connect(RUTA_BD) #conexión con la base de datos
    esborra_taules(conn)
    crea_taules(conn)
    afegir_tasques(conn, "Ir a comprar el pan")
    conn.close()  #conexión cerrada
    print("Conexió tancada.")

if __name__ == "__main__":
    main()