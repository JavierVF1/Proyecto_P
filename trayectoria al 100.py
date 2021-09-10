# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 18:50:43 2021

@author: tomas
"""

import pygame, time
from math import cos, sin, pi, tan
import math


pygame.init()

size = 800,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Probando trayectoria")

bala = pygame.image.load("imagen.png")
bala2 = pygame.image.load("imagen2.png")
balaaux = pygame.image.load("imagen.png")
bala3 = pygame.image.load("imagen3.png")
explosion = pygame.image.load("explosion.png")
speed = [1,1]
fondo = 255,255,255
posicionbala_x = 100
posicionbala_y = 400
rectangulobala = bala.get_rect()
a=0

posicionY = 400
posicionX = 100

#velocidad i modifica la intensidad del disparo
velocidadi = 2

#velocidad iY e iX modifican el angulo de disparo
velocidadiY = velocidadi * sin(1.24)
velocidadiX = velocidadi * cos(1.24) 
ti = 0
   
              #CICLO JUEGO
run = True
t = 0

while run:
    
    pygame.time.delay(6)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    rectangulobala = rectangulobala.move(speed)
    
    screen.fill(fondo)

    
    if posicionX < 900:
        posicionX = posicionX + velocidadiX * ti
        posicionY = posicionY - velocidadiY * ti +(1/2)*6*(ti**2)
        velocidadY = velocidadiY - (6 * ti)
        # ti modifica la velocidad del tiro
        ti += 0.001
         
    #representacion imagen        

    screen.blit(bala,(posicionX,posicionY))
    pygame.display.flip()
            
pygame.quit()



