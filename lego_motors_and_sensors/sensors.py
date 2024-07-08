from signal import pause
from buildhat import ForceSensor, ColorSensor

button = ForceSensor('C')
cs = ColorSensor('B')

# Function to turn the colour sensor on when pressing the Force sensor plunger
def handle_pressed(force):
    cs.on()
    print(cs.get_color())

# Function to turn the colour sensor off when releasing the Force sensor plunger
def handle_released(force):
    cs.off()

button.when_pressed = handle_pressed
button.when_released = handle_released
pause()