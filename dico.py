# coding: UTF-8
"""
Script: ProjetBTS/dico
Création: admin, le 09/03/2021
"""


# Imports
# Fonctions
# Programme principal
def main():
    keys = [100, 105, 110, 115, 121, 127, 133, 140, 147, 154, 162, 169, 178, 187, 196, 205, 215, 226, 237, 249, 261,
            274, 287, 301, 316, 332, 348, 365, 383, 402, 422, 442, 464, 487, 511, 536, 562, 590, 619, 649, 681, 715,
            750, 787, 825, 866, 909]

    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'racine carrée', '^', '+', '-', '*', '/', 'sin', 'cos',
              'tan', '(', ')', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    data = dict(zip(keys, values))
    print("Affichage dico")
    print(data)
    print(f"Lettre correspondante à 316 ohms: {data[316]}")

if __name__ == '__main__':
    main()
# Fin
