# coding: UTF-8
"""
Script: DVM_R/namedtuple
Création: admin, le 19/05/2021
"""


# Imports
import csv
from collections import namedtuple

# Fonctions
# Programme principal
def main():
    Caracteres = namedtuple('Caracteres', ['sbas', 'shaut', 'caractere'])
    csvReader = csv.reader(open("caracteres4.csv", "r"))

    print("Contents of the CSV file:")
    for caracteres in map(Caracteres._make, csvReader):
        print(caracteres.caractere, caracteres.sbas, caracteres.shaut)


if __name__ == '__main__':
    main()
# Fin
