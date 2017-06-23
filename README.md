# SGE
A simple Python game engine used for creating simple 2D games.  It is built on the Python Turtle module.

Overview:

The purpose of the Simple Game Engine is to give beginning Python coders a simple framework to make basic 2D games.  It is intended as an alternative to Pygame. As it is built on the Turtle module, it has the same features and limitations of that module. It does not require any external libraries to be added.

Documentation:

SGE Class

Initial Game Setup:

```python
from SGE import *
game = SGE(800, 600, "blue", "SGE Game Demo") # WINDOW_WIDTH, WINDOW_HEIGHT, Background Color, and Window Title
```

Keyboard Bindings
```python
game.set_keyboard_binding(key, function)
```
Built-in Key Definitions
```python    
SGE.KEY_UP = "Up"
SGE.KEY_DOWN = "Down"
SGE.KEY_LEFT = "Left"
SGE.KEY_RIGHT = "Right"
SGE.KEY_SPACE = "space"
```



Follow me on Twitter @tokyoedtech
Various tutorials available on my YouTube Channel at https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg
