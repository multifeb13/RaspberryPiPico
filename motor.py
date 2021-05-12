import machine
import utime
from machine import ADC, PWM, Pin

pinMotorInA = machine.Pin(16, machine.Pin.OUT)
pinMotorInB = machine.Pin(17, machine.Pin.OUT)

pwmMotorInA = PWM( pinMotorInA )
pwmMotorInA.freq( 1000 )
pwmMotorInB = PWM( pinMotorInB )
pwmMotorInB.freq( 1000 )

adc = ADC(Pin(27))		#Pin27 = ADC1

def getADCRatio():
	data = adc.read_u16()

	if data < 384:
		data = 0

	return data / 65535

def getDuty():
	return int(65535 * getADCRatio())

while True:
	duty = getDuty()

	if duty == 0:	#state:break
		pwmMotorInA.duty_u16( 0 )
		pwmMotorInB.duty_u16( 0 )
	else:			#state:drive(CW)
		pwmMotorInA.duty_u16( duty )
		pwmMotorInB.duty_u16( 0 )
	utime.sleep(1)
