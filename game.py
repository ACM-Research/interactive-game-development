from tkinter import *
import time
import random
import cv2
from roboflow import Roboflow
rf = Roboflow(api_key="JET4t6r3qd9gLBStSbAm")
project = rf.workspace().project("hand-game-controls")
model = project.version(9).model

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
DELAY = 700  # in ms
SPACE_SIZE = 50
INITIAL_SNAKE_SIZE = 1
SNAKE_COLOR = "#00ff00"
FOOD_COLOR = "#ff0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self) -> None:
        self.body_size = INITIAL_SNAKE_SIZE
        self.coordinates = []
        self.squares = []

        for _ in range(0, INITIAL_SNAKE_SIZE):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self) -> None:
        # pick random spot on board, if snake is there, pick a different spot
        space_is_valid = False
        while not space_is_valid:
            space_is_valid = True
            food_x = random.randint(0, int(WINDOW_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
            food_y = random.randint(0, int(WINDOW_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
            for x, y in snake.coordinates:
                if food_x == x and food_y == y:
                    space_is_valid = False
                    # break
            if space_is_valid:
                self.coordinates = [food_x, food_y]
                canvas.create_rectangle(
                    food_x,
                    food_y,
                    food_x + SPACE_SIZE,
                    food_y + SPACE_SIZE,
                    fill=FOOD_COLOR,
                    tags="food",
                )


def next_turn(snake: Snake, food: Food) -> None:
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake"
    )
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="score: {}".format(score))
        canvas.delete("food")
        if (
            snake.body_size
            < (WINDOW_HEIGHT / SPACE_SIZE) * (WINDOW_WIDTH / SPACE_SIZE) - 1
        ):
            food = Food()
            snake.body_size += 1
        else:
            game_over()
            return
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()
        return

    window.after(DELAY, next_turn, snake, food)


def change_direction(new_direction) -> None:
    global last_input_time
    global direction
    input_time = time.time()
    # limit input rate so you can't do a 180
    if input_time - last_input_time >= DELAY * 0.25 / 1000:
        if new_direction == "left":
            if direction != "right" and direction != "left":
                direction = new_direction
                last_input_time = input_time

        elif new_direction == "right":
            if direction != "left" and direction != "right":
                direction = new_direction
                last_input_time = input_time

        elif new_direction == "up":
            if direction != "down" and direction != "up":
                direction = new_direction
                last_input_time = input_time

        elif new_direction == "down":
            if direction != "up" and direction != "down":
                direction = new_direction
                last_input_time = input_time


def check_collision(snake: Snake) -> bool:
    x, y = snake.coordinates[0]

    # check colision with window borders
    if x < 0 or x >= WINDOW_WIDTH:
        return True
    if y < 0 or y >= WINDOW_HEIGHT:
        return True

    # check colision with body
    for part in snake.coordinates[1:]:
        if x == part[0] and y == part[1]:
            return True

    return False


def game_over() -> None:
    canvas.delete(ALL)
    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2,
        font=("consolas", 70),
        text="GAME OVER",
        fill="#0000ff",
        tags="game over",
    )

def use_camera():
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    frame = frame[180:450, 50:370]
    cv2.imshow('Input', frame)
    
    prediction_result = model.predict(frame, confidence=30, overlap=30).json()
    
    prediction_list = prediction_result["predictions"]
    
    try:
        first_prediction_json = prediction_list[0]
    except IndexError:
        pass
    else:
        predicted_direction = first_prediction_json["class"]
        print(predicted_direction)
        change_direction(predicted_direction)
        prediction_list = []
    finally:
        window.after(10, use_camera)

window = Tk()

window.title("snake")
window.resizable(False, False)

score = 0
direction = "down"
label = Label(window, text="score: {}".format(score), font=("consolas", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
canvas.pack()

cap = cv2.VideoCapture(0)

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

snake = Snake()
food = Food()

next_turn(snake, food)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
last_input_time = time.time()

use_camera()

#window.bind("<Left>", lambda event: change_direction("left"))
#window.bind("<Right>", lambda event: change_direction("right"))
#window.bind("<Up>", lambda event: change_direction("up"))
#window.bind("<Down>", lambda event: change_direction("down"))

#window.bind("a", lambda _: change_direction("left"))
#window.bind("d", lambda _: change_direction("right"))
#window.bind("w", lambda _: change_direction("up"))
#window.bind("s", lambda _: change_direction("down"))

window.mainloop()
