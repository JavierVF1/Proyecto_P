# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 18:19:21 2021

@author: jorge
"""

import pygame
class Turret(pygame.sprite.Sprite):
    def __init__(self,imagen,):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.top=10
        self.rect.left=20
    def angulo(self,ang):
        self.ang=ang

class Tank(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        #tamaño
        self.rect.top=100
        self.rect.left=200
    def pos(self,x,y):
        self.x=x
        self.y=y
    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)
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