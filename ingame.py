import random
import g

def new_snake(links = None):
  if links == None:
      links = [(random.randint(0, g.width-1),
                random.randint(0, g.height-1)
            )]
  return {'snix': g.NOVALUE, 
                 'sniy': g.NOVALUE, 
                 'links': links
                }  

def loop():

    g.addstr(g.playerx, g.playery, "^")

    # pygame keys
    keys = g.pygame.key.get_pressed()
    if keys[g.pygame.K_UP]:
        g.playery = (g.playery - 1) % g.height
    elif keys[g.pygame.K_DOWN]:
        g.playery = (g.playery + 1) % g.height
    elif keys[g.pygame.K_LEFT]:
        g.playerx = (g.playerx - 1) % g.width
    elif keys[g.pygame.K_RIGHT]:
        g.playerx = (g.playerx + 1) % g.width
    elif keys[g.pygame.K_SPACE]:
        g.bullets.append((g.playerx, g.playery))
        g.pygame.mixer.Sound.play(g.sound_hit)
    elif keys[g.pygame.K_q]: g.running = False
    elif keys[g.pygame.K_ESCAPE]: g.running = False

    # snakes
    g.snake_speed_cnt = (g.snake_speed_cnt + 1) % 2
    for snake in g.snakes:
        if not g.snake_speed_cnt:
            x, y = snake['links'][0]
            if snake['snix'] == g.NOVALUE or random.randint(1,100) > 95:
                snake['snix'] = snake['sniy'] = 0
                snake['snix' if random.randint(0,2) else 'sniy'] = \
                    1 if random.randint(0,1) else -1
            x = ( x + snake['snix'] ) % g.width
            y = ( y + snake['sniy'] ) % g.height
            snake['links'] = [(x,y)] + snake['links']
            if not g.first_snake or random.randint(1,100) > 30:
                snake['links'].pop(-1)
        for pos in snake['links']:
            x,y = pos
            g.addstr(x, y, "O")


    # bullets
    i = 0
    while i < len(g.bullets):
        x, y = g.bullets[i]
        y -= 1
        if y < 0:
            del g.bullets[i]
        else:
            g.bullets[i] = (x,y)
            g.addstr(x, y, ".")
            i += 1

    # colisions between bullets and snakes
    i = 0
    while i < len(g.bullets):            
        bx, by = g.bullets[i]
        for snake in g.snakes:
            hit = -1
            for l, pos in enumerate(snake['links']):
                sx, sy = pos
                if bx == sx and by == sy:
                    hit = l
                    break
            if hit > -1:
                g.pygame.mixer.Sound.play(g.sound_hit)
                # remove bullet
                del g.bullets[i]
                # split snake
                g.first_snake = False
                g.snakes.remove(snake)
                first_half = snake['links'][:l]
                second_half = snake['links'][l+1:]
                if first_half:
                    g.snakes.append(new_snake(first_half))
                if second_half:
                    g.snakes.append(new_snake(second_half))
                break
        i += 1
        
    # player - snakes collisions
    hit = False
    for snake in g.snakes:
        if (g.playerx, g.playery) in snake['links']:
            hit = True
            break
    if hit: 
        g.pygame.mixer.Sound.play(g.sound_crash)
        g.lives -= 1
        if not g.lives:
            g.running = False

    # status bar
            
    g.points += 1

    points = "Points: " + str(g.points)
    lives = "Lives: " + str(g.lives)
    spaces = " " * (g.width - len(points) - len(lives))
    g.addstr(0, g.height, points + spaces + lives, "black", "white")