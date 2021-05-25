# coding: UTF-8
"""
Script: ProjetBTS/detection
Création: admin, le 02/03/2021
"""


# Imports

import csv
import subprocess
import codecs
import time
#import RPi.GPIO as GPIO
# Fonctions


def dico_csv():
    try:    # essai d'ouverture
        f = codecs.open('caracteres4.csv','r', 'utf-8') # ouverture csv en mode read
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
    #print(caracteres[:15])
    #dict = [elt['id'] for elt in caracteres]     # liste des valeurs de résistances
    id = range(47)
    dict_complet = dict(zip(id, caracteres))   # création du dictionnaire (association liste résistances à caractères)

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
        caractere = dico[res]['sbas']
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


def check_dico(dico, valres):
    dictionnaire = dico
    for key, value in dictionnaire.items():
        seuil_bas = dictionnaire[key].get('sbas')
        seuil_bas = int(seuil_bas)
        seuil_haut = dictionnaire[key].get('shaut')
        seuil_haut = int(seuil_haut)
        #time.sleep(0.01)
        if seuil_bas <= valres <= seuil_haut:
            print(key, dictionnaire[key].get('caractere'))
            break


# Programme principal


def main():
    # ------------------initialisations----------------------------------
    dictionnaire = dico_csv()   # build du dictionnaire
    chaineCaract = ""               # définition chaine caractères vide
    validation = False          # variable si calcul posé est juste
    exo = "1+1"                     # exo de test
    resultat = 1+1

    #for key, value in dictionnaire.items():
    #    print(key, dictionnaire[key].get('sbas'), dictionnaire[key].get('shaut'))
    check_dico(dictionnaire, 880)

    while not validation:     # Boucle verification entrée juste
        print("Entrer",exo, ": ")       # print pour les tests
        synthese_vocale("Poser:") #coucou
        synthese_vocale(exo)

        #validationBP()

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
