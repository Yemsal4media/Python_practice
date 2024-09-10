import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Snakes and Ladders Adventure")
wn.bgcolor("white")

# Draw the board
board = turtle.Turtle()
board.speed(0)
board.penup()

# Function to draw squares for the board
def draw_square(color, x, y):
    board.color(color)
    board.goto(x, y)
    board.begin_fill()
    for _ in range(4):
        board.forward(50)
        board.left(90)
    board.end_fill()

# Draw the board with alternating colors
colors = ["lightblue", "lightgreen"]
for y in range(0, 500, 50):
    for x in range(0, 500, 50):
        draw_square(colors[(x+y)//50 % 2], x, y)

board.hideturtle()

# Player turtles
player1 = turtle.Turtle()
player1.color("red")
player1.shape("circle")
player1.penup()

player2 = turtle.Turtle()
player2.color("blue")
player2.shape("circle")
player2.penup()

# ... (rest of the game logic goes here)

# To keep the window open
turtle.mainloop()
