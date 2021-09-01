import pygame
import sys
import time

pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Panzerquack")
width=800
height=600
speed=[1,1]
white=255,255,255
tank=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
tankrect=tank.get_rect()
tankrect.move_ip(400,300)
run=True
while run:
    pygame.time.delay(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tank=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_m.png")
        pygame.time.delay(1)
        tank=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_m2.png")
        tankrect=tankrect.move(-1,0)
    else:
        tank=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
    if keys[pygame.K_RIGHT]:
        tank=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_m.png")
        pygame.time.delay(1)
        tank=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_m2.png")
        tankrect=tankrect.move(1,0)
    else:
        tank=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
    if tankrect.left < 0 or tankrect.right>width:
        tankrect=tankrect.move(0,0)
    screen.fill(white)
    screen.blit(tank,tankrect)
    pygame.display.flip()
    
pygame.quit()
 