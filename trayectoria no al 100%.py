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

def xyRecorrido(t, centro, radio):
    x = radio * math.cos(t) + centro[0]
    y = radio * math.sin(t) + centro[1]
    
    # x = V0 * cos(a) * t
    # y = 0 +V0 * sin()*t-1/2*g*t**2
    return [round(x), round(y)]

posicionY = 400
posicionX = 100
velocidadi = 2
velocidadiY = velocidadi * sin(1.24)
velocidadiX = velocidadi * cos(1.24) 
ti = 0.000001
   
              #CICLO JUEGO
run = True
t =0

while run:
    
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    rectangulobala = rectangulobala.move(speed)
    
    screen.fill(fondo)
    
##################### FUNCIONAL #################################
    #movimiento bala 
    t -= 0.5
    if t <= -70:
        bala = bala3
    if t<= -120:
        bala = bala2
        
    if t <= -180:
        bala = balaaux
        screen.blit(explosion,(90,300))           
        t = 0
     
    x, y = xyRecorrido(math.radians(t), [400, 300], 300)
#################################################################
    
################# NO FUNCIONAL ##################################
    """posicionX = posicionX + velocidadiX * ti
    posicionY = posicionY + velocidadiY * ti -(1/2)*9.8*(ti**2)
    velocidadY = velocidadiY - 9.8 * ti
    ti = ti + 1"""
#################################################################        
    
    #representacion imagen        

    screen.blit(bala,(x,y))
    pygame.display.flip()
            
pygame.quit()



