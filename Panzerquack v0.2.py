# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 18:19:21 2021

@author: jorge
"""


import pygame
import math


time=0
#########################  SHELL #########################
class Shell(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagem=imagen
        self.rect=self.imagen.get_rect()
    def pos(self,x,y):
        self.x=x
        self.y=y
#########################  TORRETA #########################
class Turret(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.top=10
        self.rect.left=20
    def angulo(self,ang):
        self.ang=ang
    def velocidad_proyect(self,Turret):
        if keys[pygame.K_DOWN]:
                self.vel=Turret.vel-1
        if keys[pygame.K_UP]:
                self.vel=Turret.vel+1    
    def disparo(self,ang,vel):
        self.ang=ang
        self.vel=vel
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

    def spawn(self,x,y):
        self.rect.move_ip(x,y)

    #codigo para despues, cuando pidan movimiento será util ~JR
    # def boundaries(self):
    #     if self.rect.move <0:
    #         self.rect.move(2,0)
    #     if self.rect.move > 600:
    #         self.rect.move(-2,0)
        
#########################  MAPA #########################
class Map(pygame.sprite.Sprite):
    def __init__(self,imagen,gravity,turno_map):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.turno_map=turno_map
        self.rect.top=800
        self.rect.left=600
        self.f_gravedad=f_gravedad
    def turno(self,Tank):
        if Tank.turno==self.turno_map:
            Tank.move=True
        else:
            Tank.move=False
    # def gravedad(self,gravedad):
    #     self.gravedad=gravedad
    #     Tank.rect


def main():
    import pygame
    pygame.init()
    pantalla=pygame.display.set_mode((600,600))
    
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
    tank_g=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
    tank_gc=Tank(500,100,10,10,tank_g,1)
        #tank red
    # tank_r=pygame.image.load("assets\sprites\PLAYERS\RED_P\duck_s.png")
    tank_rc=Tank(500,500,10,10,tank_g,2)
    pantalla.fill((200,200,200))
    pantalla.blit(tank_gc.imagen,tank_gc.rect)
    pygame.display.update()
main()