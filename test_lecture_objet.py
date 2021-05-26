# coding: UTF-8
"""
Script: DVM_R/test_lecture_objet
Création: admin, le 26/05/2021
"""


# Imports
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
import time
from adafruit_mcp3xxx.analog_in import AnalogIn


# Fonctions
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
		print("spi créé")
		return spi

	@classmethod
	def create_CS(cls):  # creation chip select
		cs = digitalio.DigitalInOut(board.D5)
		print("cs créé")
		return cs

	@classmethod
	def create_MCP(cls, spi, cs):
		mcp = MCP.MCP3008(spi, cs)
		print("mcp créé")
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


# Programme principal
def main():
	spi = CelluleBraille.create_SPI()
	cs = CelluleBraille.create_CS()
	mcp = CelluleBraille.create_MCP(spi, cs)
	#channels = [CelluleBraille('valCH0', 'valCH1', 'valCH2', 'valCH3', 'valCH4', 'valCH5', 'valCH6', 'valCH7')]

	Cellules = CelluleBraille()
	Cellules.lire_Channel(mcp)
	for attr, value in Cellules.__dict__.items():
		print(value)


if __name__ == '__main__':
	main()
# Fin
