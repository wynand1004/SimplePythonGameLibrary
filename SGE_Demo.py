#SGE Game Demo
from SGE import *

class Player(SGE.Sprite):
    def __init__(self, shape, color, x, y):
        SGE.Sprite.__init__(self, shape, color, x, y)
        self.speed = 3

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

# Initial Game setup
game = SGE(800, 600, "blue", "SGE Game Demo")
game.clear_terminal_screen()

# Create Sprites
# Create Player
player = Player("triangle", "red", -400, 100)

# Create orbs
for i in range(100):
    orb = Orb("circle", "yellow", 0, 0)

#Set Keyboard Bindings
game.set_keyboard_binding(SGE.KEY_UP, player.accelerate)
game.set_keyboard_binding(SGE.KEY_LEFT, player.rotate_left)
game.set_keyboard_binding(SGE.KEY_RIGHT, player.rotate_right)

# For Testing
# game.print_game_info()

while True:
    game.update_screen()

    for sprite in SGE.sprites:
        # Check collisions with Orbs
        if isinstance(sprite, Orb) and sprite.state:
            if SGE.is_collision(sprite, player):
                #game.play_sound("collision.mp3")
                #sprite.goto(0, 0)
                sprite.destroy()

        # Move all sprites
        if sprite.state:
            sprite.move()

delay = input("Press Enter to Continue")
