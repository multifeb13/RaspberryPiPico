import machine
import utime

pinMotorInA = machine.Pin(16, machine.Pin.OUT)
pinMotorInB = machine.Pin(17, machine.Pin.OUT)

while True:
	#rotate CW
	pinMotorInA.value(1)
	pinMotorInB.value(0)
	utime.sleep(1)
