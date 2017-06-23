
# SGE (Version 0.3)
A simple Python game engine used for creating simple 2D games.  It is built on the Python Turtle module.

#Overview:

The purpose of the Simple Game Engine is to give beginning Python coders a simple framework to make basic 2D games.  It is intended as an alternative to Pygame. As it is built on the Turtle module, it has the same features and limitations of that module. It does not require any external libraries to be added.

##Documentation:

###SGE Class

####Initial Game Setup:

``` 
from SGE import *
# WINDOW_WIDTH, WINDOW_HEIGHT, Background Color, and Window Title
game = SGE(800, 600, "blue", "SGE Game Demo") 
```

###SGE Attributes
```python
title # Window title text (string)
gravity # Game gravity constanst (float)
state # Game state (string) or None
FPS # Game FPS - default is 30 FPS (float)
SCREEN_WIDTH # Width of the screen in pixels (int)
SCREEN_HEIGHT # Height of the screen in pixels (int)
time # Time in seconds (float)
```

###SGE Methods

####Keyboard Bindings
```python
game.set_keyboard_binding(key, function)
```
####Built-in Key Definitions
```python    
SGE.KEY_UP = "Up"
SGE.KEY_DOWN = "Down"
SGE.KEY_LEFT = "Left"
SGE.KEY_RIGHT = "Right"
SGE.KEY_SPACE = "space"
```

```python
set_title(title)
game.set_title("My Game Title")
```

```python
set_score(score)
game.set_score(100)
```

```python
update_screen()
game.update_screen()
```

```python
play_sound(soundfile) #.wav file
game.play_sound("explosion.wav")
```

```python
stop_all_sounds()
game.stop_all_sounds()
```

```python
clear_terminal_screen()
game.clear_terminal_screen()
```

```python
print_game_info()
game.print_game_info()
```

```python
is_collision(sprite_1, sprite_2)
game.is_collision(player, enemy)
```

###SGE.Sprite Class

####Create a Sprite
*It is recommended to create child class first*

```python
class Player(SGE.Sprite):
    def __init__(self, shape, color, x, y):
        SGE.Sprite.__init__(self, shape, color, x, y)
# Shape, Color, starting x coordinate, starting y coordinate
player = Player("triangle", "red", -400, 100)
```

####Sprite Attributes

```python
dx # x velocity (float)
dy # y velocity (float)
speed # speed (float)
acceleration # acceleration (float)
width # width in pixels (float)
height # height in pixels (float)
state # object state - default is "active" (string) or None
friction # friction (float)
solid # (bool)
```

####Sprite Methods

Move
```python
sprite.move()
```

Destroy
```python
sprite.destroy()
```

Set Image
```python
sprite.set_image("image.gif", width, height)
```



Follow me on Twitter @tokyoedtech

Various tutorials available on my YouTube Channel at https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg
