# coding: UTF-8
"""
Script: ProjetBTS/detection
Création: admin, le 02/03/2021
"""


# Imports

#pour traitement csv
import csv
#pour synthese vocale
import subprocess
#pour lire fichier en UTF-8
import codecs
#pour lecture du GPIO
import RPi.GPIO as GPIO
#pour lecture du MCP
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


# classes
class CelluleBraille:
	def __init__(self, valCH0 = 0, valCH1 = 0, valCH2 = 0 , valCH3 = 0, valCH4 = 0, valCH5 = 0, valCH6 = 0, valCH7 = 0):
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
	def create_MCP(cls, spi, cs): 	# creation objet mcp
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


# Fonctions
def dico_csv():     #ouverture fichier CSV
	try:    # essai d'ouverture
		f = codecs.open('caracteres4.csv','r', 'utf-8') # ouverture csv en mode read
	except FileNotFoundError:   # si fichier non trouvé
		print("Fichier non trouvé!")    # affichage erreur
		raise   # raise de l'erreur
	else:   # si fichier ouvert
		dictionnaire = build_dico(f)  # construction du dictionnaire
		f.close()   # fermeture fichier
		return dictionnaire  # renvoi dictionnaire


def build_dico(file):       #construction du dictionnaire à partir du CSV
	dialect = csv.Sniffer().sniff(file.readline())  # objet recap infos fichier csv (détermination séparateur sur ligne 0)
	file.seek(0)    # retour ligne 0
	caracteres = list(csv.DictReader(file, dialect=dialect))    # importation données sous forme liste
	id = range(47)
	dict_complet = dict(zip(id, caracteres))   # création du dictionnaire (association liste résistances à caractères)

	return dict_complet  # renvoi dictionnaire construit


def synthese_vocale(message):   # fonction de lecture via synthèse vocale
	commande = "espeak-ng -a 200 -v mb-fr1 -s 150 " + "\"" + message + "\"" + " --stdout | aplay"  # préparation de la commande
	print(commande)  # debug: affichage de la commande avant exécution
	resultat_exec = subprocess.run(commande,shell=True)  # exécution de la commande dans shell et récup objet de subprocess
	if resultat_exec.returncode != 0:  # vérif si returncode diff de 0
		print("débug: Erreur dans la lecture")
	else:
		print("débug: Execution reussie")


def validationBP():         # met en pause exec du code jusqu'à appui bouton
	pinBtn = 19		# Pin du bp sur le GPIO
	GPIO.setmode(GPIO.BCM)		# pour reference GPIO 19 et pas pin 35
	GPIO.setup(pinBtn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)		# mise du GPIO 19 en input, activation res pull dwn
	bp = 0		# set variable bascule
	while bp == 0:
		etat = GPIO.input(pinBtn)		# lecture de l'état du GPIO 19
		if etat == 1:		# si niveau logique à 1
			#print("débug: Appui detécté")
			bp = 1		# bascule de la variable


def check_dico(dico, valres):       # lecture du dictionnaire pour reconnaissance caractère
	for key, value in dico.items():
		seuil_bas = dico[key].get('sbas')	 # lecture dictionnaire pour seuil bas
		seuil_bas = int(seuil_bas)		# conversion en int
		seuil_haut = dico[key].get('shaut')		# lecture dictionnaire pour seuil haut
		seuil_haut = int(seuil_haut)		# conversion en int
		if seuil_bas <= valres <= seuil_haut:
			caractere = dico[key].get('caractere')		# lecture dictionnaire pour caractère
			#print("débug: ", key, caractere)  # debug
			return caractere
	try:
		caractere  # si variable caractere non créée
	except NameError:
		synthese_vocale("Erreur de détection!")  # lecture erreur
		raise  # raise d'une erreur


# Programme principal
def main():
	# ------------------initialisations----------------------------------
	spi = CelluleBraille.create_SPI()      #creation bus spi
	cs = CelluleBraille.create_CS()		#creation chip select
	mcp = CelluleBraille.create_MCP(spi, cs)   #creation objet mcp
	Cellules = CelluleBraille()
	dictionnaire = dico_csv()   # build du dictionnaire
	chaineCaract = ""               # définition chaine caractères vide
	validation = False          # variable si calcul posé est juste
	exo = "1+1"                     # exo de test
	resultat = 2

	# -----------------Programme principal--------------------------------
	# -----------------Pose calcul----------------------------------------
	while not validation:     # Boucle verification entrée juste
		print("débug: Entrer",exo, ": ")       # print pour les tests
		synthese_vocale("Poser:") #coucou
		synthese_vocale(exo)

		#validationBP()		# attente validation de l'élève

		i = 0		# nombre d'itérations
		Cellules.lire_Channel(mcp)		# lecture du mcp3008
		for attr, value in Cellules.__dict__.items():   # Boucle reconnaissance entrée
			val = value		# affectation valeur
			print(val)		# débug
			caract = check_dico(dictionnaire, val)		# correspondance avec le dictionnaire
			chaineCaract = chaineCaract + caract		# concaténation caractères reconnus
			i += 1		# incrémentation nombre d'itérations
			if i == len(exo):		# si nombre d'itérations = longeur de exo
				break		# sortie de la boucle

		if chaineCaract == exo:         # verfification si exo saisi par eleve identique a exo propose
			validation = True       # changement etat pour sortie boucle de saisie
			synthese_vocale(chaineCaract)
			synthese_vocale("calcul posé juste.")
			chaineCaract = ""       # reset variable chaineCaract

		else:                   # si exo saisi incorrect
			synthese_vocale(chaineCaract)
			synthese_vocale("calcul posé faux.")
			chaineCaract = ""           # reset variable chaineCaract

	# ----------------------Pose résultat---------------------------------
	validation = False
	while not validation:
		synthese_vocale("Poser le résultat.")

		validationBP()		# attente validation de l'élève

		i = 0
		Cellules.lire_Channel(mcp)
		for attr, value in Cellules.__dict__.items():  # Boucle reconnaissance entrée
			val = value  # affectation valeur
			print(val)  # débug
			caract = check_dico(dictionnaire, val)  # correspondance avec le dictionnaire
			chaineCaract = chaineCaract + caract  # concaténation caractères reconnus
			i += 1  # incrémentation nombre d'itérations
			if i == len(str(resultat)):  # si nombre d'itérations = longeur du resultat
				break  # sortie de la boucle

		if chaineCaract == str(resultat):  # verfification si resultat saisi par eleve identique a resultat propose
			validation = True  # changement etat pour sortie boucle de saisie
			synthese_vocale(chaineCaract)
			synthese_vocale("Résultat juste.")
			print("exercice juste")  # debug: affichage exercice juste
			chaineCaract = ""  # reset variable chaineCaract

		else:  # si exo saisi incorrect
			print("exercice faux")  # debug: affichage exo faux
			synthese_vocale(chaineCaract)
			synthese_vocale("calcul posé faux.")
			chaineCaract = ""  # reset variable chaineCaract



# Fin

# https://www.youtube.com/watch?v=Hu4I3GAAOmA l15


#     for i in dict_complet.items():
#         print(i)
