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


def synthese_vocale(message):  # fonction de lecture via synthèse vocale
    commande = "espeak-ng -a 200 -v mb-fr1 -s 150 " + "\"" + message + "\"" + " --stdout | aplay"  # préparation de la commande
    print(commande)  # debug: affichage de la commande avant exécution
    resultat_exec = subprocess.run(commande,
                                   shell=True)  # exécution de la commande dans shell et récup objet de subprocess
    if resultat_exec.returncode != 0:  # vérif si returncode diff de 0
        print("débug: Erreur dans la lecture")
    else:
        print("débug: Execution reussie")


def check_dico(dico, valres):  # lecture du dictionnaire pour reconnaissance caractère
    for key, value in dico.items():
        seuil_bas = dico[key].get('sbas')
        seuil_bas = int(seuil_bas)
        seuil_haut = dico[key].get('shaut')
        seuil_haut = int(seuil_haut)
        if seuil_bas <= valres <= seuil_haut:
            caractere = dico[key].get('caractere')
            #print("débug: ", caractere)  # debug
            return caractere
    try:
        caractere   # si variable caractere non créée
    except NameError:
        synthese_vocale("Erreur de détection!")  # lecture erreur
        raise  # raise d'une erreur


# Programme principal
def main():
    dictionnaire = dico_csv()  # build du dictionnaire
    caractere1 = check_dico(dictionnaire, 15)
    print(caractere1)
    caractere2 = check_dico(dictionnaire, 38)
    print(caractere2)
    caractere3 = check_dico(dictionnaire, 15)
    print(caractere3)


if __name__ == '__main__':
    main()