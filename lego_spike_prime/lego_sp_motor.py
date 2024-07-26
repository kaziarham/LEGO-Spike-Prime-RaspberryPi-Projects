from signal import pause
from buildhat import Motor
import time

# Create motor objects
motor = Motor('A')
motorb = Motor('B')

'''
# Function to handle the motor when rotating it
def handle_motor(speed, pos, apos):
    print("Motor", speed, pos, apos)

motor.when_rotated = handle_motor
motor.set_default_speed(50)
'''

# Run the motor for 360 degrees
print("Run for 360 degrees")
motor.run_for_degrees(360)
time.sleep(3)

# Run the motor for -360 degrees
print("Run for -360 degrees")
motor.run_for_degrees(-360)
time.sleep(3)

# Start the motor for 3 seconds and stop the motor for 1 second
print("Start motor")
motor.start()
time.sleep(3)
print("Stop motor")
motor.stop()
time.sleep(1)

# Run the motor for 180 degrees
print("Run for 180 degrees")
motor.run_for_degrees(180)
time.sleep(3)

# Run the motor for 90 degrees
print("Run for 90 degrees")
motor.run_for_degrees(90)
time.sleep(3)

# Run the motor for 2 rotations
print("Run for 2 rotations")
motor.run_for_rotations(2)
time.sleep(3)

# Run the motor for 5 seconds
print("Run for 5 seconds")
motor.run_for_seconds(5)
time.sleep(3)

# Run both motors for 5 seconds
print("Run both")
motor.run_for_seconds(5, blocking=False)
motorb.run_for_seconds(5, blocking=False)
time.sleep(10)

# Run the motor to position -90
print("Run to position -90")
motor.run_to_position(-90)
time.sleep(3)

# Run the motor to position 90
print("Run to position 90")
motor.run_to_position(90)
time.sleep(3)

# Run the motor to position 180
print("Run to position 180")
motor.run_to_position(180)
time.sleep(3)