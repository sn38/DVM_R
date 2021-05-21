# coding: UTF-8
"""
Script: DVM_R/namedtuple
Création: admin, le 19/05/2021
"""


# Imports
import csv
from collections import namedtuple
import codecs

# Fonctions
# Programme principal
def main():
    Row = namedtuple('Caractere', ('sbas', 'shaut', 'caractere'))

    with codecs.open('caracteres4.csv', 'r', 'utf-8') as f:
        r = csv.reader(f, delimiter=';')
        next(r)  # Skip header
        rows = [Row(*l) for l in r]
        print("content of csv file:")
        print(rows)

    #Caracteres = namedtuple('Caracteres', ['sbas', 'shaut', 'caractere'])
    #csvReader = csv.reader(open("caracteres4.csv", "r"))

    #print("Contents of the CSV file:")
    #for caracteres in map(Caracteres._make, csvReader):
    #    print(caracteres.caractere, caracteres.sbas, caracteres.shaut)


if __name__ == '__main__':
    main()
# Fin
