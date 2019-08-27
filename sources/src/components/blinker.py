import sys, time
from machine import Pin

print('LOAD: blinker.py')


def blink_connected_to_wifi(pin=23):
    _blink_pattern(pin, [[3, 0.5, 0.5], [4, 0.2, 0.2]])


def blink_not_connected_to_wifi(pin=23):
    _blink_pattern(pin, [[2, 0.2, 0.2], [1, 0.5, 0.5], [2, 0.2, 0.2], [1, 0.5, 0.5]])

# pin - the pin, connected to LED
# pattern - the array of items: [blink_count, on-period, off-period]
def _blink_pattern(pin, pattern):
    p = Pin(pin, Pin.OUT)
    try:
        for item in pattern:
            for j in range(item[0]):
                p.value(1)
                time.sleep(item[1])
                p.value(0)
                time.sleep(item[2])
    except:
        p.value(0)
        Pin(pin, Pin.IN)
