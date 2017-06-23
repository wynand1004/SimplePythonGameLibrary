# Simple Game Engine by @TokyoEdTech
# Python 3
# Built on Top of the Turtle Module
import os
import turtle
import time
import random
import math

# If on Windows, import winsound
if os.name == "nt":
    try:
        import winsound
    except:
        print ("Winsound Module Not Available")

class SGE(object):
    # Class Constants Python 2
    KEY_UP = "up"
    KEY_DOWN = "down"
    KEY_LEFT = "left"
    KEY_RIGHT = "right"
    KEY_SPACE = "space"

    # Class Constants Python 3
    KEY_UP = "Up"
    KEY_DOWN = "Down"
    KEY_LEFT = "Left"
    KEY_RIGHT = "Right"
    KEY_SPACE = "space"

    # Keep List of Sprites
    sprites = []

    def __init__(self, screen_width = 800, screen_height = 600, background_color = "white", title = "Simple Game Engine by @TokyoEdTech"):
        turtle.setup(width=screen_width, height=screen_height)
        turtle.bgcolor(background_color)
        turtle.title(title)
        turtle.tracer(0)
        turtle.listen()
        self.title = title
        self.gravity = 0
        self.state = None
        self.FPS = 30.0
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.time = time.time()

    def set_title(self, title):
        turtle.title(title)
        self.title = title

    def set_keyboard_binding(self, key, function):
        turtle.onkey(function, key)

    def set_score(self, score):
        self.score = score

    def update_screen(self):
        while time.time() < self.time + (1.0/self.FPS):
            pass
        self.time = time.time()
        turtle.update()

    def play_sound(self, sound_file):
        # Windows
        if os.name == 'nt':
            winsound.play(sound_file, winsound.SND_ASYNC)
        #Linux
        elif os.name == "posix":
            os.system("aplay {}&".format(sound_file))
        #Mac
        else:
            os.system("afplay {}&".format(sound_file))

    def stop_all_sounds(self):
        # Windows
        if os.name == 'nt':
            print ("Sorry, not implemented...yet...LINUX RULES!")
        # Linux
        elif os.name == "posix":
            os.system("killall aplay")
        # Mac
        else:
            os.system("killall afplay")

    def clear_terminal_screen(self):
        # Windows
    	if os.name == 'nt':
    		os.system("cls")
        # Linux and Mac
    	else:
    		os.system("clear")

    def print_game_info(self):
        print (self.title)
        print ("Window Dimensions: {}x{}".format(self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        print ("Number of Registered Sprites: {}".format(len(SGE.sprites)))
        print ("Frames Per Second: {}".format(self.FPS))

    def is_collision(sprite_1, sprite_2):
        x_collision = (math.fabs(sprite_1.xcor() - sprite_2.xcor()) * 2) < (sprite_1.width + sprite_2.width)
        y_collision = (math.fabs(sprite_1.ycor() - sprite_2.ycor()) * 2) < (sprite_1.height + sprite_2.height)
        return (x_collision and y_collision)

    class Sprite(turtle.Turtle):
        def __init__(self, shape, color, x = 0, y = 0):
            turtle.Turtle.__init__(self)
            self.speed(0) #Animation Speed
            self.shape(shape)
            self.color(color)
            self.penup()
            self.goto(x, y)
            self.dx = 0.0
            self.dy = 0.0
            self.speed = 0.0 #Speed of motion
            self.acceleration = 0.0
            self.width = 20.0
            self.height = 20.0
            self.state = "active"
            self.friction = 0.0
            self.solid = True
            SGE.sprites.append(self)

        def move(self):
            self.fd(self.speed)

        def destroy(self):
            self.hideturtle()
            self.goto(10000, 10000)
            self.state = None

        def set_image(self, image, width, height):
            turtle.register_shape(image)
            self.shape(image)
            self.width = width
            self.height = height
