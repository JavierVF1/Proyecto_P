import pygame
import sys
import time
import random

pygame.init()

Sreen_width=800
Sreen_height=600

size = Sreen_width, Sreen_height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Panzerquack")
#screen size
width=800
height=600

"""
esto tiene que poderse modificar, para poder hacer que en un futuro
se pueda usarse la pantalla completa
JR
"""
#fundamental forces and tank movement
speed=[1,1]
gravity=[0,1]

#background
white=255,255,255
blue_sky=135,206,235
black=0,0,0
gray = ((127,127,127))



#player
tank=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
tankrect=tank.get_rect()
tankrect.move_ip(400,100)

#map
floor=pygame.image.load("assets/maps/cp_orange/floor.png")
floorect=floor.get_rect()
floorect.move_ip(0,500)

montaña =pygame.draw.polygon(screen, gray, [[175,440],[100,500],[250,500]])
montaña2=pygame.draw.polygon(screen, gray, [[673,440],[600,500],[750,500]])

#montain
def montain():
    pocicion = (Sreen_width/2)+ random.randint(-0.2*Sreen_width, 0.2*Sreen_width)
    randomheight= random.randrange(Sreen_height*0.1,Sreen_height*0.6)
    
    #pygame.draw.rect(screen, black, [pocicion,Sreen_height-randomheight, 50 ,randomheight])
    
    pygame.draw.polygon(screen, gray, [[175,440],[100,500],[250,500]])    #izquierda

    pygame.draw.polygon(screen, gray, [[673,440],[600,500],[750,500]])




run=True
while run:
    
    pygame.time.delay(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run=False
    keys=pygame.key.get_pressed()
    #movement
    
    if keys[pygame.K_LEFT]:
        tankrect=tankrect.move(-1,0)
    if keys[pygame.K_RIGHT]:
        tankrect=tankrect.move(1,0)
    #boundaries
    if tankrect.left < 0:
        tankrect=tankrect.move(1,0)
    if tankrect.right>width:
        tankrect=tankrect.move(-1,0)



    if montaña.colliderect(tankrect):
        tankrect=tankrect.move(0,(-2))
    
    if montaña2.colliderect(tankrect):
        tankrect=tankrect.move(0,(-2))
    

    #floor collide
    if floorect.colliderect(tankrect):
        tankrect=tankrect.move(0,0)
    
    #gravity
    else:
        tankrect=tankrect.move(gravity)
    
    
    

    screen.fill(blue_sky)
    montain()
    screen.blit(floor,floorect)
    screen.blit(tank,tankrect)
    
    pygame.display.flip()
    
pygame.quit()
 