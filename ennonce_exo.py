# coding: UTF-8
"""
Script: DVM_R/ennonce_exo
Création: admin, le 26/03/2021
"""

# Imports
import sqlite3  #importation du module sqlite3

#Class
class Eleves:
    def __init__(self, nom="Dupond", prenom="Pierre", niveau = 6): #definition d'un constructeur surchargé pour identification élève
        #attribut privés
        self.__nom = nom
        self.__prenom = prenom
        self.__niveau = niveau

    def affiche_eleve(self): #méthode pour l'énoncer de l'élève
        print(self.__nom, self.__prenom, self.__niveau)

    #propriétés pour attributs privés
    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def niveau(self):
        return self.__niveau

    def verifier_eleve(self): #Verification que l'élève existe
        cnx = sqlite3.connect('DVmath_exercice.db')  # acces base de donnée
        cursor = cnx.cursor()
        cursor.execute("SELECT count(*) FROM eleves WHERE nom = ? and prenom = ? and niveau = ?", (self.__nom, self.__prenom, self.__niveau,))
        r = cursor.fetchone()[0]
        if r==1:
            print("eleve existant")
            existant = 1
        else:
            print("eleve inconnu")
            existant = 0
        cursor.close()
        cnx.close()


class Exercices:
    def __init__(self, numero=0, calcul="1+1", resultat= 0, niveau = 6):
        self.__numero = numero
        self.__calcul = calcul
        self.__resultat = resultat
        self.__niveau = niveau

    def affiche_exercices(self):
        print(self.__numero, self.__calcul, self.__resultat)

    @property
    def numero(self):
        return self.__numero

    @property
    def calcul(self):
        return self.__calcul

    @property
    def resultat(self):
        return self.__resultat


    def affiche_calcul_bdd(self, numero, niveau):  # passe en parametres le numero et le niveau
        cnx = sqlite3.connect('DVmath_exercice.db')  # acces base de donnée
        cursor = cnx.cursor()
        request_val = "SELECT exercice FROM exercices WHERE numero = ? and niveau = ?"  # requete
        data = (self.__numero, self.__niveau)
        cursor.execute(request_val, data)
        resultat = cursor.fetchall()  # afficher plusieurs donnée en tableau
        cursor.close()
        cnx.close()

        calcul_bdd = ''.join(resultat[0])  # conversion de la valeur à l'indice 0 du tuple en chaîne de caractères
        print("calcul propose:", calcul_bdd)  # affiche le resultat de la requete

        #return calcul_bdd  # renvoie le calcul


class Travaux_eleves:
    def __init__(self, nom = "Dupond", niveau = 6, calcul = "1+2", calcul_pose = "1+2", resultat = 3, resultat_pose = 3):
        self.__nom = nom
        self.__niveau = niveau
        self.__calcul = calcul
        self.__calcul_pose = calcul_pose
        self.__resultat = resultat
        self.__resultat_pose = resultat_pose

    def affiche_travaux(self):
        print(self.__nom, self.__niveau, self.__calcul, self.__calcul_pose, self.__resultat,  )

    @property
    def nom(self):
        return self.__nom

    @property
    def niveau(self):
        return self.__niveau

    @property
    def calcul(self):
        return self.__calcul

    @property
    def calcul_pose(self):
        return self.__calcul_pose

    @property
    def resultat(self):
        return self.__resultat

    @property
    def resultat_pose(self):
        return self.__resultat_pose


# Fonctions
def affiche_eleves_bdd(niv): #passe en parametres le numero et le niveau
    cnx = sqlite3.connect('DVmath_exercice.db')  #acces base de donnée
    cursor = cnx.cursor()
    request_val = "SELECT niveau FROM eleve WHERE nom=? AND prenom=?"  #requete
    data = (niv)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs donnée en tableau
    cursor.close()
    cnx.close()

    return niv


def choisir_exo():
    num_exo = 2
    print("Quel exercice souhaitez vous réaliser ? >", num_exo)
    if num_exo in range(1, 999):
        print("Vous avez choisi l'exercice", num_exo)  # va affciher le numéro de l'exercice definis
    else:
        print("Erreur")

    return num_exo  # renvoie le numero d'exercice entrer par l'élève (numero_exo)


def affiche_calcul_bdd(numero, niv): #passe en parametres le numero et le niveau
    cnx = sqlite3.connect('DVmath_exercice.db')  #acces base de donnée
    cursor = cnx.cursor()
    request_val = "SELECT exercice FROM exercices WHERE numero = ? and niveau = ?"  #requete
    data = (numero, niv)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs donnée en tableau
    cursor.close()
    cnx.close()

    calcul_bdd = ''.join(resultat[0]) #conversion de la valeur à l'indice 0 du tuple en chaîne de caractères
    print("calcul propose:", calcul_bdd) #affiche le resultat de la requete

    return calcul_bdd #renvoie le calcul


def affiche_resultat_bdd(numero):
    cnx = sqlite3.connect('DVmath_exercice.db')  #acces base de donnée
    cursor = cnx.cursor()
    request_val = "SELECT resultat FROM exercices WHERE numero = ?"  #requete
    data = (numero)
    cursor.execute(request_val, data)
    resultat = cursor.fetchall()  #afficher plusieurs donnée en tableau
    cursor.close()
    cnx.close()

    resultat_bdd = ''.join(resultat[0]) #conversion de la valeur à l'indice 0 du tuple en chaîne de caractères
    #print("Resultat du calcul:", resultat_bdd) #affiche le resultat de la requete

    return resultat_bdd #renvoie le calcul




# Programme principal 
def main():
        #instanciation pour Eleves
        eleve1 = Eleves("Larue", "Dylan", 4) #Appel de la classe avec de nouveau parametres
        print("-----------------Eleves----------------")
        print(eleve1.nom, eleve1.prenom, eleve1.niveau) #Affichage
        eleve1.verifier_eleve() #appel fonction

        print("-------------Choix Exercice------------")
        choisir_exo() #Appel fonction qui permet de chosir un exercice


        print("---------------Exercices---------------")
        exercice1 = Exercices(2, "36-(13-8)", 31, 4)
        exercice1.affiche_calcul_bdd()
        print(exercice1.numero, exercice1.calcul, exercice1.resultat)

        print("---------------Travaux_eleves--------------------------")
        travaux = Travaux_eleves("Dupond", 6, "1+2", "1+2", 3, 3)
        print(travaux.nom, travaux.niveau, travaux.calcul, travaux.calcul_pose, travaux.resultat, travaux.resultat_pose)



if __name__ == '__main__':
    main()
    # Fin
