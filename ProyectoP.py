import pygame
import sys
import time
from math import pi
 
ejecutando = True
frameRate = 60
frameCount = 0

 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


pygame.init()
 
canvas = pygame.display.set_mode([850, 600],pygame.RESIZABLE)
pygame.display.set_caption("Age of tanks")

 
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global ejecutando
            ejecutando = False
 

def update():
    events()
    pygame.display.flip()
    time.sleep(1/frameRate)
    global frameCount
    frameCount += 1
 
 
def draw():


    pygame.draw.rect(canvas, WHITE, [0, 0, 850, 600])
    pygame.draw.rect(canvas, GREEN, [0, 500, 850, 600])

    pygame.draw.line(canvas, GREEN, [0, 500], [103,500], 5)
    
    pygame.draw.arc(canvas, GREEN,[100,440, 150, 125], pi/2, pi, 100)
    pygame.draw.arc(canvas, GREEN,[100,440, 150, 125], 0, pi/2, 100)

    pygame.draw.line(canvas, GREEN, [300,500], [250,500], 5)

    pygame.draw.arc(canvas, WHITE, [300,453, 100, 90], pi,3*pi/2, 100)
    pygame.draw.arc(canvas, WHITE,  [300,453, 100, 90], 3*pi/2, 2*pi, 100)

    pygame.draw.line(canvas, GREEN, [400,500], [450,500], 5)

    pygame.draw.arc(canvas, WHITE, [450,453, 100, 90], pi,3*pi/2, 100)
    pygame.draw.arc(canvas, WHITE,  [450,453, 100, 90], 3*pi/2, 2*pi, 100)
    
    pygame.draw.line(canvas, GREEN, [550,500], [605,500], 5)

    pygame.draw.arc(canvas, GREEN,[600,440, 150, 125], pi/2, pi, 100)
    pygame.draw.arc(canvas, GREEN,[600,440, 150, 125], 0, pi/2, 100)

    pygame.draw.line(canvas, GREEN, [750, 500], [850,500], 5)
    
  
    

 
while ejecutando:
    draw()
    update()
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()
    


class tank:
    #atributos
        #estos atributos son temporales, hay que pensar bien la estructura del tanque ~JR
    def __init___(self,health,proyectile,speed,angle,color):
        
            self.health=health #Vida del tanque
            
            self.proyectile=proyectile #tipo de proyectil
            #este ultimo puede transformarse en una clase a futuro ~JR
            
            self.speed=speed#Velocidad del tanque
            
            self.angle=angle#Angulo de la torreta
            
            self.color=color#Color del tanque
            #Este color está en formato de texto, debido al uso futuro de los sprites ~JR
            
    #constructores
                    #getters
    def getHealth(self):
        return self.health
    def getProyectile(self):
        return self.proyectile
    def getSpeed(self):
        return self.speed
    def getAngle(self):
        return self.angle
    def getColor(self):
        return self.Color
    
                    #setters
    
    def setHealth(self,health):
        self.health=health
        
    # def setProyectile(self,proyectile):
    #     self.proyectile=proyectile
    # def setSpeed(self,speed):
    #     self.speed=speed
        #estos 2 atributos de momento son estaticos, 
        #puede que se exija a futuro poder modificarlos ~JR
        
    def setAngle(self,angle):
        self.angle=angle
        
    def setColor(self,color):
        self.color=color
        
    #metodos



sys.exit()
 