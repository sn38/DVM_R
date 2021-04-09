# coding: UTF-8
"""
Script: ProjetBTS/detection
Création: admin, le 02/03/2021
"""


# Imports

import csv
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
    return dict_complet # renvoi dictionnaire construit


def lire_dico(dico, res):
    try:    # essai lecture dans dictionnaire
        caractere = dico[res]['caractere']
    except LookupError:     # si valeur hors dictionnaire
        print("Erreur de résistance!")  # affichage erreur
        raise # raise de l'erreur
    else:   # si valeur dans dictionnaire
        print('Caractère correspondant à', res, 'ohm:', caractere) # affichage caractère correspondant

# Programme principal
def main():
    dictionnaire = dico_csv()

    print("Entrer résistance: ")
    val_res = input()

    lire_dico(dictionnaire, val_res)

    # print(dialect.delimiter)   # affiche le délimiteur


if __name__ == '__main__':
    main()
# Fin

# https://www.youtube.com/watch?v=Hu4I3GAAOmA l15


#     for i in dict_complet.items():
#         print(i)
