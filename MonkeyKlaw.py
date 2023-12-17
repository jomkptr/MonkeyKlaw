import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,50)
import pygame
import pgzrun
import random

    
TITLE = 'Monkey Klaw'
WIDTH = 800
HEIGHT = 600

monkeySprite = Actor('monkey')
monkeySprite.pos = (400,550)
bananaSprite = Actor('banana')
bananaSprite.pos = (random.randint(0,800),0)
durianSprite = Actor('durian')
durianSprite.pos = (random.randint(0,800),0)

score = 0
goal = 5

game_state = ''

def update():
    global score
    global game_state
    if keyboard.d == True :
        monkeySprite.x = monkeySprite.x + 5
    if keyboard.a == True :
        monkeySprite.x = monkeySprite.x - 5
    if monkeySprite.x <= 0 :
        monkeySprite.x = 0
    if monkeySprite.x >= 800 :
        monkeySprite.x = 800
        
    if game_state == 'play' :
        bananaSprite.y = bananaSprite.y + 4
        if bananaSprite.y >= 600 :
            bananaSprite.pos = (random.randint(0,800),0)
        durianSprite.y = durianSprite.y + 6
        if durianSprite.y >= 600 :
            durianSprite.pos = (random.randint(0,800),0)
        if monkeySprite.colliderect(bananaSprite) :
            bananaSprite.pos = (random.randint(0,800),0)
            score = score +1
            print('score', score)
            if score >= 5 :
                game_state = 'win'
                #gamesong()
        if monkeySprite.colliderect(durianSprite) :
            durianSprite.pos = (random.randint(0,800),0)
            print('Game Over')
            game_state = 'gameover'
            #gamesong()

def draw():
    global game_state
    screen.blit(images.garden, (0,0))
    def restart():
        global game_state
        global score
        screen.draw.text('Press spacebar to start', center = (400,300), color = 'lightgoldenrod1', fontsize = 70)
        if keyboard.space == True :
            game_state = 'play'
            #gamesong()
            score = 0
            
    if game_state == '' :
        screen.draw.text('Monkey Klaw', center = (400,200), color = 'cornsilk1', fontsize = 100)
        restart()
        
    elif game_state == 'gameover' :
        screen.draw.text('Game Over!', center = (400,200), color = 'slateblue4', fontsize = 100)
        restart()

    elif game_state == 'win' :
        screen.draw.text('You are the winner', center = (400,200), color = 'slategray1', fontsize = 100)
        restart()
        
    elif game_state == 'play' :
        monkeySprite.draw()
        bananaSprite.draw()
        durianSprite.draw()
        screen.draw.text('goal : 5', (15,10), color = 'seashell1', fontsize = 30)
        screen.draw.text('remaining : ' + str(goal-score), (15,50), color = 'seashell1', fontsize = 30)
    
pgzrun.go()
