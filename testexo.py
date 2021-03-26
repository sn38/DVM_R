# coding: UTF-8
"""
Script: pythonProject_TESTexo/testexo
Création: admin, le 09/03/2021
"""


# Imports
import sqlite3  #importation du module sqlite3

# Fonctions


def affiche_calcul_bdd(numero, niv):
    cnx = sqlite3.connect('DVmath_exercice.db')  #acces base de donnée
    cursor = cnx.cursor()
    request_val = "SELECT exercice FROM creat_exo WHERE numero = ? and niveau = ?"  #requete
    data = (numero, niv)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs donnée en tableau
    cnx.commit()
    cursor.close()
    cnx.close()

    calcul_bdd = ''.join(resultat[0]) #conversion de la valeur à l'indice 0 du tuple en chaîne de caractères
    print("calcul propose:", calcul_bdd) #affiche le resultat de la requete

    return calcul_bdd #renvoie le calcule

def affiche_resultat_bdd(numero):
    cnx = sqlite3.connect('DVmath_exercice.db')  #acces base de donnée
    cursor = cnx.cursor()
    request_val = "SELECT resultat FROM creat_exo WHERE numero = ?"  #requete
    data = (numero)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs donnée en tableau
    cnx.commit()
    cursor.close()
    cnx.close()

    resultat_bdd = ''.join(resultat[0]) #conversion de la valeur à l'indice 0 du tuple en chaîne de caractères
    #print("Resultat du calcul:", resultat_bdd) #affiche le resultat de la requete

    return resultat_bdd #renvoie le calcul

def enter_you_name():
    answer = "Dupond"
    answer1 = "Pierre"
    answer2 = 4
    result_niv = answer2
    if answer2 == "6" or "5" or "4" or "3":
        print("Elève :", answer, answer1, result_niv, "ème")

    return result_niv  #renvoie le niveau entrer par l'élève (niveau)


def choisir_exo():

    print("Quel exercice souhaitez vous réaliser ? > ")
    num_exo = 2
    if num_exo in range(999):
        print("Vous avez choisi l'exercice", num_exo) #va affciher le numéro de l'exercice definis
    else:
        print("Erreur")

    return num_exo  #renvoie le numero d'exercice entrer par l'élève (numero_exo)


def pose_calcul(calcul_p):
    calcul_pose = input("Poser le calcul > ") #present pour le test !!
    #calcul_pose = "32-14"
    if calcul_pose == calcul_p:
        print("Vous avez correctement ecrit le calcul : ", calcul_pose)
    else:
        print("Erreur")

    return calcul_pose

def pose_resultat(resultat_p):
    resultat_pose = input("Poser le resultat >")
    if resultat_pose == resultat_p:
        print("Vous avez correctement posé le resultat : ", resultat_pose)
    else:
        print("Erreur")

    return resultat_pose


# Programme principal
def main():

    niveau = enter_you_name()  #récupere le niveau entrer par l'élève
    print("-----------------------------------------------")

    numero_exo = choisir_exo()  #récupere le numero exercice entrer par l'élève
    print("-----------------------------------------------")

    calcul_propose = affiche_calcul_bdd(numero_exo, niveau)   #affiche un exercice choisi en fonction du niveau et du numero d'exercice
    print("-----------------------------------------------")

    pose_calcul(calcul_propose) #demande le calcul a recopier et verifie si il a correctement été poser
    print("-----------------------------------------------")

    resultat_calcul = affiche_resultat_bdd(str(numero_exo))
    pose_resultat(resultat_calcul)


if __name__ == '__main__':
    main()
    # Fin
