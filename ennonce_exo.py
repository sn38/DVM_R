# coding: UTF-8
"""
Script: DVM_R/ennonce_exo
Création: admin, le 26/03/2021
"""


# Imports

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


class Exercices:
    def __init__(self, numero=3, calcul="1+2", resultat=3):
        self.__numero = numero
        self.__calcul = calcul
        self.__resultat = resultat

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


# Programme principal 
def main():
        #instanciation pour Eleves
        eleve1 = Eleves("Dupond", "Pierre", 6) #Appel de la classe avec de nouveau parametres
        print("-----------------Eleves----------------")
        print(eleve1.nom, eleve1.prenom, eleve1.niveau) #Affichage
        print("---------------Exercices---------------")
        exercice1 = Exercices(3, "1+2", 3)
        print(exercice1.numero, exercice1.calcul, exercice1.resultat)S
        print("---------------Travaux_eleves--------------------------")
        travaux = Travaux_eleves("Dupond", 6, "1+2", "1+2", 3, 3)
        print(travaux.nom, travaux.niveau, travaux.calcul, travaux.calcul_pose, travaux.resultat, travaux.resultat_pose)



if __name__ == '__main__':
    main()
    # Fin
