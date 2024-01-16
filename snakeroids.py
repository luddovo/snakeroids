#!/usr/bin/env python3

import math, random, pygame, itertools,sys

NOVALUE = -999

# setup pygame
pygame.init() 
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
FPS = 60
FONT_SIZE = 15

pygame.mouse.set_visible(0)

MAXX, MAXY = window.get_size()

font = pygame.font.SysFont("monospace", FONT_SIZE, True)

# find number of rows and columns
FSX,FSY = font.size("M")
width = MAXX // FSX
height = MAXY // FSY


playerx = width // 2
playery = height - 2
bullets = []
snakes = []
snake_speed_cnt = 0
first_snake = True

# music
pygame.mixer.init()
pygame.mixer.music.load('flying_cacti.mod')
pygame.mixer.music.play(-1)


def addstr(x, y, text):
    text = font.render(text, True, "white", "black")
    textRect = text.get_rect()
    textRect.topleft = (x * FSX, y * FSY)
    window.blit(text, textRect)

def new_snake(links = None):
  if links == None:
      links = [(random.randint(0, width-1),
                random.randint(0, height-1)
            )]
  return {'snix': NOVALUE, 
                 'sniy': NOVALUE, 
                 'links': links
                }  

snakes.append(new_snake())

# main loop

while True:

    clock.tick(FPS)

    # Events
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

        if event.type == pygame.QUIT:
            running = False
      
    # set background color to our window
    window.fill("black")
    
    addstr(playerx, playery, "^")

    # pygame keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        playery = (playery - 1) % height
    elif keys[pygame.K_DOWN]:
        playery = (playery + 1) % height
    elif keys[pygame.K_LEFT]:
        playerx = (playerx - 1) % width
    elif keys[pygame.K_RIGHT]:
        playerx = (playerx + 1) % width
    elif keys[pygame.K_SPACE]:
        bullets.append((playerx, playery))
    elif keys[pygame.K_q]: break
    elif keys[pygame.K_ESCAPE]: break

    # snakes
    snake_speed_cnt = (snake_speed_cnt + 1) % 2
    for snake in snakes:
        if not snake_speed_cnt:
            x, y = snake['links'][0]
            if snake['snix'] == NOVALUE or random.randint(1,100) > 95:
                snake['snix'] = snake['sniy'] = 0
                snake['snix' if random.randint(0,1) else 'sniy'] = \
                    1 if random.randint(0,1) else -1
            x = ( x + snake['snix'] ) % width
            y = ( y + snake['sniy'] ) % height
            snake['links'] = [(x,y)] + snake['links']
            if not first_snake or random.randint(1,100) > 30:
                snake['links'].pop(-1)
        for pos in snake['links']:
            x,y = pos
            addstr(x, y, "O")


    # bullets
    i = 0
    while i < len(bullets):
        x, y = bullets[i]
        y -= 1
        if y < 0:
            del bullets[i]
        else:
            bullets[i] = (x,y)
            addstr(x, y, ".")
            i += 1

    # colisions between bullets and snakes
    i = 0
    while i < len(bullets):            
        bx, by = bullets[i]
        for snake in snakes:
            hit = -1
            for l, pos in enumerate(snake['links']):
                sx, sy = pos
                if bx == sx and by == sy:
                    hit = l
                    break
            if hit > -1:
                # remove bullet
                del bullets[i]
                # split snake
                first_snake = False
                snakes.remove(snake)
                first_half = snake['links'][:l]
                second_half = snake['links'][l+1:]
                if first_half:
                    snakes.append(new_snake(first_half))
                if second_half:
                    snakes.append(new_snake(second_half))
                break
        i += 1
        
    # player - snakes collisions
    hit = False
    for snake in snakes:
        if (playerx, playery) in snake['links']:
            hit = True
            break
    if hit: sys.exit()
 
    pygame.display.flip()
