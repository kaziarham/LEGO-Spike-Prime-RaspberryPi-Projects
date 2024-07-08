'''
Pong Game
LEGO Robot Model: A game controller robot is built using the LEGO Spike Prime Kit
Link to the tutorial: https://projects.raspberrypi.org/en/projects/lego-game-controller
'''

from turtle import *
import time
from buildhat import Motor

# Create motor objects
motor_left = Motor('A')
motor_right = Motor('B')

# Set the starting score to zero
score_left = 0
score_right = 0

# Create a screen and give a title, background colour, smoother animations and coordinates
game_area = Screen()
game_area.title("PONG")
game_area.bgcolor('black')
game_area.tracer(0)
game_area.setworldcoordinates(-200, -170, 200, 170)

# Create a white ball and set it on the middle of the screen
ball = Turtle()
ball.color('white')
ball.shape('circle')
ball.penup()
ball.setpos(0, 0)

# Create a green paddle and set it on the far left of the screen
paddle_left = Turtle()
paddle_left.color('green')
paddle_left.shape('square')
paddle_left.shapesize(4, 1, 1)
paddle_left.penup()
paddle_left.setpos(-190, 0)

# Create a blue paddle and set it on the far right of the screen
paddle_right = Turtle()
paddle_right.color('blue')
paddle_right.shape('square')
paddle_right.shapesize(4, 1, 1)
paddle_right.penup()
paddle_right.setpos(190, 0)

# Display a score on the game area
writer = Turtle()
writer.hideturtle()
writer.color('grey')
writer.penup()
style = ("Courier", 30, 'bold')
writer.setposition(0, 150)
writer.write(f'{score_left} PONG {score_right}', font=style, align='center')

# Keep the ball track of its speed
ball.speed_x = 0.5
ball.speed_y = 0.5

# Keep track of the location of the paddle
pos_left = 0
pos_right = 0

# Function for the left paddle that will run when the motor encoder moves
def moved_left(motor_speed, motor_rpos, motor_apos):
    global pos_left
    pos_left = motor_apos

# Function for the right paddle that will run when the motor encoder moves
def moved_right(motor_speed, motor_rpos, motor_apos):
    global pos_right
    pos_right = motor_apos

motor_left.when_rotated = moved_left
motor_right.when_rotated = moved_right

# Update the game area to see the paddle and ball
while True:
    game_area.update()
    ball.setx(ball.xcor() + ball.speed_x)
    ball.sety(ball.ycor() + ball.speed_y)
    
    '''
    Conditional statements to make the ball bounce off the wall so speed can be reversed and
    the ball travels in the opposite direction.
    
    Conditions for making the ball bounce off the wall:
    1) y position is greater than 160 (upper y position)
    2) x position is greater than 195 (right x position)
    3) y position is less than -160 (lower y position)
    '''
    if ball.ycor() > 160:
        ball.speed_y *= -1
    if ball.xcor() > 195:
        ball.speed_x *= -1
    if ball.ycor() < -160:
        ball.speed_y *= -1
    
    # Update the paddle on the screen to the new position
    paddle_left.sety(pos_left)
    paddle_right.sety(pos_right)
    
    '''
    Check if the x position of the ball is within the horizontal area covered by the paddle.
    And check if the y position of the ball is in the vertical line where the paddle moves.
    '''
    # Left
    if (ball.xcor() < -180 and ball.xcor() > -190) and (ball.ycor() < paddle_left.ycor() + 20 and ball.ycor() > paddle_left.ycor() - 20):
        ball.setx(-180)
        ball.speed_x *= -1
    
    # Right
    if (ball.xcor() > 180 and ball.xcor() < 190) and (ball.ycor() < paddle_right.ycor() + 20 and ball.ycor() > paddle_right.ycor() - 20):
        ball.setx(180)
        ball.speed_x *= -1
    
    '''
    If the paddle fails to make a save, then the opponent gets the point and the ball resets back to the start
    '''
    # Left
    if ball.xcor() < -195:
        ball.hideturtle()
        ball.goto(0, 0)
        ball.showturtle()
        score_right += 1
        writer.clear()
        writer.write(f'{score_left} PONG {score_right}', font=style, align='center')
    
    # Right
    if ball.xcor() > 195:
        ball.hideturtle()
        ball.goto(0, 0)
        ball.showturtle()
        score_left += 1
        writer.clear()
        writer.write(f'{score_left} PONG {score_right}', font=style, align='center')