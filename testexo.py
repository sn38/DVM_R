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


def choisir_exo():

    i = input("Quel exercice souhaitez vous réaliser ? > ")
    if i not in range(999):
        print("Vous avez choisi l'exercice", i)
    else:
        print("Erreur")

    return i  #renvoie l'exercice entrer par l'élève


def pose_calcul(i):
    a = input("Ecrire le calcul > ")
    if a == i:
        print("Vous avez correctement ecrit le calcul : ", a)
    else:
        print("Erreur")

    return a


# Programme principal

def main():

    niveau = enter_you_name()  #récupere le niveau entrer par l'élève
    print("-----------------------------------------------")
    i = choisir_exo() #récupere l'exercice entrer par l'élève
    print("-----------------------------------------------")
    get_bdd(i, niveau)  #execution de la fonction qui va afficher un exercice choisi en fonction du niveau
    print("-----------------------------------------------")
    a = pose_calcul(i)
    #get_bdd_list_exo(niveau)  #execution de la fonction qui va afficher l'integralité des exercice concerné par le niveau


if __name__ == '__main__':
    main()
    # Fin
