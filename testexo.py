# coding: UTF-8
"""
Script: pythonProject_TESTexo/testexo
Création: admin, le 09/03/2021
"""


# Imports
import sqlite3  #importation du module sqlite3

# Fonctions
def affiche_eleves_bdd(niv): #passe en parametres le numero et le niveau
    cnx = sqlite3.connect('DVmath_exercice.db')  #acces base de donnée
    cursor = cnx.cursor()
    request_val = "SELECT niveau FROM eleve WHERE nom=? AND prenom=?"  #requete
    data = (niv)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs donnée en tableau
    cursor.close()
    cnx.close()


def affiche_calcul_bdd(numero, niv): #passe en parametres le numero et le niveau
    cnx = sqlite3.connect('DVmath_exercice.db')  #acces base de donnée
    cursor = cnx.cursor()
    request_val = "SELECT exercice FROM exercices WHERE numero = ? and niveau = ?"  #requete
    data = (numero, niv)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs donnée en tableau
    cursor.close()
    cnx.close()

    calcul_bdd = ''.join(resultat[0]) #conversion de la valeur à l'indice 0 du tuple en chaîne de caractères
    print("calcul propose:", calcul_bdd) #affiche le resultat de la requete

    return calcul_bdd #renvoie le calcul

    #return resultat


def affiche_resultat_bdd(numero):
    cnx = sqlite3.connect('DVmath_exercice.db')  #acces base de donnée
    cursor = cnx.cursor()
    request_val = "SELECT resultat FROM exercices WHERE numero = ?"  #requete
    data = (numero)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs donnée en tableau
    cursor.close()
    cnx.close()

    resultat_bdd = ''.join(resultat[0]) #conversion de la valeur à l'indice 0 du tuple en chaîne de caractères
    #print("Resultat du calcul:", resultat_bdd) #affiche le resultat de la requete

    return resultat_bdd #renvoie le calcul


def verifier_eleve(nom, prenom, niveau): #Verification que l'élève existe
    cnx = sqlite3.connect('DVmath_exercice.db')  # acces base de donnée
    cursor = cnx.cursor()
    cursor.execute("SELECT count(*) FROM eleves WHERE nom = ? and prenom = ? and niveau = ?", (nom, prenom, niveau,))
    r = cursor.fetchone()[0] #selectionne la premiere ligne des enregistrements
    if r==1:
        print("eleve existant")
        existant = 1
    else:
        print("eleve inconnu")
        existant = 0
    cursor.close()
    cnx.close()

    return existant #renvoie l'existance de l'élève dans la base de données


def travaux_eleve(nom, niveau, calcul, calcul_p, resultat, resultat_p): #Par Evan Lacombe
    # permet d'ouvrir la bdd
    cnx = sqlite3.connect('DVmath_exercice.db')
    cursor = cnx.cursor()
    # insertion des données
    request_val = "INSERT INTO travaux_eleves (nom, niveau, calcul, calcul_pose, resultat, resultat_pose) VALUES (?,?,?,?,?,?)"
    data = (nom, niveau, calcul, calcul_p, resultat, resultat_p)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  # afficher plusieurs donnée en tableau

    #curseur.execute("SELECT * FROM bilan")
    #for resultat in curseur:
        #print(resultat)

    cnx.commit()
    cursor.close()
    cnx.close()

    print("Acquis enregistrés")
    return resultat

def enter_you_name(result_niv):
    nom = "Larue"
    prenom = "Dylan"
    niveau = 4  #le niveau de l'élève

    if niveau == result_niv :
        print("Elève :", nom, prenom, niveau, "ème")
    else:
        print("Erreur")
    verifier_eleve(nom, prenom, niveau)

    return result_niv  #renvoie le niveau entrer par l'élève (niveau)


def choisir_exo():
    print("Quel exercice souhaitez vous réaliser ? > ")
    num_exo = 2
    if num_exo in range(1, 999):
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

    niveau = enter_you_name(4)#récupere le niveau entrer par l'élève
    nom = enter_you_name("Larue")
    print("-----------------------------------------------")

    numero_exo = choisir_exo()  #récupere le numero exercice entrer par l'élève
    print("-----------------------------------------------")

    calcul_propose = affiche_calcul_bdd(numero_exo, niveau)   #affiche un exercice choisi en fonction du niveau et du numero d'exercice
    print("-----------------------------------------------")

    calcul_pose = pose_calcul(calcul_propose) #demande le calcul a recopier et verifie si il a correctement été poser
    print("-----------------------------------------------")

    resultat_calcul = affiche_resultat_bdd(str(numero_exo))
    resultat_pose = pose_resultat(resultat_calcul)

    print("-----------------------------------------------")
    travaux_eleve(nom, niveau,calcul_propose, calcul_pose, resultat_calcul, resultat_pose)

if __name__ == '__main__':
    main()
    # Fin
