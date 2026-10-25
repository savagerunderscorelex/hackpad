print("Starting")

# Setup for Macropad since i didn't make a matrix...
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner # Scanner used for looking for individual keys compared to matrix scanner
from kmk.modules.macros import Press, Release, Tap # importing macros because they're needed to do the shortcuts

# Define Pins (GPIO to key mapping)
pins = [
    board.D0, board.D1, board.D2, board.D3, # lower left, upper left, upper right, lower right keys
]

# Macros

COPY = KC.MACRO(
    Press.(KC.LCTL),
    Tap.(KC.C),
    Release.(KC.LCTL)
)

PASTE = KC.MACRO(
    Press.(KC.LCTL),
    Tap.(KC.V),
    Release.(KC.LCTL)
)

DELETE = KC.MACRO(
    Press.(KC.DEL),
    Release.(KC.DEL)
)

SELECT_ALL = KC.MACRO(
    Press.(KC.LCTL),
    Tap.(KC.A),
    Release.(KC.LCTL)
)

# Class for new Scanner

class loveBoard(KMKKeyboard){
    def __init__(self):
        super().__init__()

    #creating scanner
    self.matrix = KeysScanner(
        pins = pins, value_when_pressed = False
    )
}

# New instance of LoveBoard
keyboard = loveBoard()

# Keyboard Keymap
keyboard.keymap = [
    [PASTE, COPY, SELECT_ALL, DELETE]
]


if __name__ == '__main__':
    keyboard.go()