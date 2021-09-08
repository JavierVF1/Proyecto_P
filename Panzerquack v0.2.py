# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 18:19:21 2021

@author: jorge
"""


import pygame
import math
keys=pygame.key.get_pressed()
#########################  SHELL #########################
class Shell(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagem=imagen
        self.rect=self.imagen.get_rect()
    def disparo(t, centro, radio):
        x = radio * math.cos(t) + centro[0]
        y = radio * math.sin(t) + centro[1]
        # x = V0 * cos(a) * t
        # y = 0 +V0 * sin()*t-1/2*g*t**2
        return [round(x), round(y)]
    
#########################  TORRETA #########################
class Turret(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.top=10
        self.rect.left=20
    def angulo(self,ang):
        self.ang=ang
    def disparo(self,ang,vel):
        self.ang=ang
        self,vel=vel
        # if keys[pygame.K_SPACE]:
        
#########################  TANQUE #########################
class Tank(pygame.sprite.Sprite):
    def __init__(self,imagen,spawn):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.spawn=spawn
        #tamaño
        self.rect.top=100
        self.rect.left=200
    def spawn(self,spawn):
        self.rect.move_ip(spawn)
    def pos(self,x,y):
        self.x=x
        self.y=y
    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)
    #codigo para despues, cuando pidan movimiento será util ~JR
    # def boundaries(self):
    #     if self.rect.move <0:
    #         self.rect.move(2,0)
    #     if self.rect.move > 600:
    #         self.rect.move(-2,0)
        
#########################  MAPA #########################
class g_map(pygame.sprite.Sprite,Tank):
    def __init__(self,imagen,f_gravedad):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.top=800
        self.rect.left=600
        self.f_gravedad=f_gravedad
    # def gravedad(self,gravedad):
    #     self.gravedad=gravedad
    #     Tank.rect


def main():
    import pygame
    
    pygame.init()
    pantalla=pygame.display.set_mode((100,600))
    salir=False
    imagen=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
    
    tank_r=Tank(imagen)
    pantalla.fill((200,200,200))
    tank_r.update(pantalla)
    pygame.display.update()
main()