# SGE Game Demo by @TokyoEdTech AKA /u/wynand1004
from SGE import *

# Create Classes
class Player(SGE.Sprite):
    def __init__(self, shape, color, x, y):
        SGE.Sprite.__init__(self, shape, color, x, y)
        self.speed = 3

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
        self.speed += 0.5

class Orb(SGE.Sprite):
    def __init__(self, shape, color, x, y):
        SGE.Sprite.__init__(self, shape, color, x, y)
        self.speed = 2
        self.setheading(random.randint(0,360))

    def tick(self):
        self.move()

    def move(self):
        self.fd(self.speed)

        if self.xcor() > game.SCREEN_WIDTH / 2:
            self.goto(-game.SCREEN_WIDTH / 2, self.ycor())

        if self.xcor() < -game.SCREEN_WIDTH / 2 :
            self.goto(game.SCREEN_WIDTH / 2, self.ycor())

        if self.ycor() > game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)

        if self.ycor() < -game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)

# Initial Game setup
game = SGE(800, 600, "blue", "SGE Game Demo by @TokyoEdTech AKA /u/wynand1004")
game.clear_terminal_screen()

# Create Sprites
# Create Player
player = Player("triangle", "red", -400, 0)

# Create Orbs
for i in range(100):
    orb = Orb("circle", "yellow", 0, 0)

# Set Keyboard Bindings
game.set_keyboard_binding(SGE.KEY_UP, player.accelerate)
game.set_keyboard_binding(SGE.KEY_LEFT, player.rotate_left)
game.set_keyboard_binding(SGE.KEY_RIGHT, player.rotate_right)

while True:
    # Call the game tick method
    game.tick()

    # Put your game logic here
    for sprite in SGE.sprites:
        # Check collisions with Orbs
        if sprite.state and isinstance(sprite, Orb) :
            if game.is_collision(sprite, player):
                # game.play_sound("collision.mp3")
                sprite.destroy()
