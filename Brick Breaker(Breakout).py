import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Brick Breaker")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle setup
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball setup
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -200)
ball.dx = 3
ball.dy = -3

# Brick setup
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
brick_rows = 5
brick_cols = 10

for row in range(brick_rows):
    for col in range(brick_cols):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[row % len(colors)])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        x = -350 + (col * 75)
        y = 250 - (row * 30)
        brick.goto(x, y)
        bricks.append(brick)

# Score setup
score = 0
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.hideturtle()
score_pen.color("white")
score_pen.goto(0, 260)
score_pen.write(f"Score: {score}", align="center", font=("Arial", 18, "normal"))

# Paddle movement
def paddle_left():
    x = paddle.xcor() - 30
    if x < -370:
        x = -370
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor() + 30
    if x > 370:
        x = 370
    paddle.setx(x)

screen.listen()
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(paddle_right, "Right")

# Game loop
def game_loop():
    global score
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball collision with walls
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    # Ball collision with paddle
    if (ball.ycor() < -240 and
        ball.xcor() > paddle.xcor() - 50 and
        ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Ball collision with bricks
    for brick in bricks:
        if brick.isvisible() and abs(ball.xcor() - brick.xcor()) < 40 and abs(ball.ycor() - brick.ycor()) < 20:
            brick.hideturtle()
            ball.dy *= -1
            score += 10
            score_pen.clear()
            score_pen.write(f"Score: {score}", align="center", font=("Arial", 18, "normal"))
            break

    # Game over condition
    if ball.ycor() < -300:
        score_pen.clear()
        score_pen.goto(0, 0)
        score_pen.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        return

    screen.update()
    screen.ontimer(game_loop, 20)

# Start the game
game_loop()
screen.mainloop()
