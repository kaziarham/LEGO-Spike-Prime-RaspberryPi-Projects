import time
from signal import pause
from buildhat import Motor

# Create a motor object
motor = Motor('A')
motor.set_default_speed(30)

'''
# Print the absolute position
print("Position", motor.get_aposition())
'''

'''
# Function to handle the motor
def handle_motor(speed, pos, apos):
    print("Motor", speed, pos, apos)

motor.when_rotated = handle_motor
'''

'''
# Run the motor in degrees
print("Run for degrees")
motor.run_for_degrees(360)
'''

'''
# Run the motor in seconds
print("Run for seconds")
motor.run_for_seconds(5)
'''

'''
# Run the motor in rotations
print("Run for rotations")
motor.run_for_rotations(2)
'''

# Run the motor for 3 seconds
print("Start motor")
motor.start()
time.sleep(3)
print("Stop motor")
motor.stop()

pause()