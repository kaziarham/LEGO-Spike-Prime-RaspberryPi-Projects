from signal import pause
from buildhat import Motor, DistanceSensor

# Create a motor and distance sensor object
motor = Motor('A')
dist = DistanceSensor('D', threshold_distance=100)

'''
# Wait for the distance sensor and motor go in range
print("Wait for in range")
dist.wait_for_in_range(50)
motor.run_for_rotations(1)
'''

'''
# Wait for the distance sensor and motor go out of range
print("Wait for out of range")
dist.wait_for_out_of_range(100)
motor.run_for_rotations(2)
'''

# Function to print the distance that is in range
def handle_in(distance):
    print("in range", distance)

# Function to print the distance that is out of range
def handle_out(distance):
    print("out of range", distance)

dist.when_in_range = handle_in
dist.when_out_of_range = handle_out
pause()