import time
from gpiozero import LED

red = LED(18)

print("LED on")
red.on()
time.sleep(5)
print("LED off")
