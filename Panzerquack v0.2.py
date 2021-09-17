# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 18:19:21 2021

@author: jorge
"""


import pygame
from math import cos, sin, pi, tan

blue_sky=135,206,235
floor=pygame.image.load("assets/maps/cp_orange/floor.png")
floorect=floor.get_rect()
floorect.move_ip(0,500)
time=0
# #########################  SHELL #########################
# class Shell(pygame.sprite.Sprite):
#     def __init__(self,imagen):
#         self.imagem=imagen
#         self.rect=self.imagen.get_rect()
#     def pos(self,x,y):
#         self.x=x
#         self.y=y
#########################  TORRETA #########################
class Turret(pygame.sprite.Sprite):
    def __init__(self,vel,ang):
        # self.imagen=imagen
        # self.rect=self.imagen.get_rect()
        self.vel=vel
        self.ang=ang
        self.rect.top=10
        self.rect.left=20
            
#########################  TANQUE #########################
class Tank(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,imagen,turno):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.turno=turno

    def spawn(self):
        self.rect.move_ip(self.x,self.y)
    
    def vel_ang(self,Turret):
        if keys[pygame.K_DOWN]:
                self.vel=Turret.vel-1
        if keys[pygame.K_UP]:
                self.vel=Turret.vel+1
        if keys[pygame.K_LEFT]:
                self.ang=self.ang+1
        if keys[pygame.K_RIGHT]:
                self.ang=self.ang-1
        if keys[pygame.K_SPACE]:
            if turno==1:
                turno=turno+1
            if turno==2:
                turno=1
    #codigo para despues, cuando pidan movimiento será util ~JR
    # def boundaries(self):
    #     if self.rect.move <0:
    #         self.rect.move(2,0)
    #     if self.rect.move > 600:
    #         self.rect.move(-2,0)
        
#########################  MAPA #########################
# class Map(pygame.sprite.Sprite):
#     def __init__(self,imagen,turno):
#         self.imagen=imagen
#         self.rect=self.imagen.get_rect()
#         self.turno_map=turno_map
#         self.rect.top=800
#         self.rect.left=600
#         # self.gravityt=gravity
#     def turno(self,Tank):
#         if Tank.turno==self.turno_map:
#             Tank.move=True
#         else:
#             Tank.move=False
#     # def gravedad(self,gravedad):
#     #     self.gravedad=gravedad
#     #     Tank.rect
##########################################################
    #tank obj
    #ejemplo para futuro:
    #tank_x=pygame.image.load("assets\Sprites\PLAYERS\X_P\duck_s.png)
    #El comando de arriba quiere decir que se cargara la imagen duck_s (duck still), que se usara...
    #en la creación del tanque
    #tank_xc=Tank(x,y,width,height,tank_x,turno)
    #este de aquí arriba es el objeto tank
    #tiene coordenadas x e y que serán su punto de spawn
    #un ancho y alto
    #un sprite tank_x
    #y finalmente un numero de turno que debiese ser modificado manualmente
        #tank green

        #tank red
    # tank_r=pygame.image.load("assets\sprites\PLAYERS\RED_P\duck_s.png")


run=True
while run:
    pygame.init()

    Sreen_width=800
    Sreen_height=600
    
    size = Sreen_width, Sreen_height
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Panzerquack")

        
    pygame.time.delay(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run=False
    keys=pygame.key.get_pressed()
    turno=1
    tank_g=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
    tank_gc=Tank(200,100,10,10,tank_g,1)
    tank_rc=Tank(300,120,10,10,tank_g,2)
    
    screen.fill(blue_sky)
    #tanque green
    tank_gc.spawn()
    screen.blit(tank_gc.imagen,tank_gc.rect)
    tank_rc.spawn()
    screen.blit(tank_rc.imagen,tank_rc.rect)
    def disparo(tanque):
        speed = [1,1]
        bala = pygame.image.load("imagen.png")
        rectangulobala = bala.get_rect()
        rectangulobala = rectangulobala.move(speed)
        velocidadi = 2
        velocidadiY = velocidadi * sin(tanque.ang)
        velocidadiX = velocidadi * cos(tanque.ang) 
        if posicionX < 900:
            tanque.x = tanque.x + velocidadiX * ti
            posicionY = tanque.y - velocidadiY * ti +(1/2)*6*(ti**2)
            velocidadY = velocidadiY - (6 * ti)
            # ti modifica la velocidad del tiro
            ti += 0.001
    screen.blit(floor,floorect)
    pygame.display.flip()
    disparo(tank_gc)
