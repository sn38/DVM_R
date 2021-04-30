# coding: UTF-8
"""
Script: ProjetBTS/detection
Création: admin, le 02/03/2021
"""


# Imports

import csv
import subprocess
# Fonctions


def dico_csv():
    try:    # essai d'ouverture
        f = open('caracteres3.csv', mode='r')   # ouverture csv en mode read
    except FileNotFoundError:   # si fichier non trouvé
        print("Fichier non trouvé!")    # affichage erreur
        raise   # raise de l'erreur
    else:   # si fichier ouvert
        dictionnaire = build_dico(f)  # construction du dictionnaire
        f.close()   # fermeture fichier
        return dictionnaire  # renvoi dictionnaire


def build_dico(file):
    dialect = csv.Sniffer().sniff(file.readline())  # objet recap infos fichier csv (détermination séparateur sur ligne 0)
    file.seek(0)    # retour ligne 0
    caracteres = list(csv.DictReader(file, dialect=dialect))    # importation données sous forme liste
    resistances = [elt['resistance'] for elt in caracteres]     # liste des valeurs de résistances
    dict_complet = dict(zip(resistances, caracteres))   # création du dictionnaire (association liste résistances à caractères)
    return dict_complet  # renvoi dictionnaire construit


def lire_dico(dico, res):
    try:    # essai lecture dans dictionnaire
        caractere = dico[res]['caractere']
    except LookupError:     # si valeur hors dictionnaire
        print("Erreur de résistance!")  # affichage erreur
        raise  # raise de l'erreur
    else:   # si valeur dans dictionnaire
        print('Caractère correspondant à', res, 'ohm:', caractere)  # affichage caractère correspondant


def lire_dico2(dico, res):  # retourne le caractère correspondant
    try:    # essai lecture dans dictionnaire
        caractere = dico[res]['caractere']
    except LookupError:     # si valeur hors dictionnaire
        print("Erreur de résistance!")  # affichage erreur
        raise  # raise de l'erreur
    else:   # si valeur dans dictionnaire
        return caractere  # affichage caractère correspondant


def synthese_vocale(message):   # fonction de lecture via synthèse vocale
    commande = "espeak-ng -a 200 -v mb-fr1 -s 150 " + "\"" + message + "\"" + " --stdout | aplay"  # préparation de la commande
    print(commande)  # debug: affichage de la commande avant exécution
    resultat_exec = subprocess.run(commande,shell=True)  # exécution de la commande dans shell et récup objet de subprocess
    if resultat_exec.returncode != 0:  # vérif si returncode diff de 0
        print("Erreur dans la lecture")
    else:
        print("Execution reussie")

# Programme principal


def main():
    # ------------------initialisations----------------------------------
    dictionnaire = dico_csv()   # build du dictionnaire
    chaineCaract = ""               # définition chaine caractères vide
    validation = False          # variable si calcul posé est juste
    exo = "1+1"                     # exo de test
    resultat = 1+1

    while not validation:     # Boucle verification entrée juste
        print("Entrer",exo, ": ")       # print pour les tests
        synthese_vocale("Poser:")
        synthese_vocale(exo)

        for i in range(len(exo)):   # Boucle reconnaissance entrée
            val_res = input()           # input de test pour "ecriture"
            caract = lire_dico2(dictionnaire, val_res)      # correspondance avec dico
            synthese_vocale(caract)
            chaineCaract = chaineCaract + caract    # concatenation entrée précédente et actuelle
            print(chaineCaract)     # debug: affichage chaine à chaque input

        if chaineCaract == exo:         # verfification si exo saisi par eleve identique a exo propose
            validation = True       # changement etat pour sortie boucle de saisie
            synthese_vocale(chaineCaract)
            synthese_vocale("calcul posé juste.")
            print("exercice juste")     # debug: affichage exo juste
            chaineCaract = ""       # reset variable chaineCaract

        else:                   # si exo saisi incorrect
            print("exercice faux")  # debug: affichage exo faux
            synthese_vocale(chaineCaract)
            synthese_vocale("calcul posé faux.")
            chaineCaract = ""           # reset variable chaineCaract


if __name__ == '__main__':
    main()
# Fin

# https://www.youtube.com/watch?v=Hu4I3GAAOmA l15


#     for i in dict_complet.items():
#         print(i)
