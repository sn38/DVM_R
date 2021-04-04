# coding: UTF-8
"""
Script: ProjetBTS/detection
Création: admin, le 02/03/2021
"""


# Imports

import csv
# Fonctions

# Programme principal
def main():
    with open('caracteres3.csv', mode='r') as f:                # ouverture fichier csv en lecture
        dialect = csv.Sniffer().sniff(f.readline())             # objet recap infos fichier csv (détermination séparateur sur ligne 0)
        f.seek(0)                                               # retour à première ligne
        caracteres = list(csv.DictReader(f, dialect=dialect))   # importation données sous forme liste
    resistances = [elt['resistance'] for elt in caracteres]     # liste des valeurs de résistances

    dict_complet = dict(zip(resistances, caracteres))           # création du dictionnaire (association liste résistances à caractères)
    print("Entrer résistance: ")
    val_res = input()
    if val_res in dict_complet:                                 # vérif si valeur présent dans dico
        caract = dict_complet[val_res]['caractere']
        print('Caractère correspondant à', val_res, 'ohm:', caract)  # affichage caractère à une valeur de résistance
    else:
        print('Erreur de résistance')

    # print(dialect.delimiter)   # affiche le délimiteur


if __name__ == '__main__':
    main()
# Fin

# https://www.youtube.com/watch?v=Hu4I3GAAOmA l15


#     for i in dict_complet.items():
#         print(i)
