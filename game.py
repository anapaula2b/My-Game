from distutils.dep_util import newer_group
from tkinter import FALSE
from tkinter.tix import Tree
from turtle import update 
import pygame
import random
from fantasma import Fantasma
from esfera import Esfera
from tiro import Tiro
import time



pygame.init()

pontuacao = 0

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption('Meu jogo')


#Grupos
objG = pygame.sprite.Group()
asteroideGrup = pygame.sprite.Group()
tiroGroup = pygame.sprite.Group()
playerGrup = pygame.sprite.Group()

#personagem
fantasma = Fantasma(playerGrup)

#musica
pygame.mixer.music.load("data/music.ogg")
pygame.mixer.music.play(-1)
shot = pygame.mixer.Sound("data/laser.wav")

#backgroud
bg = pygame.sprite.Sprite(objG)
bg.image = pygame.image.load("data/background.jpg")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()


life = 10
gameLoop = True
timer = 0

clock = pygame.time.Clock()

#função para desenhar os objetos na tela
def canvas():
    objG.draw(display)
    objG.update()
    asteroideGrup.update()
    playerGrup.draw(display)
    playerGrup.update()

while gameLoop:
    clock.tick(60)

    canvas()
    pygame.display.update()

    font = pygame.font.SysFont(None, 50)

   
    #A cada 30 frames uma nova esfera deve aparecer
    timer += 1
    if timer > 40:
        timer = 0
        newEsfera = Esfera(objG, asteroideGrup)
   
    #Colisões entre grupos
    collisions1 = pygame.sprite.groupcollide(tiroGroup, asteroideGrup, True, True)
    if collisions1:

        pontuacao += 1 
        print(pontuacao)


        pygame.display.flip()
        texto = str(pontuacao)
        txt = font.render(texto, True, [255, 255, 255])
        display.blit(txt, [0, 0])
        pygame.display.flip()
 

    collisions2 = pygame.sprite.groupcollide(playerGrup, asteroideGrup, False, True)
    # if collisions2:
    #     life -= 1
    # if life == 0:
    #     fantasma.kill()
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shot.play()
                newTiro = Tiro(objG, tiroGroup)
                newTiro.rect.center = fantasma.rect.center

   
            
                

        


    