import machine
import utime
from machine import PWM, Pin

pinMotorInA = machine.Pin(16, machine.Pin.OUT)
pinMotorInB = machine.Pin(17, machine.Pin.OUT)

pwmMotorInA = PWM( pinMotorInA )
pwmMotorInA.freq( 1000 )
pwmMotorInB = PWM( pinMotorInB )
pwmMotorInB.freq( 1000 )

while True:
	#rotate CW
	pwmMotorInA.duty_u16( 32767 )	# 100% = 65535, 0% = 0
	pwmMotorInB.duty_u16( 0 )
	utime.sleep(1)
