# SPGL Game Demo by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.7
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
#
# How to Play
# Navigate using the arrow keys
# Green objects are worth 10 points
# Yellow objects are worth 5 points
# Red objects are worth -10 points

#Import SPGL
from SPGL import *
import random

# Create Classes
class Player(Sprite):
    def __init__(self, shape, color, x, y):
        Sprite.__init__(self, shape, color, x, y)
        self.speed = 3
        self.score = 0

    def tick(self):
        self.move()

    def move(self):
        self.fd(self.speed)

        if self.xcor() > game.SCREEN_WIDTH / 2:
            self.goto(-game.SCREEN_WIDTH / 2, self.ycor())

        if self.xcor() < -game.SCREEN_WIDTH /2 :
            self.goto(game.SCREEN_WIDTH / 2, self.ycor())

        if self.ycor() > game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)

        if self.ycor() < -game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)

    def rotate_left(self):
        self.lt(30)

    def rotate_right(self):
        self.rt(30)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1
        if self.speed < 0:
            self.speed = 0

class Orb(Sprite):
    def __init__(self, shape, color, x, y):
        Sprite.__init__(self, shape, color, x, y)
        self.speed = 2
        self.setheading(random.randint(0,360))
        self.turn = 0

    def tick(self):
        self.move()
        if random.randint(0, 100) < 5:
            self.clear()

    def move(self):
        self.rt(random.randint(-10, 10))
        self.fd(self.speed)

        if self.xcor() > game.SCREEN_WIDTH / 2:
            self.goto(-game.SCREEN_WIDTH / 2, self.ycor())

        if self.xcor() < -game.SCREEN_WIDTH / 2:
            self.goto(game.SCREEN_WIDTH / 2, self.ycor())

        if self.ycor() > game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)

        if self.ycor() < -game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)

# Initial Game setup
game = Game(800, 600, "black", "SPGL Game Demo by /u/wynand1004 AKA @TokyoEdTech", 5)

# Game attributes
game.highscore = 0

# Load high score
highscore = game.load_data("highscore")
if highscore:
    game.highscore = highscore
else:
    game.highscore = 0

# Create Sprites
# Create Player
player = Player("triangle", "white", -400, 0)

# Create Orbs
for i in range(100):
    color = random.choice(["red", "yellow", "green"])
    shape = random.choice(["circle", "square", "triangle", "arrow"])
    orb = Orb(shape, color, 0, 0)
    speed = random.randint(1, 5)
    orb.speed = speed

# Create Labels
score_label = Label("Score: 0 Highscore: {}".format(game.highscore), "white", -380, 280)

# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(KEY_UP, player.accelerate)
game.set_keyboard_binding(KEY_DOWN, player.decelerate)
game.set_keyboard_binding(KEY_LEFT, player.rotate_left)
game.set_keyboard_binding(KEY_RIGHT, player.rotate_right)
game.set_keyboard_binding(KEY_ESCAPE, game.exit)

while True:
    # Call the game tick method
    game.tick()

    # Put your game logic here
    for sprite in game.sprites:
        # Check collisions with Orbs
        if sprite.state and isinstance(sprite, Orb):
            if game.is_collision(sprite, player):
                game.play_sound("collision.wav")
                sprite.destroy()
                # Update Score
                if sprite.pencolor() == "red":
                    player.score -= 10
                if sprite.pencolor() == "green":
                    player.score += 10
                if sprite.pencolor() == "yellow":
                    player.score += 5

                # Update High Score
                if player.score > game.highscore:
                    game.highscore = player.score
                    game.save_data("highscore", game.highscore)

    # Update the Game Score, High Score, and Player Speed
    speed_string = "-" * int(player.speed)
    score_label.update("Score: {} High Score: {} Speed: {}".format(player.score, game.highscore, speed_string))

    # Show game info in terminal
    game.clear_terminal_screen()
    game.print_game_info()
