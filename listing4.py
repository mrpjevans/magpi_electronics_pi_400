from gpiozero import Buzzer, Button
from signal import pause

bz = Buzzer(21)
button = Button(25)

button.when_pressed = bz.on
button.when_released = bz.off

pause()
