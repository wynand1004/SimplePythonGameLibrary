# SGE Space Invaders by @TokyoEdTech AKA /u/wynand1004

# Import SGE (Version 0.4)
from SGE import *

# Create Classes
class Player(SGE.Sprite):
    def __init__(self, shape, color, x, y):
        SGE.Sprite.__init__(self, shape, color, x, y)
        self.speed = 5
        self.setheading(90)
        self.score = 0

    def tick(self):
        self.move()

    def move(self):
        self.setx(self.xcor() + self.dx)

        if self.xcor() > game.SCREEN_WIDTH / 2:
            self.goto(game.SCREEN_WIDTH / 2, self.ycor())
            self.dx = 0

        if self.xcor() < -game.SCREEN_WIDTH /2 :
            self.goto(-game.SCREEN_WIDTH / 2, self.ycor())
            self.dx = 0

    def move_left(self):
        self.dx = -self.speed

    def move_right(self):
        self.dx = self.speed

class Invader(SGE.Sprite):
    def __init__(self, shape, color, x, y):
        SGE.Sprite.__init__(self, shape, color, x, y)
        self.speed = 3
        self.setheading(90)
        self.dx = self.speed

    def tick(self):
        self.move()

    def move(self):
        self.setx(self.xcor() + self.dx)

        if self.xcor() > game.SCREEN_WIDTH / 2:
            self.goto(self.xcor(), self.ycor() - 35)
            self.dx = -self.speed

        if self.xcor() < -game.SCREEN_WIDTH / 2 :
            self.goto(self.xcor(), self.ycor() - 35)
            self.dx = self.speed

class Missile(SGE.Sprite):
    def __init__(self, shape, color, x, y):
        SGE.Sprite.__init__(self, shape, color, x, y)
        self.speed = 20
        self.setheading(90)
        self.state = "ready"
        self.goto(10000, 10000)

    def tick(self):
        self.move()

    def move(self):
        if self.state == "firing":
            self.fd(self.speed)

            # Boundary checking
            if self.ycor() > game.SCREEN_HEIGHT / 2:
                self.hide()

    def fire(self):
        if self.state == "ready":
            self.goto(player.xcor(), player.ycor() + 10)
            self.state = "firing"

    def hide(self):
        self.goto(10000, 10000)
        self.state = "ready"

# Initial Game setup
game = SGE(800, 600, "black", "SGE Space Invaders Example by @TokyoEdTech AKA /u/wynand1004")

# Create Sprites
# Create Player
player = Player("triangle", "white", 0, -280)
missile = Missile("triangle", "yellow", 10000, 10000)

# Create Labels
score_label = SGE.Label("Score: 0", "white", -380, 280)

# Create Invaders (3 rows of 9)
for row in range(1):
    for column in range(9):
        x = -300 + (column * 75)
        y = 275 - (row * 75)
        invader = Invader("square", "red", x, y)

# Set Keyboard Bindings
game.set_keyboard_binding(SGE.KEY_LEFT, player.move_left)
game.set_keyboard_binding(SGE.KEY_RIGHT, player.move_right)
game.set_keyboard_binding(SGE.KEY_SPACE, missile.fire)
game.set_keyboard_binding(SGE.KEY_ESCAPE, game.exit)

while True:
    # Call the game tick method
    game.tick()

    # Check collisions with missile
    # Iterate through all sprites
    # Keep track of current number of invaders

    invader_count = 0

    for sprite in SGE.sprites:
        # Check if the sprite is active and an invader
        if sprite.state and isinstance(sprite, Invader):
            invader_count += 1
            # Check for invader collision with missile
            if game.is_collision(sprite, missile):
                sprite.destroy()
                missile.hide()
                player.score += 10

            # Check if an invader has gotten below a certain point
            if sprite.ycor() < -250:
                game.show_game_over()

    # Show Score and Invader Count
    score_label.update("Score: {} Invaders: {}".format(player.score, invader_count))

    if invader_count == 0:
        game.show_game_over()
