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
    with open('caracteres2.csv', mode='r') as f:                #https://www.youtube.com/watch?v=Hu4I3GAAOmA
        dialect = csv.Sniffer().sniff(f.readline())
        f.seek(0)
        caracteres = list(csv.DictReader(f, dialect=dialect))
    resistances = [elt['resistance'] for elt in caracteres]

    dict_complet = dict(zip(resistances, caracteres))
    print(dict_complet['175'])


if __name__ == '__main__':
    main()
# Fin
