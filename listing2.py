import time
from gpiozero import LED

red = LED(18)

print("Blinking the LED")
while True:
    red.on()
    time.sleep(0.5)
    red.off()
    time.sleep(0.5)

print("Done")
