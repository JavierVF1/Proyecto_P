# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 18:19:21 2021

@author: jorge
"""


import pygame
from math import cos, sin, pi, tan, radians
from random import randint
gray = 127,127,127
blue_sky=135,206,235
blue_sky=0,170,255

fondo=pygame.image.load("assets/maps/world.png")
fondorect=fondo.get_rect()
fondorect.move_ip(0,0)

floor=pygame.image.load("assets/maps/cp_orange/floor.png")
floorect=floor.get_rect()
floorect.move_ip(0,500)
bala = pygame.image.load("imagen.png")
speed = [1,1]
#rectangulobala = bala.get_rect()


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
#class Turret(pygame.sprite.Sprite):
#    def __init__(self,vel,ang):
#        # self.imagen=imagen
#        # self.rect=self.imagen.get_rect()
#        self.vel=vel
#        self.ang=ang
#        self.rect.top=10
#        self.rect.left=20
            
#########################  TANQUE #########################
class Tank(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,imagen,turno,ang,vel):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.turno=turno
        self.ang=ang
        self.vel=vel
    def spawn(self):
        self.rect.move_ip(self.x,self.y)
    def setVel(self,x):
        self.vel=x
    def setAng(self,y):
        self.ang=y
        # if keys[pygame.K_SPACE]:
        #     disparo()
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


def mapa():
    screen.blit(fondo,fondorect)
    montana =pygame.draw.polygon(screen, gray, [[175,440],[100,500],[250,500]]) #izquierda
    montana2=pygame.draw.polygon(screen, gray, [[673,440],[600,500],[750,500]])
    pygame.draw.polygon(screen, gray, [[175,440],[100,500],[250,500]])    #izquierda
    pygame.draw.polygon(screen, gray, [[673,440],[600,500],[750,500]])

    screen.blit(floor,floorect)

    pygame.draw.polygon(screen, blue_sky, [[350,545],[300,500],[400,500]])
    pygame.draw.polygon(screen, blue_sky, [[500,545],[450,500],[550,500]])

    return montana,montana2


def disparo(tanque): 
    rectangulobala = bala.get_rect()
    posicionY = tanque.y
    posicionX = tanque.x
    rectangulobala = rectangulobala.move(speed)
    
    #velocidad i modifica la intensidad del disparo
    velocidadi = tanque.vel
    angulo= tanque.ang
    #velocidad iY e iX modifican el angulo de disparo
    velocidadiY = velocidadi * sin(radians(angulo))
    velocidadiX = velocidadi * cos(radians(angulo))
    ti = 0

    while posicionY < 500 and posicionX<800:
        posicionX = posicionX + velocidadiX * ti
        posicionY = posicionY - velocidadiY * ti +(1/2)*6*(ti**2)
        velocidadY = velocidadiY - (6 * ti)
        velocidadX = velocidadiX - (6 * ti)
        # ti modifica la velocidad del tiro
        ti += 0.01          
        screen.blit(bala,(posicionX,posicionY))
        pygame.display.flip()
    


# def disparo(self):
    #     speed = [1,1]
    #     ti = 0
    #     bala = pygame.image.load("imagen.png")
    #     rectangulobala = bala.get_rect()
    #     rectangulobala = rectangulobala.move(speed)
    #     velocidadiY = self.vel * sin(self.ang)
    #     velocidadiX = self.vel * cos(self.ang) 
    #     if posicionX < 900:
    #         posicionX = posicionX + velocidadiX * ti
    #         posicionY = posicionY - velocidadiY * ti +(1/2)*6*(ti**2)
    #         velocidadY = velocidadiY - (6 * ti)
    #         # ti modifica la velocidad del tiro
    #         ti += 0.001
    
    # if posicionX < 900:
    #     posicionX = posicionX + velocidadiX * ti
    #     posicionY = posicionY - velocidadiY * ti +(1/2)*6*(ti**2)
    #     velocidadY = velocidadiY - (6 * ti)
    #     # ti modifica la velocidad del tiro
    #     ti += 0.01



pygame.init()

#ancho y alto
Sreen_width=800
Sreen_height=600

#     SPAWN RANDOM

xtanki = randint(10,Sreen_width/2)
ytanki = 486
constantesuelo = 0.8

if xtanki > 90 and xtanki < 167:
    ytanki = ytanki - constantesuelo*(xtanki-90)  

if xtanki == 167:
    ytanki = 428

if xtanki > 167 and xtanki < 250:
    ytanki = 428 + constantesuelo*(xtanki-167)

if xtanki > 290 and xtanki < 340:
    ytanki = ytanki + (xtanki-290)
    
if xtanki == 340:
    ytanki = 530

if xtanki > 340 and xtanki < 400:
    ytanki = 530 - (xtanki-340)


xtankd=randint(xtanki+Sreen_width/2,Sreen_width-10)
ytankd = 486

if xtankd < 748 and xtankd > 665:
    ytankd = ytankd - constantesuelo*(748-xtankd)

if xtankd == 665:
    ytankd = 428

if xtankd < 665 and xtankd > 595:
    ytankd = 428 + constantesuelo*(665-xtankd)

if xtankd < 540 and xtankd > 495:
    ytankd = ytankd + (540-xtankd)
    
if xtankd == 495:
    ytankd = 530

if xtankd < 495 and xtankd > 438:
    ytankd = 530 - (495-xtankd)


size = Sreen_width, Sreen_height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Panzerquack")


run=True
turno=0
contador=0
while run:
    
   
    
    pygame.time.delay(4)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run=False
    keys=pygame.key.get_pressed()



    tank_g=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
    tank_r=pygame.image.load("assets\sprites\PLAYERS\GREEN_R\duck_s.png")
    tank_gc=Tank(xtanki,ytanki,10,10,tank_g,1,10,10)
    tank_rc=Tank(xtankd,ytankd,10,10,tank_r,2,10,10)

    
    montana,montana2=mapa()

    tank_gc.spawn()
    screen.blit(tank_gc.imagen,tank_gc.rect)
    tank_rc.spawn()
    screen.blit(tank_rc.imagen,tank_rc.rect)
    
    
    if keys[pygame.K_SPACE]:
        turno = 1
    
    if turno==10:
       turno=1
    
    if turno == 2:
        
        print("Truno DOS")
        x=float(input("ingrese la velocidad:"))
        tank_rc.setVel(-x)
        y=float(input("ingrese el angulo:"))
        tank_rc.setAng(-y)

        
        disparo(tank_rc)
        pygame.display.flip()
        turno=10
    
    
    if turno == 1:

        print("Truno UNO")
        x=float(input("ingrese la velocidad:"))
        tank_gc.setVel(x)
        y=float(input("ingrese el angulo:"))
        tank_gc.setAng(y)


        disparo(tank_gc)
        pygame.display.flip()
        turno=2
    
        
    pygame.display.flip()
    
    if keys[pygame.K_ESCAPE]:
        run=False
    
