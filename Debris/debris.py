# Debris by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
#
# How to Play
# Navigate using the arrow keys
# Shoot your missile using the space bar
# Use the ESC key to end the game

# The object of the game is to shoot as many objects as possible for points.
# Colliding with an object results in points lost

# Green objects are worth +10 / -10 points
# Yellow objects are worth +5 / -5 points
# Red objects are worth +20 / -20 points

# Sound effects courtesy of http://www.freesfx.co.uk

#Import SPGL
import spgl
import random
import math

# Create Classes
class Player(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 3
        self.score = 0
        self.thrust = 1
        self.dx = 0
        self.dy = 0
        self.rotation_speed = 0

    def tick(self):
        self.move()

    def move(self):
        player.goto(player.xcor()+self.dx, player.ycor()+self.dy)

        if self.xcor() > game.SCREEN_WIDTH / 2:
            self.goto(-game.SCREEN_WIDTH / 2, self.ycor())

        if self.xcor() < -game.SCREEN_WIDTH /2 :
            self.goto(game.SCREEN_WIDTH / 2, self.ycor())

        if self.ycor() > game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)

        if self.ycor() < -game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)

    def rotate_left(self):
        self.rotation_speed = 30
        h = self.heading() + self.rotation_speed
        player.setheading(h)

    def rotate_right(self):
        self.rotation_speed = -30
        h = self.heading() + self.rotation_speed
        player.setheading(h)

    def accelerate(self):
        h = player.heading()
        self.dx += math.cos(h*math.pi/180)*self.thrust
        self.dy += math.sin(h*math.pi/180)*self.thrust

class Orb(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
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

class Particle(spgl.Sprite):
    def __init__(self, spriteshape, color):
        spgl.Sprite.__init__(self, shape, color, 1000, 1000)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000,-1000)
        self.frame = 0.0
        self.max_frame = random.randint(5, 20)
        self.state = "ready"

    def tick(self):
        if self.frame != 0:
            self.fd(self.myspeed)
            self.frame += 1

        if self.frame > self.max_frame:
            self.goto(1000, 1000)
            self.frame = 0
            self.state = "ready"

    def explode(self, startx, starty):
        if self.state == "ready":
            self.goto(startx,starty)
            self.setheading(random.randint(0,360))
            self.frame = 1.0
            self.myspeed = random.randint(3, 10)
            self.state = "exploding"

class Explosion(object):
    def __init__(self):
        self.particles = []
        for _ in range(30):
            color = random.choice(["red", "yellow", "orange"])
            self.particles.append(Particle("circle", color))

    def explode(self, x, y):
        for particle in self.particles:
            particle.explode(x, y)

class Missile(spgl.Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        spgl.Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)
        
    def fire(self):
        if self.status == "ready":
            game.play_sound("fire_missile.wav")
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
            
    def tick(self):
        if self.status == "ready":
            self.goto(-1000, 1000)
        
        elif self.status == "firing":
            self.fd(self.speed)    
            
        #Border check
        if self.xcor() < -game.SCREEN_WIDTH / 2 or self.xcor() > game.SCREEN_WIDTH / 2 or \
            self.ycor()< -game.SCREEN_HEIGHT / 2 or self.ycor()> game.SCREEN_HEIGHT / 2:
            self.goto(-1000,1000)
            self.status = "ready"

# Initial Game setup
game = spgl.Game(800, 600, "black", "Debris (SPGL Demo) by @TokyoEdTech", 5)

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
for i in range(75):
    color = random.choice(["red", "yellow", "green"])
    shape = random.choice(["circle", "square", "triangle", "arrow"])
    orb = Orb(shape, color, 0, 0)
    speed = random.randint(1, 5)
    orb.speed = speed

# Create Explosion
explosion = Explosion()

# Create Missile
missile = Missile("triangle", "white", 1000, 1000)

# Create Labels
score_label = spgl.Label("Score: 0 Highscore: {}".format(game.highscore), "white", -380, 280)

# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.accelerate)
game.set_keyboard_binding(spgl.KEY_LEFT, player.rotate_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.rotate_right)
game.set_keyboard_binding(spgl.KEY_SPACE, missile.fire)
game.set_keyboard_binding(spgl.KEY_ESCAPE, game.exit)

# Set background image
game.set_background("starfield.gif")

while True:
    # Call the game tick method
    game.tick()

    # Put your game logic here
    for sprite in game.sprites:
        # Check collisions with Orbs
        if sprite.state and isinstance(sprite, Orb):
            
            # Collision with the missile
            if game.is_collision(sprite, missile):
                game.play_sound("missile_collides.wav")
                
                middle_x = (sprite.xcor() + missile.xcor()) / 2
                middle_y = (sprite.ycor() + missile.ycor()) / 2

                explosion.explode(middle_x, middle_y)
                sprite.destroy()
                missile.goto(1000, 1000)
                missile.status = "ready"

                # Update Score
                if sprite.pencolor() == "red":
                    player.score += 20
                if sprite.pencolor() == "green":
                    player.score += 10
                if sprite.pencolor() == "yellow":
                    player.score += 5

            # Collision with the player
            if game.is_collision(sprite, player):
                game.play_sound("player_collides.wav")
                
                middle_x = (sprite.xcor() + player.xcor()) / 2
                middle_y = (sprite.ycor() + player.ycor()) / 2

                explosion.explode(middle_x, middle_y)
                sprite.destroy()
                
                # Update Score
                if sprite.pencolor() == "red":
                    player.score -= 20
                if sprite.pencolor() == "green":
                    player.score -= 10
                if sprite.pencolor() == "yellow":
                    player.score -= 5

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
