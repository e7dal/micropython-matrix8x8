# This file is executed on every boot (including wake-boot from deepsleep)
print("starting boot.by")
import esp
import uos
import network
import webrepl
import machine
from machine import Pin,I2C
import time

esp.osdebug(None)
uos.listdir()

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("blackhole", "verysecret")

webrepl.start()

i2c = I2C(0)
i2c = I2C(1, scl=Pin(22), sda=Pin(21), freq=400000)



#from matrix8x8 import Matrix8x8
#display=Matrix8x8(i2c=i2c)
#display.set_row(2, 0xFF)      # turn on all LEDs in row 2
#display.set_column(3, 0xFF)   # turn on all LEDs in column 3
#display.set_pixel(7, 6)             # turn on LED at row 7, column 6

print("starting test features, loop once, in 3 seconds, u can CTRL-C")
time.sleep(3)

import test_features as tf
tf.loop()
#tf.loop(amount=100)


print("starting game of life, loop, in 3 seconds, u can CTRL-C")
time.sleep(3)

import game_of_life as gol
gol.loop()


