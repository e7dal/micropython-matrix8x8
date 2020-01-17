import machine
from machine import Pin,I2C
import time


from matrix8x8 import Matrix8x8


def loop(amount=1):
    i2c = I2C(0)
    i2c = I2C(1, scl=Pin(22), sda=Pin(21), freq=400000)
    display=Matrix8x8(i2c=i2c,brightness=0)

    la=0
    while True:
        la+=1
        # test set() and clear()
        display.set(b'\xFF' * 8)
        time.sleep_ms(500)
        display.clear()
        time.sleep_ms(500)
        display.set(b'\x55\xAA' * 4)
        time.sleep_ms(500)
        display.set(b'\xAA\x55' * 4)
        time.sleep_ms(500)
        display.clear()

        # test set_row(), clear_row()
        for i in range(8):
            display.set_row(i, 0xFF)
            time.sleep_ms(100)
        for i in range(8):
            display.clear_row(i)
            time.sleep_ms(100)
        display.clear()

        # test set_column(), clear_column()
        for i in range(8):
            display.set_column(i, 0xFF)
            time.sleep_ms(100)
        for i in range(8):
            display.clear_column(i)
            time.sleep_ms(100)
        display.clear()

        # test set_pixel(), clear_pixel()
        for row in range(8):
            for column in range(8):
                display.set_pixel(row, column)
                time.sleep_ms(40)
        for row in range(8):
            for column in range(8):
                display.clear_pixel(row, column)
                time.sleep_ms(40)
        display.clear()

        # test set_brightness()
        display.set(b'\xFF' * 8)
        for i in range(16):
            display.set_brightness(i)
            time.sleep_ms(100)
        for i in range(16):
            display.set_brightness(16-i)
            time.sleep_ms(100)

        # test on(), off()
        display.set(b'\xAA' * 8)
        time.sleep_ms(500)
        display.off()
        time.sleep_ms(500)
        display.on()

        # test set_blinking()
        display.set_blinking(3)
        time.sleep_ms(5000)
        display.set_blinking(2)
        time.sleep_ms(5000)
        display.set_blinking(1)
        time.sleep_ms(5000)
        display.set_blinking(0)
        time.sleep_ms(2000)

        # test changes when display is in off state
        display.off()
        time.sleep_ms(500)
        display.set(b'\x33' * 8)
        display.set_blinking(1)
        display.on()
        time.sleep_ms(2000)
        display.set_blinking(0)
        
        if la==amount:
            break