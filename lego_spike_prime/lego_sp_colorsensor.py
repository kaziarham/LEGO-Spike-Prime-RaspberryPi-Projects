from buildhat import ColorSensor

# Create a color sensor object
color = ColorSensor('C')

'''
# Print the different colour values
print("HSV:", color.get_color_hsv())
print("RGBI:", color.get_color_rgbi())
print("Ambient:", color.get_ambient_light())
print("Reflected:", color.get_reflected_light())
print("Colour:", color.get_color())
'''

'''
# Detect the colour 'black'
print("Waiting for colour black")
color.wait_until_color("black")
print("Found colour black")
'''

'''
# Detect the colour 'white'
print("Waiting for colour white")
color.wait_until_color("white")
print("Found colour white")
'''

# Loop to detect a new colour
while True:
    c = color.wait_for_new_color()
    print("Found new color", c)