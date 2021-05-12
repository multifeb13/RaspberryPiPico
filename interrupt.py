import machine
import utime
from machine import Pin

#SW1 : Pin=GPIO20 with pullup

def callback(pin):
	global sw_pressed
	sw_pressed = pin	#pin = "Pin(20, mode=IN, pull=PULL_UP)"

def main():
	global sw_pressed
	sw_pressed = None

	SW_PRESS_INTERVAL = 250 * 1000	#250ms
	SW_IRQ_TRIGGER    = Pin.IRQ_FALLING

	#SW1
	sw1 = Pin(20, Pin.IN, Pin.PULL_UP)
	#割り込みの設定
	sw1.irq(trigger=SW_IRQ_TRIGGER, handler=callback)

	ref_time = utime.ticks_us()
	while True:
		if sw_pressed:
			# disable IRQ until get values
			sw_state   = machine.disable_irq()
			sw_trigger = sw_pressed.irq().flags()
			time_diff  = utime.ticks_diff(utime.ticks_us(), ref_time)
			# enable IRQ
			machine.enable_irq(sw_state)

			if( time_diff > SW_PRESS_INTERVAL ):
				if sw_trigger == SW_IRQ_TRIGGER:
					if sw_pressed == sw1:
						print("sw1")
				else:
					pass
			else:
				pass			# avoid chattering

			sw_pressed = None
			ref_time = utime.ticks_us()

if __name__ == "__main__":
	main()
