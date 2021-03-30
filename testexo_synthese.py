# coding: UTF-8
"""
Script: pythonProject_TESTexo/testexo
Création: admin, le 09/03/2021
"""


# Imports
#from espeakng import ESpeakNG #plus utile
import sqlite3  #importation du module sqlite3
#import os #plus utile
import subprocess


# Fonctions


def get_bdd(numero, niv):
    cnx = sqlite3.connect('DVmath_exercice.db')  #accès base de donnée
    cursor = cnx.cursor()
    request_val = "SELECT exercice FROM creat_exo WHERE numero = ? and niveau = ?"  #requête
    data = (numero, niv)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs données en tableau
    print(resultat)  #affiche le résultat de la requête
    cnx.commit()
    cursor.close()
    cnx.close()
    return (resultat)


def get_bdd_list_exo(niv):
    cnx = sqlite3.connect('DVmath_exercice.db')  #accès base de données
    cursor = cnx.cursor()
    request_val = "SELECT exercice FROM creat_exo WHERE niveau = ?"  #requête
    data = (niv)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs données en tableau
    print(resultat)  #affiche le resultat de la requête
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

    return result  #renvoie le niveau entré par l'élève


# Programme principal

def main():
    #esng = ESpeakNG(voice='fr')


    niveau = enter_you_name()  #récupere le niveau entré par l'élève
    num1 = 1  #le numero de l'exercice
    print("-----------------------------------------------")
    exo = get_bdd(num1, niveau)  #execution de la fonction qui va afficher un exercice choisi en fonction du niveau

    exo = str(exo)
    commande = "espeak-ng -a 200 -v mb-fr1 -s 150 " + "\"" + exo + "\"" + " --stdout | aplay"   #préparation de la commande
    print(commande) #débug, affichage de la commande avant exécution
    resultat_exec= subprocess.run(commande, shell=True) #exécution de la commande dans shell et récup objet de subprocess
    if(resultat_exec.returncode != 0):  #vérif si returncode diff de 0
        print("Erreur dans la lecture")
    else:
        print("Execution reussie")

    #print(resultat_exec.returncode)
    #print(resultat_exec.stderr)

    print("-----------------------------------------------")
    get_bdd_list_exo(niveau)  #execution de la fonction qui va afficher l'integralité des exercices concernés par le niveau


if __name__ == '__main__':
    main()
    # Fin
