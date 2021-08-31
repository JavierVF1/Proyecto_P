 
import pygame
import sys
import time
"""davinshi estuvo aquí"""
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
 
sys.exit()
 