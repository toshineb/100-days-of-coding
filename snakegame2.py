import turtle
import random

# Game configuration
WIDTH = 600
HEIGHT = 600
FOOD_SIZE = 15
DELAY = 100
COLORS = ["cyan", "magenta", "orange", "green", "blue"]

# Direction offsets
DIRECTIONS = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

# Initialize game state
def reset_game():
    global snake, snake_direction, food_pos, score
    snake = [[0, 0], [0, 20], [0, 40]]  # Initial snake segments
    snake_direction = "up"
    food_pos = get_random_food_position()
    food.goto(food_pos)
    score = 0
    update_score()
    move_snake()

def move_snake():
    global snake_direction, score, food_pos

    # Calculate the new head position
    new_head = snake[-1].copy()
    new_head[0] += DIRECTIONS[snake_direction][0]
    new_head[1] += DIRECTIONS[snake_direction][1]

    # Check for collisions (self or boundaries)
    if new_head in snake or not (-WIDTH // 2 < new_head[0] < WIDTH // 2 and -HEIGHT // 2 < new_head[1] < HEIGHT // 2):
        game_over()
        return

    # Add the new head
    snake.append(new_head)

    # Check for food collision
    if food_collision():
        # Update the food position
        food_pos = get_random_food_position()
        food.goto(food_pos)
        score += 10
        update_score()
    else:
        # Remove the tail to maintain snake length unless food is eaten
        snake.pop(0)

    # Clear previous snake drawings
    pen.clearstamps()

    # Draw the snake
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.color(random.choice(COLORS))  # Change color for each segment
        pen.stamp()

    # Refresh the screen
    screen.update()

    # Schedule the next movement
    turtle.ontimer(move_snake, DELAY)

def food_collision():
    """Check if the snake's head is close enough to the food."""
    return get_distance(snake[-1], food_pos) < FOOD_SIZE

def get_random_food_position():
    x = random.randint(-WIDTH // 2 + FOOD_SIZE, WIDTH // 2 - FOOD_SIZE)
    y = random.randint(-HEIGHT // 2 + FOOD_SIZE, HEIGHT // 2 - FOOD_SIZE)
    return x, y

def get_distance(pos1, pos2):
    return ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5

def update_score():
    score_pen.clear()
    score_pen.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

def game_over():
    pen.clearstamps()
    pen.goto(0, 0)
    pen.color("red")
    pen.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
    pen.goto(0, -30)
    pen.write(f"Final Score: {score}", align="center", font=("Arial", 16, "normal"))
    pen.goto(0, -70)
    pen.write("Press 'R' to Restart", align="center", font=("Arial", 16, "italic"))
    screen.update()

def restart_game():
    """Restart the game when the 'R' key is pressed."""
    pen.clear()
    reset_game()

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

# Initialize screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game with Restart")
screen.bgcolor("black")
screen.tracer(0)

# Snake pen
pen = turtle.Turtle("square")
pen.penup()

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Scoreboard
score = 0
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.hideturtle()
score_pen.color("white")
score_pen.goto(0, HEIGHT // 2 - 40)

# Event listeners
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(restart_game, "r")  # Bind 'R' key to restart the game

# Start the game
reset_game()
turtle.done()

