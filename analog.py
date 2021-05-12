#https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/8
from machine import ADC, Pin
import utime

adc = ADC(Pin(27))	#Pin27 = ADC1

while True:
	print(adc.read_u16())
	utime.sleep(0.5)
