from buildhat import MotorPair

# Create a motor pair object and run for 2 rotations
pair = MotorPair('C', 'D')
pair.set_default_speed(20)
pair.run_for_rotations(2)

'''
Run the motor pair for 1 rotation
Make the speed of the left motor 100 and right motor 20
'''
pair.run_for_rotations(1, speedl=100, speedr=20)

'''
Run the left motor to position 20 and right motor to position 100
Make the speed of both motors to 20
'''
pair.run_to_position(20, 100, speed=20)