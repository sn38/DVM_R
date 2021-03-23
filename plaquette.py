import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

def conv(n):
	if n > 1:
		conv(n // 2)
	print(n % 2, end='')


# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
chan2 = AnalogIn(mcp, MCP.P2)
chan3 = AnalogIn(mcp, MCP.P3)
chan4 = AnalogIn(mcp, MCP.P4)
chan5 = AnalogIn(mcp, MCP.P5)

while(True):
	cha0 = (chan0.value/65536)*1024
	cha1 = (chan1.value/65536)*1024
	cha2 = (chan2.value/65536)*1024
	cha3 = (chan3.value/65536)*1024
	cha4 = (chan4.value/65536)*1024
	cha5 = (chan5.value/65536)*1024
	#print('Raw ADC Value: ', (chan0.value/65536)*1024)
	#print('Raw ADC Value: ', (chan1.value/65536)*1024)
	#print('Raw ADC Value: ', (chan2.value/65536)*1024)
	#print('Raw ADC Value: ', (chan3.value/65536)*1024)
	#print('Raw ADC Value: ', (chan4.value/65536)*1024)
	#print('Raw ADC Value: ', (chan5.value/65536)*1024)
	#print('ADC Voltage chan1(pont diviseur 1): ' + str(cha0) + ' V')
	#print('ADC Voltage chan2(pont diviseur 2): ' + str(cha1) + ' V')
	#print('ADC Voltage chan3(pont diviseur 3): ' + str(cha2) + ' V')
	#print('ADC Voltage 3v3                   : ' + str(cha3) + ' V')
	#print('ADC Voltage chan4(pont diviseur 4): ' + str(cha4) + ' V')
	#print('ADC Voltage chan5(pont diviseur 5): ' + str(cha5) + ' V')

	#chan0.value = conv((chan0.value/65536)*1024)
	#print('nombre binaire = ', conv((chan0.value/65536)*1024))
	
	print('----------------------------------------------')
	print(' ', cha0, cha1, cha2, cha3, cha4, cha5, sep=' | ')
	#print(' ', bin(cha0), bin(cha2), bin(cha3), bin(cha4), bin(cha5))






	time.sleep(1)

	
