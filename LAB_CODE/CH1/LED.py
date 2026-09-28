from machine import Pin
import time

led = Pin(2, Pin.OUT)
while True:
    led.value(0)
    print("===============1================")
    time.sleep(2.5)
    led.value(1)
    print("===============2================")
    time.sleep(2.5)
