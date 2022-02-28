from distutils.dep_util import newer_group
from tkinter import FALSE
from turtle import update 
import pygame
import random
from Cenarios import Cenarios
from sum import Sum
from esfera import Esfera
from tiro import Tiro

PressingW = False

pygame.init()

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption('Meu jogo')

#Grupos

objG = pygame.sprite.Group()
cenG = pygame.sprite.Group()
npc = pygame.sprite.Group()
tiroGroup = pygame.sprite.Group()




sum = Sum(objG)
cenario = Cenarios(cenG)







def canvas():
    display.fill([54,54,54])
    objG.draw(display)
    objG.update()
    npc.update()
 
    
    
    

gameLoop = True
timer = 0

clock = pygame.time.Clock()


while gameLoop:
    clock.tick(60)

    canvas()
    pygame.display.update()
    

    
    timer += 1
    if timer > 30:
        timer = 0
        if random.random() < 0.3:
            newEsfera = Esfera(objG, npc)

    # collisions = pygame.sprite.spritecollide(sum, npc, FALSE)
    # if collisions:
    #     print('Game Over')

    hits = pygame.sprite.groupcollide(tiroGroup, npc, True, True)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                newTiro = Tiro(objG, tiroGroup)
                newTiro.rect.center = sum.rect.center

        


    