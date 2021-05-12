"""
  AE-ADT7410 Temperature sensor
    akizuki : M-06675

  I2C
    bass addr : 0x48
    scl       : GPIO13
    sda       : GPIO12

[shell]
>>> from machine import Pin, I2C
>>> i2c = I2C( 0, scl=Pin(13), sda=Pin(12) )
>>> i2c.scan()
[72]
"""
#define
I2C_ADR       = 0x48
I2C_GROUP_NUM = 0
I2C_SCL_GPIO  = 13
I2C_SDA_GPIO  = 12

from machine import Pin, I2C
import utime

i2c = I2C( I2C_GROUP_NUM, scl=Pin(I2C_SCL_GPIO), sda=Pin(I2C_SDA_GPIO) )

while True:
    data = i2c.readfrom_mem( I2C_ADR, 0x00, 2 )
    temp = (data[0] << 8 | data[1]) >> 3
    if( temp >= 4096 ):
        temp -= 8192
    temp = temp * 0.0625
    print(temp)
    
    utime.sleep(0.2)
