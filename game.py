import random
from time import sleep
from gpiozero import LED, Buzzer, Button

leds = {
    "red": LED(18),
    "yellow": LED(23),
    "green": LED(34)
}
bz = Buzzer(21)
button = Button(25)

choice = "red"


def check_colour:
    if choice is not "green":
        bz.on
        sleep(0.5)
        bz.off


button.when_pressed = check_colour

while True:
    for led in leds:
        led.off()

    choice = random.choice(["red", "yellow", "green"])
    leds[choice].on()

    sleep(0.5)
