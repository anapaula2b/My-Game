from distutils.dep_util import newer_group
from tkinter import FALSE
from tkinter.tix import Tree
from turtle import update 
import pygame
import random
from fanton import Fanton
from esfera import Esfera
from tiro import Tiro



pygame.init()

tela = pygame.display.set_mode([840, 480])




display = pygame.display.set_mode([840, 480])
pygame.display.set_caption('Meu jogo')

WHITE = (255, 255, 255)
pontuacao = 0



#Grupos

objG = pygame.sprite.Group()

asteroideGrup = pygame.sprite.Group()
tiroGroup = pygame.sprite.Group()




#music
pygame.mixer.music.load("data/music.ogg")

pygame.mixer.music.play(-1)


shot = pygame.mixer.Sound("data/laser.wav")

#backgroud

bg = pygame.sprite.Sprite(objG)
bg.image = pygame.image.load("data/background.jpg")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()


fanton = Fanton(objG)

def canvas():
    objG.draw(display)
    objG.update()
    asteroideGrup.update()
 
    
   
    

gameLoop = True
timer = 0

clock = pygame.time.Clock()


while gameLoop:
    clock.tick(60)

    canvas()
    pygame.display.update()

    font = pygame.font.SysFont(None, 20)


    
    timer += 1
    if timer > 30:
        timer = 0
        if random.random() < 0.5:
            newEsfera = Esfera(objG, asteroideGrup)

    # collisions = pygame.sprite.spritecollide(sum, asteroideGrup, FALSE)
    # if collisions:
    #     print('Game Over')
    colisoes = pygame.sprite.groupcollide(tiroGroup, asteroideGrup, True, True)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shot.play()
                newTiro = Tiro(objG, tiroGroup)
                newTiro.rect.center = sum.rect.center
    # if hits == True:
    #     pontuacao += 1
    #     pontuacao1 = font.render(str(pontuacao), True, WHITE)
    #     display.blit(pontuacao1, [10, 10])
    #     pygame.display.flip()

                

        


    