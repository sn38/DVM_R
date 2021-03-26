# coding: UTF-8
"""
Script: DVM_R/test_tuple_str
Création: admin, le 26/03/2021
"""


# Imports
import sqlite3
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
    return resultat

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
    liste_exo = get_bdd_list_exo("5")
    str = ''.join(liste_exo[0])
    print(str)
    commande = "espeak-ng -a 200 -v mb-fr1 -s 150 " + "\"" + str + "\"" + " --stdout | aplay"
    print(commande)
    code_retour = subprocess.run(commande, shell=True)
    print(code_retour)


if __name__ == '__main__':
    main()
# Fin
