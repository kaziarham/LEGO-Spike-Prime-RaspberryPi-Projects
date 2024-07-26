from signal import pause
from buildhat import Motor, ForceSensor

# Create a motor and force sensor object
motor = Motor('A')
button = ForceSensor('D', threshold_force=1)

'''
# Press the button fully and release it and make the motor run for 1 rotation
print("Waiting for button to be pressed fully and released")

button.wait_until_pressed(100)
button.wait_until_released(0)

motor.run_for_rotations(1)
'''

'''
# Press the button and make the motor run for 2 rotations
print("Wait for button to be pressed")

button.wait_until_pressed()
motor.run_for_rotations(2)
'''

# Function to print when the button is pressed
def handle_pressed(force):
    print("pressed", force)

# Function to print when the button is released
def handle_released(force):
    print("released", force)

button.when_pressed = handle_pressed
button.when_released = handle_released
pause()