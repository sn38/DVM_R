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


def get_bdd_list_exo(niv):
    cnx = sqlite3.connect('DVmath_exercice.db')  #acces base de donnée
    cursor = cnx.cursor()
    request_val = "SELECT exercice FROM creat_exo WHERE niveau = ?"  #requete
    data = (niv)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs donnée en tableau
    print(resultat)  #affiche le resultat de la requete
    cnx.commit()
    cursor.close()
    cnx.close()

    print("Acces BDD Réussi !")


def enter_you_name():
    answer = input("Nom ? > ")
    answer1 = input("Prénom ? > ")
    answer2 = input("Niveau ? > ")
    result = answer2
    if answer2 == "6" or "5" or "4" or "3":
        print("Elève :", answer, answer1, result, "ème")

    return result  #renvoie le niveau entrer par l'élève


# Programme principal

def main():

    niveau = enter_you_name()  #récupere le niveau entrer par l'élève
    num1 = 1  #le numero de l'exercice
    print("-----------------------------------------------")
    get_bdd(num1, niveau)  #execution de la fonction qui va afficher un exercice choisi en fonction du niveau
    print("-----------------------------------------------")
    get_bdd_list_exo(niveau)  #execution de la fonction qui va afficher l'integralité des exercice concerné par le niveau


if __name__ == '__main__':
    main()
    # Fin
