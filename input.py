import time
from machine import Pin

sw = Pin( 17, Pin.IN )

while True:
	print( sw.value() )
	time.sleep( 0.5 )