# Simple Python Game Library Version 0.6 by /u/wynand1004 AKA @TokyoEdTech
# Documentation on Github: https://wynand1004.github.io/SPGL
# Python 2.x and 3.x Compatible

import os
import turtle
import time
import random
import math
import pickle

# Import message box
# This code is necessary for Python 2.x and 3.x compatibility
try:
    import tkMessageBox as messagebox
except:
    from tkinter import messagebox

# If on Windows, import winsound or, better yet, switch to Linux!
if os.name == "nt":
    try:
        import winsound
    except:
        print ("Winsound module not available.")

# SPGL Class
class SPGL(object):

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

    # Keep List of Labels
    labels = []

    # Keep List of Buttons
    buttons = []

    # Logs
    logs = []

    def __init__(
                self,
                screen_width = 800,
                screen_height = 600,
                background_color = "black",
                title = "Simple Game Engine by /u/wynand1004 AKA @TokyoEdTech",
                splash_time = 3):

        # Setup using Turtle module methods
        turtle.setup(width=screen_width, height=screen_height)
        turtle.bgcolor(background_color)
        turtle.title(title)
        turtle.tracer(0) # Stop automatic screen refresh
        turtle.listen() # Listen for keyboard input
        turtle.hideturtle() # Hides default turtle
        turtle.penup() # Puts pen up for defaut turtle
        turtle.setundobuffer(0) # Do not keep turtle history in memory
        turtle.onscreenclick(self.click)

        # Game Attributes
        self.FPS = 30.0 # Lower this on slower computers or with large number of sprites
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.DATAFILE = "game.dat"
        self.SPLASHFILE = "splash.gif" # Must be in the same folder as game file

        self.title = title
        self.gravity = 0
        self.state = "showsplash"
        self.splash_time = splash_time

        self.time = time.time()

        # Clear the terminal and print the game title
        self.clear_terminal_screen()
        print (self.title)

        # Show splash
        self.show_splash(self.splash_time)

    # Pop ups
    def ask_yes_no(self, title, message):
        return messagebox.askyesno(title, message)

    def show_info(self, title, message):
        return messagebox.showinfo(title, message)

    def show_warning(self, title, message):
        return messagebox.showwarning(title, message)

    def print_error_logs(self):
        print ("Error Logs:")
        for error in SPGL.logs:
            print (error)

        if len(SPGL.logs) == 0:
            print ("No errors")
        print ("")

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
            for sprite in SPGL.sprites:
                if sprite.state:
                    sprite.tick()

            # Iterate through all labels and call their update method
            for label in SPGL.labels:
                if label.text != "":
                    label.tick()

        # Update the screen
        self.update_screen()

    def click(self, x, y):
        print ("The window was clicked at ({},{})".format(x, y))

    def show_splash(self, seconds):
        # Show splash screen
        # To be implemented

        try:
            # Load self.SPLASHFILE
            turtle.bgpic(self.SPLASHFILE)

            self.update_screen()

            # Pause
            self.time = time.time()
            while time.time() < self.time + (self.splash_time):
                pass

            # Hide Splash
            turtle.bgpic("")

        except:
            SPGL.logs.append("Warning: {} missing from disk.".format(self.SPLASHFILE))

        # Change state to running
        self.state = "running"

    def destroy_all_sprites(self):
        for sprite in SPGL.sprites:
            if sprite.state:
                sprite.destroy()

    def save_data(self, key, value):
        # Load DATAFILE
        try:
            data = pickle.load(open(self.DATAFILE, "rb"))
        except:
            data = {}
            SPGL.logs.append("Warning: Creating new {} file on disk.".format(self.DATAFILE))

        data[key] = value

        #Save DATAFILE
        pickle.dump(data, open(self.DATAFILE, "wb"))

    def load_data(self, key):
        # Load DATAFILE
        try:
            data = pickle.load(open(self.DATAFILE, "rb"))
        except:
            data = {}
            SPGL.logs.append("Warning: {} missing from disk.".format(self.DATAFILE))

        if key in data:
            return data[key]
        else:
            return None

    def set_title(self, title):
        turtle.title(title)
        self.title = title

    def set_keyboard_binding(self, key, function):
        turtle.onkey(function, key)

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
            SPGL.logs.append("Warning: .stop_all_sounds not implemened on Windows yet.")
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
        print ("")
        print ("Window Dimensions: {}x{}".format(self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        print ("")

        # Calcuate number of active sprites
        active_sprites = 0
        for sprite in SPGL.sprites:
            if sprite.state:
                active_sprites += 1

        print ("Number of Sprites (Active / Total): {} / {}".format(active_sprites, len(SPGL.sprites)))

        print ("Number of Labels: {}".format(len(SPGL.labels)))
        print ("Number of Buttons: {}".format(len(SPGL.buttons)))
        print ("")
        print ("Frames Per Second (Target): {}".format(self.FPS))
        print ("")
        self.print_error_logs()

    def is_collision(self, sprite_1, sprite_2):
        # Axis Aligned Bounding Box
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

    # Sprite Class
    class Sprite(turtle.Turtle):
        def __init__(self,
                    shape,
                    color,
                    x = 0,
                    y = 0,
                    width = 20,
                    height = 20):

            turtle.Turtle.__init__(self)
            self.speed(0) # Animation Speed
            # Register shape if it is a .gif file
            if shape.endswith(".gif"):
                try:
                    turtle.register_shape(shape)
                except:
                    SPGL.logs.append("Warning: {} file missing from disk.".format(shape))

                    # Set placeholder shape
                    shape = "square"
                    width = 20 # This is the default for turtle module primitives
                    height = 20 # This is the default for turtle module primitives

            self.shape(shape)
            self.color(color)
            self.penup()
            self.goto(x, y)

            # Attributes
            self.width = width
            self.height = width

            self.speed = 0.0 # Speed of motion
            self.dx = 0.0
            self.dy = 0.0
            self.acceleration = 0.0
            self.friction = 0.0

            self.state = "active"
            self.solid = True

            # Append to master sprite list
            SPGL.sprites.append(self)

        def tick(self):
            # This is the function that is called each frame of the game
            # For most sprites, you'll want to call the move method here
            # self.move()
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
            # Register shape if it is a .gif file
            if image.endswith(".gif"):
                try:
                    turtle.register_shape(image)
                except:
                    SPGL.logs.append("Warning: {} file missing from disk.".format(image))

                    # Set placeholder shape
                    shape = "square"
                    width = 20 # This is the default for turtle module primitives
                    height = 20 # This is the default for turtle module primitives

            self.shape(image)
            self.width = width
            self.height = height

    #Label Class
    class Label(turtle.Turtle):
        def __init__(self,
                    text,
                    color,
                    x = 0,
                    y = 0):

            turtle.Turtle.__init__(self)
            self.hideturtle()
            self.penup()
            self.goto(x, y)
            self.color(color)

            # Attributes
            self.text = text

            # Append to master label list
            SPGL.labels.append(self)

        def tick(self):
            self.clear()
            self.write(self.text)

        def update(self, text):
            self.text = text
            self.tick()

    #Button Class
    class Button(turtle.Turtle):
        def __init__(self,
                    shape,
                    color,
                    x = 0,
                    y = 0):

            turtle.Turtle.__init__(self)
            # self.hideturtle()
            self.penup()
            # Register shape if it is a .gif file
            if shape.endswith(".gif"):
                try:
                    turtle.register_shape(shape)
                except:
                    SPGL.logs.append("Warning: {} file missing from disk.".format(shape))

                    # Set placeholder shape
                    shape = "square"

            self.shape(shape)
            self.color(color)
            self.goto(x, y)

            #Set click binding
            self.onclick(self.click)

            # Append to master button list
            SPGL.buttons.append(self)

        def set_image(self, image):
            # Allows the use of custom images (must be .gif) due to turtle/tkinter limitation
            turtle.register_shape(image)
            self.shape(image)
            # Click binding needs to be set again after image change
            self.onclick(self.click)

        def click(self, x, y):
            print ("The button was clicked at ({},{})".format(x, y))
