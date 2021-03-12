# coding: UTF-8
"""
Script: pythonProject_TESTexo/testexo
Création: admin, le 09/03/2021
"""


# Imports
import sqlite3  #importation du module sqlite3

# Fonctions 
def set_bdd(exo, result, niv):
    cnx = sqlite3.connect('DVmath_exercice.db') #
    cursor = cnx.cursor()
    request_val = "SELECT numero, niveau FROM creat_exo WHERE" #3 variable
    #data = (exo, result, niv)
    cursor.execute(request_val, data)
    cnx.commit()
    cursor.close()
    cnx.close()


# Programme principal
def main():
    pass

if __name__ == '__main__':
    main()
    # Fin
