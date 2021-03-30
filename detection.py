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
    f = open('caracteres.csv')
    csvfile = csv.reader(open("caracteres.csv"))
    caracteres = dict(csvfile)
    print(caracteres["150"])


if __name__ == '__main__':
    main()
# Fin
