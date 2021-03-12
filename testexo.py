# coding: UTF-8
"""
Script: pythonProject_TESTexo/testexo
Création: admin, le 09/03/2021
"""


# Imports
import sqlite3  #importation du module sqlite3

# Fonctions 
def get_bdd(numero, niv):
    cnx = sqlite3.connect('DVmath_exercice.db') #acces base de donnée
    cursor = cnx.cursor()

    identifiant = numero
    niveau = niv

    request_val = "SELECT exercice FROM creat_exo WHERE numero = ? and niveau = ?", identifiant, niveau  #avec variables
    #data = (exo, result, niv)
    request_val = str(request_val)
    cursor.execute(request_val)
    resultat = cursor.fetchall()  #afficher plusieurs donnée en tableau
    cnx.commit()
    cursor.close()
    cnx.close()


    print("Acces BDD Réussi !")
    print(resultat)

# Programme principal
def main():

    num1 = input()
    num2 = input()
    get_bdd(num1, num2)




if __name__ == '__main__':
    main()
    # Fin
