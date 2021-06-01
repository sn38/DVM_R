# coding: UTF-8
"""
Script: ProjetBTS/detection
Création: admin, le 02/03/2021
"""

# Imports

# pour traitement csv
import csv
# pour synthese vocale
import subprocess
# pour lire fichier en UTF-8
import codecs
# pour lecture du GPIO
import RPi.GPIO as GPIO

# pour lecture du MCP --> Partie Evan LACOMBE
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# pour lecture/ecriture bdd --> Partie Milly NOURDIN
import sqlite3


# classes
class CelluleBraille:  # Réalisé conjointement avec Evan LACOMBE
	def __init__(self, valCH0=0, valCH1=0, valCH2=0, valCH3=0, valCH4=0, valCH5=0, valCH6=0, valCH7=0):
		self.__valCH0 = valCH0
		self.__valCH1 = valCH1
		self.__valCH2 = valCH2
		self.__valCH3 = valCH3
		self.__valCH4 = valCH4
		self.__valCH5 = valCH5
		self.__valCH6 = valCH6
		self.__valCH7 = valCH7

	@property
	def valCH0(self):
		return self.__valCH0

	@property
	def valCH1(self):
		return self.__valCH1

	@property
	def valCH2(self):
		return self.__valCH2

	@property
	def valCH3(self):
		return self.__valCH3

	@property
	def valCH4(self):
		return self.__valCH4

	@property
	def valCH5(self):
		return self.__valCH5

	@property
	def valCH6(self):
		return self.__valCH6

	@property
	def valCH7(self):
		return self.__valCH7

	@classmethod
	def create_SPI(cls):  # creation bus spi
		spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
		print("débug: spi créé")
		return spi

	@classmethod
	def create_CS(cls):  # creation chip select
		cs = digitalio.DigitalInOut(board.D5)
		print("débug: cs créé")
		return cs

	@classmethod
	def create_MCP(cls, spi, cs):  # creation objet mcp
		mcp = MCP.MCP3008(spi, cs)
		print("débug: mcp créé")
		return mcp

	def lire_Channel(self, mcp):
		chan0 = AnalogIn(mcp, MCP.P0)
		chan1 = AnalogIn(mcp, MCP.P1)
		chan2 = AnalogIn(mcp, MCP.P2)
		chan3 = AnalogIn(mcp, MCP.P3)
		chan4 = AnalogIn(mcp, MCP.P4)
		chan5 = AnalogIn(mcp, MCP.P5)
		chan6 = AnalogIn(mcp, MCP.P6)
		chan7 = AnalogIn(mcp, MCP.P7)

		self.__valCH0 = (chan0.value / 65536 * 1024)
		self.__valCH1 = (chan1.value / 65536 * 1024)
		self.__valCH2 = (chan2.value / 65536 * 1024)
		self.__valCH3 = (chan3.value / 65536 * 1024)
		self.__valCH4 = (chan4.value / 65536 * 1024)
		self.__valCH5 = (chan5.value / 65536 * 1024)
		self.__valCH6 = (chan6.value / 65536 * 1024)
		self.__valCH7 = (chan7.value / 65536 * 1024)


# Code rapatrié depuis le code de Milly NOURDIN
class Eleves:
	def __init__(self, nom="Dupond", prenom="Pierre", niveau=6):  # definition constructeur surchargé pour identif élève
		# attribut privés
		self.__nom = nom
		self.__prenom = prenom
		self.__niveau = niveau

	def affiche_eleve(self):  # méthode pour l'énoncer de l'élève
		print(self.__nom, self.__prenom, self.__niveau)

	# propriétés pour attributs privés
	@property
	def nom(self):
		return self.__nom

	@property
	def prenom(self):
		return self.__prenom

	@property
	def niveau(self):
		return self.__niveau

	def verifier_eleve(self):  # Verification que l'élève existe
		cnx = sqlite3.connect('DVmath_exercice.db')  # acces base de donnée
		cursor = cnx.cursor()
		cursor.execute(
			"SELECT count(*) FROM eleves WHERE nom = ? and prenom = ? and niveau = ?", (
				self.__nom, self.__prenom, self.__niveau,))
		r = cursor.fetchone()[0]
		if r == 1:
			synthese_vocale("élève existant")
			existant = 1
		else:
			synthese_vocale("eleve inconnu")
			existant = 0
		cursor.close()
		cnx.close()
		return existant


class Exercices:
	def __init__(self, numero="0", niveau=6, calcul="1+1", resultat="0"):  # definition d'un constructeur surchargé
		# attribut privés
		self.__numero = numero
		self.__niveau = niveau
		self.__calcul = calcul
		self.__resultat = resultat

	def affiche_exercices(self):
		print(self.__numero)

	# propriétés pour attributs privés
	@property
	def numero(self):
		return self.__numero

	@property
	def niveau(self):
		return self.__niveau

	@property
	def calcul(self):
		return self.__calcul

	@property
	def resultat(self):
		return self.__resultat

	def ennonce_calcul_bdd(self):  # en parametres passe le numero et le niveau
		cnx = sqlite3.connect('DVmath_exercice.db')  # acces base de donnée
		cursor = cnx.cursor()
		request_val = "SELECT exercice FROM exercices WHERE numero = ? and niveau = ?"  # requete
		data = (self.__numero, self.__niveau)
		cursor.execute(request_val, data)
		resultat = cursor.fetchall()  # afficher plusieurs donnée en tableau
		cursor.close()
		cnx.close()

		calcul_bdd = ''.join(resultat[0])  # conversion de la valeur à l'indice 0 du tuple en chaîne de caractères
		return calcul_bdd  # renvoie le calcul

	def def_calcul(self, calcul, resultat):  # permet de definir l'attribut calcul
		self.__calcul = calcul
		self.__resultat = resultat

	def affiche_resultat_bdd(self):
		cnx = sqlite3.connect('DVmath_exercice.db')  # acces base de donnée
		cursor = cnx.cursor()
		request_val = "SELECT resultat FROM exercices WHERE numero = ?"  # requete
		data = (self.__numero)
		cursor.execute(request_val, data)
		resultat = cursor.fetchall()  # afficher plusieurs donnée en tableau
		cursor.close()
		cnx.close()

		resultat_bdd = ''.join(resultat[0])  # conversion de la valeur à l'indice 0 du tuple en chaîne de caractères
		# print("Resultat du calcul:", resultat_bdd) #affiche le resultat de la requete

		return resultat_bdd  # renvoie le calcul


class Travaux_eleves:
	def __init__(self, nom="Dupond", niveau=6, calcul="1+2", calcul_pose="1+2", resultat=3, resultat_pose=3):
		self.__nom = nom
		self.__niveau = niveau
		self.__calcul = calcul
		self.__calcul_pose = calcul_pose
		self.__resultat = resultat
		self.__resultat_pose = resultat_pose

	def affiche_travaux(self):
		print(self.__nom, self.__niveau, self.__calcul, self.__calcul_pose, self.__resultat, )

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

	def travaux_eleve(self):  # Par Evan Lacombe
		# permet d'ouvrir la bdd
		cnx = sqlite3.connect('DVmath_exercice.db')
		cursor = cnx.cursor()
		# insertion des données
		request_val =\
			"INSERT INTO travaux_eleves (" \
			"nom, niveau, calcul, calcul_pose, resultat, resultat_pose) VALUES (?,?,?,?,?,?)"
		data = (self.__nom, self.__niveau, self.__calcul, self.__calcul_pose, self.__resultat, self.__resultat_pose)
		cursor.execute(request_val, data)
		resultat = cursor.fetchall()  # afficher plusieurs donnée en tableau
		cnx.commit()
		cursor.close()
		cnx.close()

		print("Acquis enregistrés")
		return resultat  # renvoie les données si besoin d'affichage


# Fonctions
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
	commande = \
		"espeak-ng -a 200 -v mb-fr1 -s 150 " + "\"" + message + "\"" + " --stdout | aplay"  # préparation de la commande
	print(commande)  # debug: affichage de la commande avant exécution
	resultat_exec = subprocess.run(
		commande, shell=True)  # exécution de la commande dans shell et récup objet de subprocess
	if resultat_exec.returncode != 0:  # vérif si returncode diff de 0
		print("débug: Erreur dans la lecture")
	else:
		print("débug: Execution reussie")


def validationBP():  # met en pause exec du code jusqu'à appui bouton
	pinBtn = 19  # Pin du bp sur le GPIO
	GPIO.setmode(GPIO.BCM)  # pour reference GPIO 19 et pas pin 35
	GPIO.setup(pinBtn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # mise du GPIO 19 en input, activation res pull dwn
	bp = 0  # set variable bascule
	while bp == 0:
		etat = GPIO.input(pinBtn)  # lecture de l'état du GPIO 19
		if etat == 1:  # si niveau logique à 1
			# print("débug: Appui detécté")
			bp = 1  # bascule de la variable


def check_dico(dico, valres):  # lecture du dictionnaire pour reconnaissance caractère
	for key, value in dico.items():
		seuil_bas = dico[key].get('sbas')  # lecture dictionnaire pour seuil bas
		seuil_bas = int(seuil_bas)  # conversion en int
		seuil_haut = dico[key].get('shaut')  # lecture dictionnaire pour seuil haut
		seuil_haut = int(seuil_haut)  # conversion en int
		if seuil_bas <= valres <= seuil_haut:
			caractere = dico[key].get('caractere')  # lecture dictionnaire pour caractère
			# print("débug: ", key, caractere)  # debug
			return caractere
	try:
		caractere  # si variable caractere non créée
	except NameError:
		synthese_vocale("Erreur de détection!")  # lecture erreur
		raise  # raise d'une erreur


def choisir_exo():
	num_exo = 3
	# print("Quel exercice souhaitez vous réaliser ? >", num_exo)
	if num_exo in range(1, 999):
		print("Vous avez choisi l'exercice", num_exo)  # va affciher le numéro de l'exercice definis
		exo = "Exercice" + str(num_exo) + "choisi"
		synthese_vocale(exo)
	else:
		# print("Erreur")
		synthese_vocale("Erreur")

	return num_exo  # renvoie le numero d'exercice entrer par l'élève (numero_exo)


def pose_calcul(exercice, cellule, dictionnaire, mcp):
	validation = False
	chaineCaract = ""
	while not validation:
		synthese_vocale("Poser:")  # coucou
		synthese_vocale(exercice.calcul)

		validationBP()  # attente validation de l'élève

		i = 0  # nombre d'itérations
		cellule.lire_Channel(mcp)  # lecture du mcp3008
		for attr, value in cellule.__dict__.items():  # Boucle reconnaissance entrée
			val = value  # affectation valeur
			print(val)  # débug
			caract = check_dico(dictionnaire, val)  # correspondance avec le dictionnaire
			chaineCaract = chaineCaract + caract  # concaténation caractères reconnus
			i += 1  # incrémentation nombre d'itérations
			if i == len(exercice.calcul):  # si nombre d'itérations = longeur de exo
				break  # sortie de la boucle

		if chaineCaract == exercice.calcul:  # verfification si exo saisi par eleve identique a exo propose
			validation = True  # changement etat pour sortie boucle de saisie
			synthese_vocale(chaineCaract)
			synthese_vocale("calcul posé juste.")
			chaineCaract = ""  # reset variable chaineCaract
			return chaineCaract

		else:  # si exo saisi incorrect
			synthese_vocale(chaineCaract)
			synthese_vocale("calcul posé faux.")
			chaineCaract = ""  # reset variable chaineCaract


# calcul_pose = input("Poser le calcul > ")  # present pour le test !!
# # calcul_pose = "32-14"
# if calcul_pose == object.calcul:
# 	print("Vous avez correctement ecrit le calcul : ", calcul_pose)
# else:
# 	print("Erreur")

# return calcul_pose


def pose_resultat(exercice, cellule, dictionnaire, mcp):
	chaineCaract = ""
	validation = False
	while not validation:
		synthese_vocale("Poser le résultat.")

		validationBP()  # attente validation de l'élève

		i = 0
		cellule.lire_Channel(mcp)
		for attr, value in cellule.__dict__.items():  # Boucle reconnaissance entrée
			val = value  # affectation valeur
			print(val)  # débug
			caract = check_dico(dictionnaire, val)  # correspondance avec le dictionnaire
			chaineCaract = chaineCaract + caract  # concaténation caractères reconnus
			i += 1  # incrémentation nombre d'itérations
			if i == len(str(exercice.resultat)):  # si nombre d'itérations = longeur du resultat
				break  # sortie de la boucle

		if chaineCaract == str(
				exercice.resultat):  # verfification si resultat saisi par eleve identique a resultat propose
			validation = True  # changement etat pour sortie boucle de saisie
			synthese_vocale(chaineCaract)
			synthese_vocale("Résultat juste.")
			print("exercice juste")  # debug: affichage exercice juste
			chaineCaract = ""  # reset variable chaineCaract
			return chaineCaract

		else:  # si exo saisi incorrect
			print("exercice faux")  # debug: affichage exo faux
			synthese_vocale(chaineCaract)
			synthese_vocale("calcul posé faux.")
			chaineCaract = ""  # reset variable chaineCaract


# resultat_pose = input("Poser le resultat >")
# if resultat_pose == exercice.resultat:
# 	print("Vous avez correctement posé le resultat : ", resultat_pose)
# else:
# 	print("Erreur")
#
# return resultat_pose


# Programme principal
def main():
	print("hello")
	# ------------------initialisations----------------------------------
	spi = CelluleBraille.create_SPI()  # creation bus spi
	cs = CelluleBraille.create_CS()  # creation chip select
	mcp = CelluleBraille.create_MCP(spi, cs)  # creation objet mcp
	Cellules = CelluleBraille()
	dictionnaire = dico_csv()  # build du dictionnaire
	# chaineCaract = ""  # définition chaine caractères vide
	validation = False  # variable si calcul posé est juste
	eleveValide = False
	# exo = "1+1"  # exo de test
	resultat = 2

	# -----------------Programme principal--------------------------------
	while not eleveValide:
		eleve1 = Eleves("Dupond", "Pierre", 6)  # instanciation classe avec de nouveau parametres
		enonceEleve = eleve1.nom + eleve1.prenom + str(eleve1.niveau)
		synthese_vocale(enonceEleve)
		existe = eleve1.verifier_eleve()  # Appel fonction de vérification
		if existe == 1:
			eleveValide = True

	exercice1 = Exercices(str(choisir_exo()), eleve1.niveau)  # instanciation classe

	# appel de def_calcul pour modifier l'attribut calcul et resultat de exercice
	exercice1.def_calcul(exercice1.ennonce_calcul_bdd(), exercice1.affiche_resultat_bdd())

	calcul_pose = pose_calcul(exercice1, Cellules, dictionnaire, mcp)

	resultat_pose = pose_resultat(exercice1, Cellules, dictionnaire, mcp)

	travaux1 = \
		Travaux_eleves(
			eleve1.nom, eleve1.niveau, exercice1.calcul, calcul_pose, int(exercice1.resultat), int(resultat_pose))
# # -----------------Pose calcul----------------------------------------
# while not validation:  # Boucle verification entrée juste
# 	print("débug: Entrer", exo, ": ")  # print pour les tests
# 	synthese_vocale("Poser:")  # coucou
# 	synthese_vocale(exercice1.calcul)
#
# 	# validationBP()		# attente validation de l'élève
#
# 	i = 0  # nombre d'itérations
# 	Cellules.lire_Channel(mcp)  # lecture du mcp3008
# 	for attr, value in Cellules.__dict__.items():  # Boucle reconnaissance entrée
# 		val = value  # affectation valeur
# 		print(val)  # débug
# 		caract = check_dico(dictionnaire, val)  # correspondance avec le dictionnaire
# 		chaineCaract = chaineCaract + caract  # concaténation caractères reconnus
# 		i += 1  # incrémentation nombre d'itérations
# 		if i == len(exercice1.calcul):  # si nombre d'itérations = longeur de exo
# 			break  # sortie de la boucle
#
# 	if chaineCaract == exercice1.calcul:  # verfification si exo saisi par eleve identique a exo propose
# 		validation = True  # changement etat pour sortie boucle de saisie
# 		synthese_vocale(chaineCaract)
# 		synthese_vocale("calcul posé juste.")
# 		chaineCaract = ""  # reset variable chaineCaract
#
# 	else:  # si exo saisi incorrect
# 		synthese_vocale(chaineCaract)
# 		synthese_vocale("calcul posé faux.")
# 		chaineCaract = ""  # reset variable chaineCaract
#
# # ----------------------Pose résultat---------------------------------
# validation = False
# while not validation:
# 	synthese_vocale("Poser le résultat.")
#
# 	validationBP()  # attente validation de l'élève
#
# 	i = 0
# 	Cellules.lire_Channel(mcp)
# 	for attr, value in Cellules.__dict__.items():  # Boucle reconnaissance entrée
# 		val = value  # affectation valeur
# 		print(val)  # débug
# 		caract = check_dico(dictionnaire, val)  # correspondance avec le dictionnaire
# 		chaineCaract = chaineCaract + caract  # concaténation caractères reconnus
# 		i += 1  # incrémentation nombre d'itérations
# 		if i == len(str(resultat)):  # si nombre d'itérations = longeur du resultat
# 			break  # sortie de la boucle
#
# 	if chaineCaract == str(resultat):  # verfification si resultat saisi par eleve identique a resultat propose
# 		validation = True  # changement etat pour sortie boucle de saisie
# 		synthese_vocale(chaineCaract)
# 		synthese_vocale("Résultat juste.")
# 		print("exercice juste")  # debug: affichage exercice juste
# 		chaineCaract = ""  # reset variable chaineCaract
#
# 	else:  # si exo saisi incorrect
# 		print("exercice faux")  # debug: affichage exo faux
# 		synthese_vocale(chaineCaract)
# 		synthese_vocale("calcul posé faux.")
# 		chaineCaract = ""  # reset variable chaineCaract

if __name__ == '__main__':
	main()

# Fin


