import random, pyfiglet
import g
# go from black to white in 5 sec, then display name
# keypress cancels and goes on ingame stage

# grayscale values
grayscale = ' `.-'':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@'

timespan = 2 * g.FPS
counter = 0
density = 1000

logo = pyfiglet.figlet_format("Snakeroids ! ! !", font="slant")

def loop():
    global counter

    if g.key_pressed: g.stage = g.INGAME

    if counter < timespan:
        for i in range(density - density * counter // timespan):
            g.addstr(random.randint(0,g.width-1), random.randint(0,g.height-1), '**')
        counter += 1
    else:
        # display name
        rows = logo.split('\n')
        for i, r in enumerate(rows):
            g.addstr((g.width - len(r)) // 2, g.height / 2 -3 + i,r)

        g.addstr((g.width - len(r)) // 2, g.height / 2 - 1 + i,"ARROWS To Move, SPACE To Shoot.")

        for i in range(200):
            g.addstr(random.randint(0,g.width-1), random.randint(0,g.height-1), '*')
