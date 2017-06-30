# Simple Game Engine Version 0.5 by @TokyoEdTech AKA /u/wynand1004
# Python 2.x and 3.x Compatible
# Built on Top of the Turtle Module
#
import os
import turtle
import time
import random
import math
import pickle

# If on Windows, import winsound or, better yet, switch to Linux!
if os.name == "nt":
    try:
        import winsound
    except:
        print ("Winsound Module Not Available")

class SGE(object):

    # Class Constants
    # Use for Keyboard Bindings
    KEY_UP = "Up"
    KEY_DOWN = "Down"
    KEY_LEFT = "Left"
    KEY_RIGHT = "Right"
    KEY_SPACE = "space"
    KEY_ESCAPE = "Escape"

    # Keep List of Sprites
    sprites = []

    def __init__(self, screen_width = 800, screen_height = 600, background_color = "white", title = "Simple Game Engine by @TokyoEdTech"):
        # Setup using Turtle module methods
        turtle.setup(width=screen_width, height=screen_height)
        turtle.bgcolor(background_color)
        turtle.title(title)
        turtle.tracer(0)
        turtle.listen() # Listen for keyboard input
        turtle.hideturtle() # Hides default turtle in Python 2.x
        turtle.penup() # Puts pen up for defaut turtle in Python 2.x
        turtle.setundobuffer(0) # Do not keep turtle history in memory

        # Game Attributes
        self.FPS = 30.0 # Lower this on slower computers or with large number of sprites
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.DATAFILE= "game.dat"

        self.title = title
        self.gravity = 0
        self.state = "showsplash"
        self.splash_time = 3

        self.time = time.time()

        # Show splash
        self.show_splash(self.splash_time)

    def tick(self):
        # Check the game state
        # showsplash, running, gameover, paused

        if self.state == "showsplash":
            self.show_splash(self.splash_time)

        elif self.state == "paused":
            pass

        elif self.state == "gameover":
            pass

        else:
            # Iterate through all sprites and call their tick method
            for sprite in SGE.sprites:
                if sprite.state:
                    sprite.tick()

        # Update the screen
        self.update_screen()

    def show_splash(self, seconds):
        # Show splash screen
        # To be implemented

        print ("SHOW SPLASH SCREEN HERE")
        self.update_screen()

        # Pause
        self.time = time.time()
        while time.time() < self.time + (self.splash_time):
            pass

        # Hide Splash
        self.clear_terminal_screen()

        # Change state to running
        self.state = "running"

    def hide_all_sprites(self):
        for sprite in SGE.sprites:
            if sprite.state:
                sprite.destroy()

    def save_data(self, key, value):
        # Load DATAFILE
        try:
            data = pickle.load(open(self.DATAFILE, "rb"))
        except:
            data = {}

        data[key] = value

        #Save DATAFILE
        pickle.dump(data, open(self.DATAFILE, "wb"))

    def load_data(self):
        # Load DATAFILE
        try:
            data = pickle.load(open(self.DATAFILE, "rb"))
        except:
            data = {}

        return data

    def set_title(self, title):
        turtle.title(title)
        self.title = title

    def set_keyboard_binding(self, key, function):
        turtle.onkey(function, key)

    def set_score(self, score):
        self.score = score

    def update_screen(self):
        while time.time() < self.time + (1.0 / self.FPS):
            pass
        turtle.update()
        self.time = time.time()


    def play_sound(self, sound_file):
        # Windows
        if os.name == 'nt':
            winsound.play(sound_file, winsound.SND_ASYNC)
        # Linux
        elif os.name == "posix":
            os.system("aplay -q {}&".format(sound_file))
        # Mac
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

    def is_collision(self, sprite_1, sprite_2):
        x_collision = (math.fabs(sprite_1.xcor() - sprite_2.xcor()) * 2) < (sprite_1.width + sprite_2.width)
        y_collision = (math.fabs(sprite_1.ycor() - sprite_2.ycor()) * 2) < (sprite_1.height + sprite_2.height)
        return (x_collision and y_collision)

    def show_game_over(self):
        self.state = "gameover"
        self.hide_all_sprites()
        print ("Game Over!")
        self.state = "paused"

    def exit(self):
        self.stop_all_sounds()
        os._exit(0)

    class Sprite(turtle.Turtle):
        def __init__(self, shape, color, x = 0, y = 0):
            turtle.Turtle.__init__(self)
            self.speed(0) # Animation Speed
            self.shape(shape)
            self.color(color)
            self.penup()
            self.goto(x, y)
            self.dx = 0.0
            self.dy = 0.0
            self.speed = 0.0 # Speed of motion
            self.acceleration = 0.0
            self.width = 20.0
            self.height = 20.0
            self.state = "active"
            self.friction = 0.0
            self.solid = True
            SGE.sprites.append(self)

        def tick(self):
            # This is the function that is called each frame of the game
            # For most sprites, you'll want to call the move method here
            pass

        def move(self):
            self.fd(self.speed)

        def destroy(self):
            # When a sprite is destoyed move it off screen, hide it, and set state to None
            # This is a workaround as there is no way to delete a sprite from memory in the turtle module.
            self.hideturtle()
            self.goto(10000, 10000)
            self.state = None

        def set_image(self, image, width, height):
            # Allows the use of custom images (must be .gif) due to turtle/tkinter limitation
            turtle.register_shape(image)
            self.shape(image)
            self.width = width
            self.height = height

    class Label(turtle.Turtle):
        def __init__(self, text, color, x = 0, y = 0):
            turtle.Turtle.__init__(self)
            self.hideturtle()
            self.penup()
            self.goto(x, y)
            self.color(color)
            if text != "":
                self.write(text)

        def update(self, text):
            self.clear()
            self.write(text)
