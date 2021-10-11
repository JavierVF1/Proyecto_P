import sys
import pygame
from math import cos, sin, pi, tan, radians
import time 
from random import randint
from pygame.locals import *

pygame.init()
#PANTALLA
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#Tamaño de los recuadros del mapa
tile_size = 50

#cargar fondo

fondo=pygame.image.load("assets/maps/world.png")

#Función que dibuja las separaciónes del mapa
#esto es para visualizarlo
def draw_grid():
    for line in range(0,20):
        pygame.draw.line(screen, (255, 255, 255),
        (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255),
        (line * tile_size, 0), (line * tile_size, screen_height))
#funcion de texto
def text():

    texto1= pygame.font.SysFont("Comic Sans MS",65)
    Titulo= texto1.render("Panzerquack", 0, ColorMagico)

    texto2= pygame.font.SysFont("Comic Sans MS",20)
    SubTitulo= texto2.render("Presione espacio para comenzar", 0, ColorMagico)



    screen.blit(Titulo,(200,220))
    screen.blit(SubTitulo,(240,310))

    return
class World():
    def __init__(self, data):
        self.tile_list = []

        #cargar imagenes para crear mapa
        dirt_img =pygame.image.load("assets/textures/grassCenter.png")
        grass_img = pygame.image.load("assets/textures/grass.png")
        dirt_cliff=pygame.image.load("assets/textures/grassHillLeft.png")
        dirt_cliff2 = pygame.transform.flip(dirt_cliff, True, False)
        grass_corner=pygame.image.load("assets/textures/grassHillLeft2.png")
        grass_corner2 = pygame.transform.flip(grass_corner, True, False)


        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(dirt_cliff, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(dirt_cliff2, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(grass_corner, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(grass_corner2, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
            img_right = pygame.transform.scale(img_right, (40, 40))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def update(self):
        dx = 0
        dy = 0

        #get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5

        #draw player onto screen
        screen.blit(self.image, self.rect)
class Bullet():
    def __init__(self, ang, vel,imagen,x,y):
        self.ang=ang
        self.vel=vel
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.vel -= 1
            print(self.vel ,"\n")
        if key[pygame.K_RIGHT]:
            self.vel += 1
            print(self.vel ,"\n")
        if key[pygame.K_UP]:
            self.ang+=  1
            print(self.ang ,"\n")
        if key[pygame.K_DOWN]:
            self.ang-=  1
            print(self.ang ,"\n")
        if key[pygame.K_SPACE]:
                self.rect = self.rect.move(1,1) #velocidad del rect
                #velocidad i modifica la intensidad del disparo
                velocidadi = self.vel
                angulo= self.ang
                #velocidad iY e iX modifican el angulo de disparo
                velocidadiY = velocidadi * sin(radians(angulo))
                velocidadiX = velocidadi * cos(radians(angulo))
                ti = 0
                aux=0
                
                while self.rect.y < screen_height and self.rect.x<screen_width:
                    time.sleep(0.001)
                    self.rect.x = self.rect.x + velocidadiX * ti
                    self.rect.y = self.rect.y - velocidadiY * ti +(1/2)*6*(ti**2)
                    print(self.rect.y)
                    print(self.rect.x)
                    velocidadY = velocidadiY - (6 * ti)
                    velocidadX = velocidadiX - (6 * ti)
                    # ti modifica la velocidad del tiro
                    ti += 0.001   
                    screen.blit(self.imagen,(self.rect.x,self.rect.y))
        screen.blit(self.imagen, self.rect)

        
world_data = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,3,4,3,4,0,0,3,4,0,0,0],
[2,2,2,4,3,5,6,5,6,4,3,5,6,2,2,2],
[1,1,1,6,5,1,1,1,1,6,5,1,1,1,1,1]
]

world = World(world_data)
bullet_default=pygame.image.load("assets/sprites/BULLETS/Bullet_default.png")
x_player1=100
y_player1=screen_height-140
player = Player(x_player1, y_player1)
bullet = Bullet(1,1,bullet_default,x_player1,y_player1)
run = True
screen.blit(fondo, (0, 0))

while run:

    world.draw()

    draw_grid()
    
    player.update()
    bullet.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()