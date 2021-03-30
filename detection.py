# coding: UTF-8
"""
Script: ProjetBTS/detection
Création: admin, le 02/03/2021
"""


# Imports
#from resistances import detect
import csv
# Fonctions

# Programme principal
def main():
    with open('caracteres2.csv', mode='r') as f:                #ouverture fichier csv en lecture         #https://www.youtube.com/watch?v=Hu4I3GAAOmA
        dialect = csv.Sniffer().sniff(f.readline())             #objet recap infos fichier csv (détermination séparateur sur ligne 0)
        f.seek(0)                                               #retour à première ligne
        caracteres = list(csv.DictReader(f, dialect=dialect))   #importation données sous forme liste
    resistances = [elt['resistance'] for elt in caracteres]     #liste des valeurs de résistances

    dict_complet = dict(zip(resistances, caracteres))           #création du dictionnaire (association liste résistances à caractères
    print(dict_complet['175']['caractere'])


if __name__ == '__main__':
    main()
# Fin
