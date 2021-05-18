# coding: UTF-8
"""
Script: ProjetBTS/detection
Création: admin, le 02/03/2021
"""


# Imports

import csv
import subprocess
from collections import namedtuple
#import RPi.GPIO as GPIO
# Fonctions


def dico_csv():
    try:    # essai d'ouverture
        f = open('caracteres4.csv', mode='r')   # ouverture csv en mode read
    except FileNotFoundError:   # si fichier non trouvé
        print("Fichier non trouvé!")    # affichage erreur
        raise   # raise de l'erreur
    else:   # si fichier ouvert
        dictionnaire = build_namedtuple(f)  # construction du dictionnaire
        f.close()   # fermeture fichier
        return dictionnaire  # renvoi dictionnaire


def build_namedtuple(file):


    return   # renvoi dictionnaire construit



def synthese_vocale(message):   # fonction de lecture via synthèse vocale
    commande = "espeak-ng -a 200 -v mb-fr1 -s 150 " + "\"" + message + "\"" + " --stdout | aplay"  # préparation de la commande
    print(commande)  # debug: affichage de la commande avant exécution
    resultat_exec = subprocess.run(commande,shell=True)  # exécution de la commande dans shell et récup objet de subprocess
    if resultat_exec.returncode != 0:  # vérif si returncode diff de 0
        print("Erreur dans la lecture")
    else:
        print("Execution reussie")


def validationBP():
    pinBtn = 19
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinBtn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    bp = 0
    while bp == 0:
        etat = GPIO.input(pinBtn)
        if etat == 1:
            print("Appui detécté")
            bp = 1

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
        synthese_vocale("Poser:") #coucou
        synthese_vocale(exo)

        validationBP()

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
