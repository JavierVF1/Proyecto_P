import pygame
from math import cos, sin, pi, tan, radians
import time 
from random import randint

#########################  TANQUE #########################
class Tank(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,imagen,turno,ang,vel):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.turno=turno
        self.ang=ang
        self.vel=vel
    def spawn(self):
        self.rect.move_ip(self.x,self.y)
    def setVel(self,x):
        self.vel=x
    def setAng(self,y):
        self.ang=y

def mapa():
    screen.blit(fondo,fondorect)
    montana =pygame.draw.polygon(screen, gray, [[175,440],[100,500],[250,500]]) #izquierda
    montana2=pygame.draw.polygon(screen, gray, [[673,440],[600,500],[750,500]])
    pygame.draw.polygon(screen, gray, [[175,440],[100,500],[250,500]])    #izquierda
    pygame.draw.polygon(screen, gray, [[673,440],[600,500],[750,500]])

    screen.blit(floor,floorect)

    pygame.draw.polygon(screen, blue_sky, [[350,545],[300,500],[400,500]])
    pygame.draw.polygon(screen, blue_sky, [[500,545],[450,500],[550,500]])

    return montana,montana2

def colision(posicionY,posicionX,flag):
    flag=False

    
    #print("cord x gT", xtanki, "cord y gT",ytanki)


    ##COLICION MONTAÑA IZQUIERDA

    
    if  (490 <= posicionY <= 500) and (100 <= posicionX <= 110): 
        return flag
    if (480 <= posicionY <= 490) and (110 <= posicionX <= 120):
        return flag
    if (470 <= posicionY <= 480) and (120 <= posicionX <= 130):
        return flag
    if (460 <= posicionY <= 470) and (130 <= posicionX <= 140):
        return flag
    if (450 <= posicionY <= 460) and (140 <= posicionX <= 150):
        return flag
    if (440 <= posicionY <= 450) and (150 <= posicionX <= 175):
        return flag
    if (440 <= posicionY <= 450) and (175 <= posicionX <= 200):
        return flag
    if (450 <= posicionY <= 460) and (200 <= posicionX <= 210):
        return flag
    if (460 <= posicionY <= 470) and (210 <= posicionX <= 220):
        return flag
    if (470 <= posicionY <= 480) and (220 <= posicionX <= 230):
        return flag
    if (480 <= posicionY <= 490) and (230 <= posicionX <= 240):
        return flag
    if (490 <= posicionY <= 500) and (240 <= posicionX <= 250):
        return flag


    #COLISION MONTAÑA DERECHA

    if  (490 <= posicionY <= 500) and (600 <= posicionX <= 610): 
        return flag
    if (480 <= posicionY <= 490) and (610 <= posicionX <= 620):
        return flag
    if (470 <= posicionY <= 480) and (620 <= posicionX <= 630):
        return flag
    if (460 <= posicionY <= 470) and (630 <= posicionX <= 640):
        return flag
    if (450 <= posicionY <= 460) and (640 <= posicionX <= 650):
        return flag
    if (440 <= posicionY <= 450) and (650 <= posicionX <= 675):
        return flag
    if (440 <= posicionY <= 450) and (675 <= posicionX <= 700):
        return flag
    if (450 <= posicionY <= 460) and (700 <= posicionX <= 710):
        return flag
    if (460 <= posicionY <= 470) and (710 <= posicionX <= 720):
        return flag
    if (470 <= posicionY <= 480) and (720 <= posicionX <= 730):
        return flag
    if (480 <= posicionY <= 490) and (730 <= posicionX <= 740):
        return flag
    if (490 <= posicionY <= 500) and (740 <= posicionX <= 750):
        return flag


    #COLISION PISO
    if  (500 <= posicionY <= 550) and (0 <= posicionX <= 300): 
        return flag
    if  (500 <= posicionY <= 550) and (400 <= posicionX <= 450): 
        return flag
    if  (500 <= posicionY <= 550) and (550 <= posicionX <= 850): 
        return flag


    #COLISION CAÑONES IZQUEIRDA
    if  (500 <= posicionY <= 510) and (300 <= posicionX <= 310): 
        return flag
    if  (510 <= posicionY <= 520) and (310 <= posicionX <= 320): 
        return flag
    if  (520 <= posicionY <= 530) and (320 <= posicionX <= 330): 
        return flag
    if  (530 <= posicionY <= 540) and (330 <= posicionX <= 340): 
        return flag
    if  (540 <= posicionY <= 550) and (340 <= posicionX <= 350): 
        return flag
    
    if  (540 <= posicionY <= 550) and (350 <= posicionX <= 360): 
        return flag
    if  (530 <= posicionY <= 540) and (360 <= posicionX <= 370): 
        return flag
    if  (520 <= posicionY <= 530) and (370 <= posicionX <= 380): 
        return flag
    if  (510 <= posicionY <= 520) and (380 <= posicionX <= 390): 
        return flag
    if  (500 <= posicionY <= 510) and (390 <= posicionX <= 400): 
        return flag
    


     #COLISION CAÑONES DERECHA
    if  (500 <= posicionY <= 510) and (450 <= posicionX <= 460): 
        return flag
    if  (510 <= posicionY <= 520) and (460 <= posicionX <= 470): 
        return flag
    if  (520 <= posicionY <= 530) and (470 <= posicionX <= 480): 
        return flag
    if  (530 <= posicionY <= 540) and (480 <= posicionX <= 490): 
        return flag
    if  (540 <= posicionY <= 550) and (490 <= posicionX <= 500): 
        return flag
    
    if  (540 <= posicionY <= 550) and (500 <= posicionX <= 510): 
        return flag
    if  (530 <= posicionY <= 540) and (510 <= posicionX <= 520): 
        return flag
    if  (520 <= posicionY <= 530) and (520 <= posicionX <= 530): 
        return flag
    if  (510 <= posicionY <= 520) and (530 <= posicionX <= 540): 
        return flag
    if  (500 <= posicionY <= 510) and (540 <= posicionX <= 550): 
        return flag
    


    #COLISION VICTORIA
    #xtanki,ytanki
    #COLISION PISO
    



def disparo(tanque,xtanki,ytanki,xtankd,ytankd,turno,win): 
    rectangulobala = bala.get_rect()
    posicionY = tanque.y
    posicionX = tanque.x
    rectangulobala = rectangulobala.move(speed)
    
    #velocidad i modifica la intensidad del disparo
    velocidadi = tanque.vel
    angulo= tanque.ang
    #velocidad iY e iX modifican el angulo de disparo
    velocidadiY = velocidadi * sin(radians(angulo))
    velocidadiX = velocidadi * cos(radians(angulo))
    ti = 0

    while posicionY < 545 and posicionX<800:
        posicionX = posicionX + velocidadiX * ti
        posicionY = posicionY - velocidadiY * ti +(1/2)*6*(ti**2)
        velocidadY = velocidadiY - (6 * ti)
        velocidadX = velocidadiX - (6 * ti)
        # ti modifica la velocidad del tiro
        ti += 0.01       

        #colision con montañas
        flag=True
        if flag == True:
            flag=colision(posicionY,posicionX,flag)

            posicion_Y=posicionY
            posicion_X=posicionX 

            if turno == 2:
                if  (ytanki-10 <= posicion_Y <= ytanki+10) and (xtanki-10 <= posicion_X <= xtanki+10): 
                    print("WEON GANASTE POR LA CHUCHA")
                    flag= False
                    win=False
            if turno == 1:
                if  (ytankd-10 <= posicion_Y <= ytankd+10) and (xtankd-10 <= posicion_X <= xtankd+10): 
                    print("WEON GANASTE POR LA CHUCHA")
                    flag= False
                    win=False
            
        #condicion para asegurarnos de que saldra de la funcion cuando colisione
        if flag == False:
            return win  
            

        screen.blit(bala,(posicionX,posicionY))
        pygame.display.flip()
        
        
def SpawnRandom(Sreen_width):
    #     SPAWN RANDOM
    xtanki = randint(10,Sreen_width/2)
    ytanki = 486
    constantesuelo = 0.8

    if xtanki > 90 and xtanki < 167:
        ytanki = ytanki - constantesuelo*(xtanki-90)  
    if xtanki == 167:
        ytanki = 428
    if xtanki > 167 and xtanki < 250:
        ytanki = 428 + constantesuelo*(xtanki-167)
    if xtanki > 290 and xtanki < 340:
        ytanki = ytanki + (xtanki-290)
    if xtanki == 340:
        ytanki = 530
    if xtanki > 340 and xtanki < 400:
        ytanki = 530 - (xtanki-340)

    xtankd=randint(xtanki+Sreen_width/2,Sreen_width-10)
    ytankd = 486

    if xtankd < 748 and xtankd > 665:
        ytankd = ytankd - constantesuelo*(748-xtankd)
    if xtankd == 665:
        ytankd = 428
    if xtankd < 665 and xtankd > 595:
        ytankd = 428 + constantesuelo*(665-xtankd)
    if xtankd < 540 and xtankd > 495:
        ytankd = ytankd + (540-xtankd)
    if xtankd == 495:
        ytankd = 530
    if xtankd < 495 and xtankd > 438:
        ytankd = 530 - (495-xtankd)
    return xtanki,ytanki,xtankd,ytankd


def victoria():

    print(" ")
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    print(" ")
    print("⠀⠟⠑⡄⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣤⣤⣤⣀⡀")
    time.sleep(0.5)
    print("⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀")
    time.sleep(0.5)
    print("⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆")
    time.sleep(0.5)
    print("⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆                               Enorabuena")
    time.sleep(0.5)
    print("⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆")
    time.sleep(0.5)
    print("⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿                     Has Ganado <3 ")
    time.sleep(0.5)
    print("⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉")
    time.sleep(0.5)
    print("⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇")
    time.sleep(0.5)
    print("⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇")
    time.sleep(0.5)
    print("⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇")
    time.sleep(0.5)
    print("⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇")
    time.sleep(0.5)
    print("⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇")
    time.sleep(0.5)
    print("⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃")
    print(" ")
    ("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    print(" ")




gray = 127,127,127
blue_sky=135,206,235
blue_sky=0,170,255

fondo=pygame.image.load("assets/maps/world.png")
fondorect=fondo.get_rect()
fondorect.move_ip(0,0)

floor=pygame.image.load("assets/maps/cp_orange/floor.png")
floorect=floor.get_rect()
floorect.move_ip(0,500)
bala = pygame.image.load("imagen.png")
speed = [1,1]
#rectangulobala = bala.get_rect()


pygame.init()
#ancho y alto
Sreen_width=800
Sreen_height=600

aux=1
while aux==1:
    xtanki = 0
    ytanki = 0
    xtankd = 0
    ytankd = 0
    xtanki,ytanki,xtankd,ytankd=SpawnRandom(Sreen_width)
    aux=2


size = Sreen_width, Sreen_height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Panzerquack")



run=True
turno=0
contador=0
win=True
while run:
    
    pygame.display.flip()
    
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run=False
    keys=pygame.key.get_pressed()


    tank_g=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
    tank_r=pygame.image.load("assets\sprites\PLAYERS\GREEN_R\duck_s.png")
    tank_gc=Tank(xtanki,ytanki,10,10,tank_g,1,10,10)
    tank_rc=Tank(xtankd,ytankd,10,10,tank_r,2,10,10)
    
    montana,montana2=mapa()

    tank_gc.spawn()
    screen.blit(tank_gc.imagen,tank_gc.rect)
    tank_rc.spawn()
    screen.blit(tank_rc.imagen,tank_rc.rect)
    
    
    if keys[pygame.K_SPACE]: turno = 1
    if turno==10: turno=1
    
    if turno == 2:
        pygame.display.flip()

        print("Truno DOS")
        x=float(input("ingrese la velocidad:"))
        tank_rc.setVel(-x)
        y=float(input("ingrese el angulo:"))
        tank_rc.setAng(-y)
        
        win=disparo(tank_rc,xtanki,ytanki,xtankd,ytankd,turno,win)
        pygame.display.flip()
        turno=10
        if win == False:
            victoria()
            run=False
    
    
    if turno == 1:
        pygame.display.flip()

        print("Truno UNO")
        x=float(input("ingrese la velocidad:"))
        tank_gc.setVel(x)
        y=float(input("ingrese el angulo:"))
        tank_gc.setAng(y)


        win=disparo(tank_gc,xtanki,ytanki,xtankd,ytankd,turno,win)
        pygame.display.flip()
        turno=2
        if win == False:
            victoria()
            run=False
    
    