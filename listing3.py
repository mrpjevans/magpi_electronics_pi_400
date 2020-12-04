from gpiozero import LED, Button
from signal import pause

red = LED(18)
button = Button(25)

button.when_pressed = red.on
button.when_released = red.off

pause()
