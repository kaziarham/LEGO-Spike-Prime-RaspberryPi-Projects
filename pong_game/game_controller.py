from buildhat import Motor
from signal import pause

'''
Game Controller Robot - A game controller robot is built using the LEGO Spike Prime Kit
Link to the tutorial: https://projects.raspberrypi.org/en/projects/lego-game-controller
'''

# Create motor object
motor_left =  Motor('A')

'''
# Print the absolute position of the motor
print(motor_left.get_aposition())

# Print the relative position of the motor
print(motor_left.get_position())
'''

'''
# Loop to constantly read the motor's absolute position
while True:
    print(motor_left.get_aposition())
'''


# Function to print the absolute position of the motor
def moved_left(motor_speed, motor_pos, motor_apos):
    print(motor_apos)

motor_left.when_rotated = moved_left
pause()