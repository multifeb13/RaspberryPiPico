# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/7
import time
from machine import Pin, PWM

pwm = PWM( Pin( 25 ) )
pwm.freq( 1000 )
duty = 0
direction = 50

while True:
	duty += direction
	if duty > 65535:
		duty = 65535
		direction = -50
	elif duty < 0:
		duty = 0
		direction = 50

	pwm.duty_u16( duty )
	time.sleep( 0.001 )
