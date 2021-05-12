# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/7
import time
from machine import Pin, PWM

pwm = [0, 0]
pwm[0] = PWM( Pin( 25 ) )
pwm[0].freq( 1000 )
pwm[1] = PWM( Pin( 16 ) )
pwm[1].freq( 1000 )
duty = 0
direction = 50

sw = Pin( 17, Pin.IN )

while True:
	duty += direction
	if duty > 65535:
		duty = 65535
		direction = -50
	elif duty < 0:
		duty = 0
		direction = 50

	if( sw.value() == 0 ):
		pwm[0].duty_u16( duty )
	else:
		pwm[1].duty_u16( duty )
	time.sleep( 0.001 )
