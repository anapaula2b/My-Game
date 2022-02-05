from tkinter import FALSE
from turtle import update 
import pygame
import random
from Cenarios import Cenarios
from Sum import Sum
from Laser import Laser

PressingW = False

pygame.init()

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption('Meu jogo')

#objects

objG = pygame.sprite.Group()

sum = Sum(objG)


cenG = pygame.sprite.Group()
cenario = Cenarios(cenG)

npc = pygame.sprite.Group()



def canvas():
    display.fill([148, 193, 255])
    objG.draw(display)
    objG.update()
    npc.update()
    cenG.draw(display)
    
    
    

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
            newLaser = Laser(objG, npc)

    # collisions = pygame.sprite.spritecollide(sum, npc, FALSE)
    # if collisions:
    #     print('Game Over')


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False


    