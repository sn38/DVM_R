# coding: UTF-8
"""
Script: pythonProject_TESTexo/testexo
Création: admin, le 09/03/2021
"""


# Imports
import sqlite3  #importation du module sqlite3

# Fonctions


def get_bdd(numero, niv):
    cnx = sqlite3.connect('DVmath_exercice.db')  #acces base de donnée
    cursor = cnx.cursor()
    request_val = "SELECT exercice FROM creat_exo WHERE numero = ? and niveau = ?"  #requete
    data = (numero, niv)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs donnée en tableau
    print(resultat)  #affiche le resultat de la requete
    cnx.commit()
    cursor.close()
    cnx.close()

    print("Acces BDD Réussi !")


# Programme principal


def main():

    num1 = 4
    num2 = 5
    get_bdd(num1, num2)


if __name__ == '__main__':
    main()
    # Fin
