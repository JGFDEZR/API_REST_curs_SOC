#!usr/bin/python3

import sqlite3


RUTA_BD = "una_base_dades.bd"  # mayúsculas porque será constante

def main():
    print("Obrint conexió amb base de dades")
    conn = sqlite3.connect(RUTA_BD) #conexión con la base de datos

    conn.close()  #conexión cerrada
    print("Conexió tancada.")

if __name__ == "__main__":
    main()