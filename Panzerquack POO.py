import sys
import pygame
from math import cos, sin, pi, tan, radians
import time 
from random import randint
from pygame.locals import *

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

        #definición de texturas 
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
    def __init__(self, x, y, imagen):
        
        
        self.x=x
        self.y=y
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.width = self.imagen.get_width()
        self.height = self.imagen.get_height()
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
        screen.blit(player1.imagen, player1.rect)
        screen.blit(player2.imagen, player2.rect)

    def setVel(self,x):
        self.vel=x
    def setAng(self,y):
        self.ang=y

        
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
        """
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
    """
        rectangulobala = bullet_default.get_rect()
        #posicionY = Player.y-10
        #posicionX = Player.x+5
        rectangulobala = rectangulobala.move(1,1)
        #self.rect = self.rect.move(1,1) #velocidad del rect
        #velocidad i modifica la intensidad del disparo
        velocidadi = self.vel
        angulo= self.ang
        posicionX=self.rect.x
        posicionY=self.rect.y
        #velocidad iY e iX modifican el angulo de disparo
        velocidadiY = velocidadi * sin(radians(angulo))
        velocidadiX = velocidadi * cos(radians(angulo))
        ti = 0
        aux=0
        
        while posicionY < 545 and posicionX<800:
            time.sleep(0.01)
            posicionX = posicionX + velocidadiX * ti
            posicionY = posicionY - velocidadiY * ti +(1/2)*6*(ti**2)
            velocidadY = velocidadiY - (6 * ti)
            velocidadX = velocidadiX - (6 * ti)
            # ti modifica la velocidad del tiro
            ti += 0.01  
            screen.blit(self.imagen,(posicionX,posicionY))
            pygame.display.flip()
        pygame.display.flip()

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

def texttankI(posicion_Y,posicion_X,tanque):

    posicionY=600-posicion_Y
    posicionX=posicion_X - tanque.x


    texto3= pygame.font.SysFont("Comic Sans MS",20)
    altura= texto3.render(str(posicionY), 0, ColorMagico)
    #pygame.draw.rect(screen, gray, [15, 550, 100, 30])

    texto4= pygame.font.SysFont("Comic Sans MS",20)
    altura_a= texto4.render("Altura:", 0, ColorMagico)

    texto5= pygame.font.SysFont("Comic Sans MS",20)
    distancia= texto5.render(str(posicionX-5), 0, ColorMagico) # el -5 el por margen de error
    #pygame.draw.rect(screen, gray, [100, 550, 100, 30])

    texto6= pygame.font.SysFont("Comic Sans MS",20)
    distancia_d= texto4.render("Distancia:", 0, ColorMagico)


    screen.blit(altura_a,(15,530))
    screen.blit(altura,(15,550))
    screen.blit(distancia_d,(100,530))
    screen.blit(distancia,(100,550))
    

    return

def texttankD(posicion_Y,posicion_X,tanque):

    posicionY=600-posicion_Y
    posicionX=posicion_X - tanque.x


    texto3= pygame.font.SysFont("Comic Sans MS",20)
    altura= texto3.render(str(posicionY), 0, ColorMagico)
    #pygame.draw.rect(screen, gray, [15, 550, 100, 30])

    texto4= pygame.font.SysFont("Comic Sans MS",20)
    altura_a= texto4.render("Altura:", 0, ColorMagico)

    texto5= pygame.font.SysFont("Comic Sans MS",20)
    distancia= texto5.render(str(-1*posicionX+5), 0, ColorMagico) #el +5 es por margen de error
    #pygame.draw.rect(screen, gray, [100, 550, 100, 30])

    texto6= pygame.font.SysFont("Comic Sans MS",20)
    distancia_d= texto4.render("Distancia:", 0, ColorMagico)


    screen.blit(altura_a,(15,530))
    screen.blit(altura,(15,550))
    screen.blit(distancia_d,(100,530))
    screen.blit(distancia,(100,550))
    

    return

def textbox():
    
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(650, 40, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color("black")
    color = color_inactive
    active = False
    text = ''
    done = False
    aux2=0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if input_box.collidepoint(event.pos):

                    active = not active
                else:
                    active = False

                color = color_active if active else color_inactive
                
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        
                        aux=text
                        aux2=1
                        text = ''

                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                        #pygame.draw.rect(screen, gray, [520, 560, 200, 60])
                    else:
                        text += event.unicode
                        
        

        txt_surface = font.render(text, True, color)

        width = max(100, txt_surface.get_width()+10)
        input_box.w = width

        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

        if aux2==1:
            return aux
        
    

pygame.init()
#PANTALLA
screen_width = 800
screen_height = 600

negro = 0,0,0
ColorMagico = 0,70,70
gray = 127,127,127
blue_sky=0,160,235



screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Panzerquack')

#Tamaño de los recuadros del mapa 
tile_size = 50

#cargar fondo
fondo=pygame.image.load("assets/maps/world.png")

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

#For Player One
img_right = pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
img_right = pygame.transform.scale(img_right, (40, 40))
x_player1=100
y_player1=screen_height-140
player1 = Player(x_player1, y_player1, img_right)
bullet1 = Bullet(1,1,bullet_default,x_player1,y_player1)
#For Player Tow
img_left = pygame.image.load("assets\sprites\PLAYERS\GREEN_R\duck_s.png")
img_left = pygame.transform.scale(img_left, (40, 40))
x_player2=660
y_player2=screen_height-140
player2 = Player(x_player2, y_player2, img_left)
bullet2 = Bullet(1,1,bullet_default,x_player2,y_player2)
#For the text of Vel. and Ang.
texto7= pygame.font.SysFont("Comic Sans MS",16,5)
textvel= texto7.render("Velocidad:", 0, negro)
texto8= pygame.font.SysFont("Comic Sans MS",16,5)
textang= texto8.render("Angulo:", 0, negro)
#Variables auxiliares
run = True   #Variable while principal
auxT=True   #Variable Pantalla de inicio (texto de inicio panzerquak)
turno=0     #Variable control de turnos
win=True    #Variable control de victoria



while run:
    pygame.display.flip()
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed()

    screen.blit(fondo, (0, 0))
    world.draw()
    draw_grid()

    player1.update()

    if auxT == True:  text()

    if turno==10: turno=1
    
    if keys[pygame.K_SPACE]: turno = 10

    if turno!= 0: auxT=False

    if turno == 2:
        print("\nTurno DOS")
        #SE IMORIME TEXTO VELOCIDAD
        screen.blit(textvel,(655, 20))
        temporalvel=int(textbox())
        player2.setVel(-temporalvel)
        #SE BORRA EL TEXTO ANTERIOR 
        pygame.draw.rect(screen, blue_sky, [650, 20, 200, 60])
        #Se imprime el texto angulo
        screen.blit(textang,(655, 20))
        temporalang=int(textbox())
        player2.setAng(-temporalang)

        bullet2 = Bullet(-temporalang,-temporalvel,bullet_default,x_player2,y_player2)
        bullet2.update()
        #Siguente turno
        turno=10
        
        if win == False:
            #victoria()
            run=False

    if turno == 1:
        print("\nTurno UNO")
        #SE IMORIME TEXTO VELOCIDAD
        screen.blit(textvel,(655, 20))
        temporalvel=int(textbox())
        player1.setVel(temporalvel)
        #SE BORRA EL TEXTO ANTERIOR 
        pygame.draw.rect(screen, blue_sky, [650, 20, 200, 60])
        #Se imprime el texto angulo
        screen.blit(textang,(655, 20))
        temporalang=int(textbox())
        player1.setAng(temporalang)
        
        bullet1 = Bullet(temporalang,temporalvel,bullet_default,x_player1,y_player1)
        bullet1.update()
        #Siguente turno
        turno=2

        if win == False:
            #victoria()
            run=False
    pygame.display.update()

pygame.quit()