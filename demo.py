# pour traitement csv
import csv
# pour synthese vocale
import subprocess
# pour lire fichier en UTF-8
import codecs


def dico_csv():  # ouverture fichier CSV
    try:  # essai d'ouverture
        f = codecs.open('caracteres4.csv', 'r', 'utf-8')  # ouverture csv en mode read
    except FileNotFoundError:  # si fichier non trouvé
        print("Fichier non trouvé!")  # affichage erreur
        raise  # raise de l'erreur
    else:  # si fichier ouvert
        dictionnaire = build_dico(f)  # construction du dictionnaire
        f.close()  # fermeture fichier
        return dictionnaire  # renvoi dictionnaire


def build_dico(file):  # construction du dictionnaire à partir du CSV
    dialect = csv.Sniffer().sniff(
        file.readline())  # objet recap infos fichier csv (détermination séparateur sur ligne 0)
    file.seek(0)  # retour ligne 0
    caracteres = list(csv.DictReader(file, dialect=dialect))  # importation données sous forme liste
    id = range(47)
    dict_complet = dict(zip(id, caracteres))  # création du dictionnaire (association liste résistances à caractères)

    return dict_complet  # renvoi dictionnaire construit


# def synthese_vocale(message):  # fonction de lecture via synthèse vocale
#     commande = "espeak-ng -a 200 -v mb-fr1 -s 150 " + "\"" + message + "\"" + " --stdout | aplay"  # préparation de la commande
#     print(commande)  # debug: affichage de la commande avant exécution
#     resultat_exec = subprocess.run(commande,
#                                    shell=True)  # exécution de la commande dans shell et récup objet de subprocess
#     if resultat_exec.returncode != 0:  # vérif si returncode diff de 0
#         print("débug: Erreur dans la lecture")
#     else:
#         print("débug: Execution reussie")


def check_dico(dico, valres):  # lecture du dictionnaire pour reconnaissance caractère
    for key, value in dico.items():
        seuil_bas = dico[key].get('sbas')   # obtention valeur de sbas
        seuil_bas = int(seuil_bas)  # conversion en int
        seuil_haut = dico[key].get('shaut') # obtention valeur de shaut
        seuil_haut = int(seuil_haut)    # conversion en int
        if seuil_bas <= valres <= seuil_haut:   # si valeur donnée en paramètres comprise entre sbas et shaut
            caractere = dico[key].get('caractere')  # on récupère le caractère correspondant
            #print("débug: ", caractere)  # debug
            return caractere
    try:
        caractere   # si variable caractere non créée
    except NameError:
        print("erreur")
        #synthese_vocale("Erreur de détection!")  # lecture erreur
        raise  # raise d'une erreur


# Programme principal
def main():
    # val1 = 15
    # val2 = 130
    # val3 = 15
    dictionnaire = dico_csv()  # build du dictionnaire
    # caractere1 = check_dico(dictionnaire, val1)
    # print("caractère correspondant à " + str(val1) + " --> " + caractere1)
    # caractere2 = check_dico(dictionnaire, val2)
    # print("caractère correspondant à " + str(val2) + " --> " + caractere2)
    # caractere3 = check_dico(dictionnaire, val3)
    # print("caractère correspondant à " + str(val3) + " --> " + caractere3)

    print("Entrer valeur numérique: ")
    val = input()   # entrée pour tests
    val = int(val)  # conversion en int
    caractere = check_dico(dictionnaire, val)   # check dans dictionnaire
    print(caractere)    # affichage caractère si existant


if __name__ == '__main__':
    main()