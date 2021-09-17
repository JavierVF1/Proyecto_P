import pygame
import sys
import time
import random

#montain
#

def cambiaso(turno):
    if turno == 1:
        turno=2
        
        return turno
    if turno == 2:
        turno=1
        
        return turno




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
gray = 127,127,127



#player
tank=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
tankrect=tank.get_rect()
tankrect.move_ip(200,100)


#player2
tank2=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
tank2rect=tank2.get_rect()
tank2rect.move_ip(500,100)

#map
floor=pygame.image.load("assets/maps/cp_orange/floor.png")
floorect=floor.get_rect()
floorect.move_ip(0,500)

montaña =pygame.draw.polygon(screen, gray, [[175,440],[100,500],[250,500]])
montaña2=pygame.draw.polygon(screen, gray, [[673,440],[600,500],[750,500]])



#turnos
turno = 0




run=True
while run:
    

        
    pygame.time.delay(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run=False
    keys=pygame.key.get_pressed()
    
    
    if keys[pygame.K_1]:
        turno=1
    if keys[pygame.K_2]:
        turno=2
    if keys[pygame.K_3]:
        turno=cambiaso(turno)



    if turno == 1:
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


    if turno == 2:
    #movement
        if keys[pygame.K_LEFT]:
            tank2rect=tank2rect.move(-1,0)
        if keys[pygame.K_RIGHT]:
            tank2rect=tank2rect.move(1,0)
        #boundaries
        if tank2rect.left < 0:
            tank2rect=tank2rect.move(1,0)
        if tank2rect.right>width:
            tank2rect=tank2rect.move(-1,0)



    if montaña.colliderect(tankrect):
        tankrect=tankrect.move(0,(-2))
    if montaña2.colliderect(tankrect):
        tankrect=tankrect.move(0,(-2))

    if montaña.colliderect(tank2rect):
        tank2rect=tank2rect.move(0,(-2))
    if montaña2.colliderect(tank2rect):
        tank2rect=tank2rect.move(0,(-2))


    #floor collide player1
    if floorect.colliderect(tankrect):
        tankrect=tankrect.move(0,0)
    #gravity player1
    else:
        tankrect=tankrect.move(gravity)


    #floor collide player2
    if floorect.colliderect(tank2rect):
        tank2rect=tank2rect.move(0,0)
    #gravity player2
    else:
        tank2rect=tank2rect.move(gravity)
        
    


        

        
    

    screen.fill(blue_sky)
    #montain()
    screen.blit(floor,floorect)
    screen.blit(tank,tankrect)
    screen.blit(tank2,tank2rect)
    
    
    pygame.display.flip()
    
pygame.quit()
 