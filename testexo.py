# coding: UTF-8
"""
Script: pythonProject_TESTexo/testexo
Création: admin, le 09/03/2021
"""


# Imports
import sqlite3  #importation du module sqlite3

# Fonctions


def affiche_bdd(numero, niv):
    cnx = sqlite3.connect('DVmath_exercice.db')  #acces base de donnée
    cursor = cnx.cursor()
    request_val = "SELECT exercice FROM creat_exo WHERE numero = ? and niveau = ?"  #requete
    data = (numero, niv)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs donnée en tableau
    print(resultat[0])  #affiche le resultat de la requete  tuple [] a voir
    resultat_str = str(resultat)
    cnx.commit()
    cursor.close()
    cnx.close()


def affiche_bdd_list_exo(niv):
    cnx = sqlite3.connect('DVmath_exercice.db')  #acces base de donnée
    cursor = cnx.cursor()
    request_val = "SELECT exercice FROM creat_exo WHERE niveau = ?"  #requete
    data = (niv)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs donnée en tableau
    print(resultat)  #affiche le resultat de la requete #parcourir le curseur
    cnx.commit()
    cursor.close()
    cnx.close()

    print("Acces BDD Réussi !")


def enter_you_name():
    answer = "Dupond"
    answer1 = "Pierre"
    answer2 = 5
    result = answer2
    if answer2 == "6" or "5" or "4" or "3":
        print("Elève :", answer, answer1, result, "ème")

    return result  #renvoie le niveau entrer par l'élève


def choisir_exo():

    print("Quel exercice souhaitez vous réaliser ? > ")
    i = 4
    if i in range(999):
        print("Vous avez choisi l'exercice", i)
    else:
        print("Erreur")

    return i  #renvoie l'exercice entrer par l'élève


def pose_calcul(i):
    #a = input("Ecrire le calcul > ")
    a = 4
    if a == i:
        print("Vous avez correctement ecrit le calcul : ", a)
    else:
        print("Erreur")

    return a

def  pose_resultat():
    resultat = 18
    print("Vous avez entrer le resultat :", resultat)

# Programme principal

def main():

    niveau = enter_you_name()  #récupere le niveau entrer par l'élève
    print("-----------------------------------------------")

    i = choisir_exo()  #récupere l'exercice entrer par l'élève
    print("-----------------------------------------------")

    affiche_bdd(i, niveau)  #execution de la fonction qui va afficher un exercice choisi en fonction du niveau
    print("-----------------------------------------------")

    a = pose_calcul(i)
    print("-----------------------------------------------")

    pose_resultat()

    #affiche_bdd_list_exo(niveau) #execution de la fonction qui va afficher l'integralité des exercice concerné par le niveau


if __name__ == '__main__':
    main()
    # Fin
