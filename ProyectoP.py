 
import pygame
import sys
import time

ejecutando = True
frameRate = 60
frameCount = 0
 
pygame.init()
 
canvas = pygame.display.set_mode([800, 600],pygame.RESIZABLE)
 
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
    pygame.draw.rect(canvas, [frameCount % 255, 0, 200], [0, 0, 800, 600])
 
while ejecutando:
    draw()
    update()

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
 