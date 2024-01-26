#!/usr/bin/env python3

import random
import g, intro, ingame

# setup pygame
g.pygame.init() 
g.window = g.pygame.display.set_mode((0,0), g.pygame.FULLSCREEN)
#g.font = g.pygame.font.SysFont("monospace", g.FONT_SIZE, True)
g.font = g.pygame.font.Font("assets/MonospaceBold.ttf", g.FONT_SIZE)
clock = g.pygame.time.Clock()

g.pygame.mouse.set_visible(0)

g.MAXX, g.MAXY = g.window.get_size()

# find number of rows and columns
g.FSX,g.FSY = g.font.size("M")
g.width = g.MAXX // g.FSX
g.height = g.MAXY // g.FSY


g.playerx = g.width // 2
g.playery = g.height - 2
g.bullets = []
g.snakes = []
g.snakes.append(ingame.new_snake())

# music
g.pygame.mixer.init()
g.pygame.mixer.music.load('flying_cacti.mod')
g.pygame.mixer.music.play(-1)

g.sound_gunshot = g.pygame.mixer.Sound("assets/111047__garyq__gunshot-2-laser.wav")
g.sound_hit = g.pygame.mixer.Sound("assets/111047__garyq__gunshot-2-laser.wav")
g.sound_crash = g.pygame.mixer.Sound("assets/541029__audiopapkin__very-low-frequency-impact.wav")

# main loop

while g.running:

    clock.tick(g.FPS)

    # Events
    for event in g.pygame.event.get():

        if event.type == g.pygame.KEYDOWN:
            g.key_pressed = True
            if event.key == g.pygame.K_q:
                g.running = False

        if event.type == g.pygame.QUIT:
            g.running = False

    if g.stage == g.INTRO:
        # set background color to our window
        g.window.fill("black")
        intro.loop()    
        g.pygame.display.flip()
    elif g.stage == g.INGAME:      
        # set background color to our window
        g.window.fill("black")
        ingame.loop()    
        g.pygame.display.flip()
