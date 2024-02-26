import pygame

# constants
NOVALUE = -999
FONT_SIZE = 20
FPS = 60

# game stages
INTRO = 1
INGAME = 2
LIFEDOWN = 3
WON = 4
GAMEOVER = 5

MAXX = MAXY = None
FSX = FSY = None
width = height = None

# state variables
running = True
stage = INTRO

window = None
font = None

snake_speed_cnt = 0
first_snake = True

key_pressed = False

points = 0
lives = 5

# functions
def addstr(x, y, text, fg="white", bg="black"):
    text = font.render(text, True, fg, bg)
    textRect = text.get_rect()
    textRect.topleft = (x * FSX, y * FSY)
    window.blit(text, textRect)

