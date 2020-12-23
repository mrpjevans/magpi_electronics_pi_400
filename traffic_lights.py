from time import sleep
from gpiozero import LED

red = LED(18)
yellow = LED(23)
green = LED(24)

while True:
    red.on()
    sleep(5)

    yellow.on()
    sleep(1)

    red.off()
    yellow.off()
    green.on()
    sleep(5)

    green.off()
    yellow.on()
    sleep(1)

    yellow.off()
