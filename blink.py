# Init code credit to examples by Tony DiCola
# License: Public Domain

import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# GPIO config
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Main loop
while True:
	for i in range(5):
		GPIO.output(11, True)    # led on
		time.sleep(0.5)	         # wait 500ms
		GPIO.output(11, False)   # led off
		time.sleep(0.5)	         # wait 500ms
	
	for i in range(50):
		light = mcp.read_adc(1)
		print("light sensor:", light)
		if light < 300:
			print("dark")
		else:
			print ("bright")
		time.sleep(.1)
	
	for i in range(4):
		GPIO.output(11, True)
		time.sleep(.2)
		GPIO.output(11, False)
		time.sleep(.2)

	for i in range(50):
		sound = mcp.read_adc(0)
		print("sound sensor:", sound)
		if sound > 800:
			GPIO.output(11, True)
			time.sleep(.1)
			GPIO.output(11, False)
		else:
			time.sleep(.1)
	
	for i in range(4):
		GPIO.output(11, True)
		time.sleep(.2)
		GPIO.output(11, False)
		time.sleep(.2)
