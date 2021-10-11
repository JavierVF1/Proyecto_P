import sys
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

    if  posicionY <= 0  : 
        print("\nLIMITE SUPERIOR ALCANZADO!!!!!\n")
        return flag
    
    if  posicionX <= 0  : 
        print("\nLIMITE IZQUIERDO ALCANZADO!!!!!\n")
        return flag
    
    if  posicionX >= 800  : 
        print("\nLIMITE DERECHO ALCANZADO!!!!!\n")
        return flag
    


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
    posicionY = tanque.y-10
    posicionX = tanque.x+5
    rectangulobala = rectangulobala.move(speed)
    
    #velocidad i modifica la intensidad del disparo
    velocidadi = tanque.vel
    angulo= tanque.ang
    #velocidad iY e iX modifican el angulo de disparo
    velocidadiY = velocidadi * sin(radians(angulo))
    velocidadiX = velocidadi * cos(radians(angulo))
    ti = 0
    aux=0
    
    while posicionY < 545 and posicionX<800:
        time.sleep(0.001)
        posicionX = posicionX + velocidadiX * ti
        posicionY = posicionY - velocidadiY * ti +(1/2)*6*(ti**2)
        velocidadY = velocidadiY - (6 * ti)
        velocidadX = velocidadiX - (6 * ti)
        # ti modifica la velocidad del tiro
        ti += 0.01       

        
        flag=True
        if flag == True:
            #condicion para asegurarnos de que saldra de la funcion cuando colisione
            flag=colision(posicionY,posicionX,flag)

            posicion_Y=posicionY
            posicion_X=posicionX 
            
            
            #text2(int(posicion_Y),int(posicion_X),tanque)
           

            if turno == 2:
                texttankD(int(posicion_Y),int(posicion_X),tanque)

                if  (ytanki-10 <= posicion_Y <= ytanki+10) and (xtanki-10 <= posicion_X <= xtanki+10): 
                    print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                    print("Victoria para Jugador N°2\n")
                    flag= False
                    win=False

                if aux >= 40:
                    if  (ytankd-10 <= posicion_Y <= ytankd+10) and (xtankd-10 <= posicion_X <= xtankd+10):  
                        print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                        print("Victoria para Jugador N°1\n")
                        flag= False
                        win=False




            if turno == 1:
                texttankI(int(posicion_Y),int(posicion_X),tanque)
                if  (ytankd-10 <= posicion_Y <= ytankd+10) and (xtankd-10 <= posicion_X <= xtankd+10): 
                    print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                    print("Victoria para Jugador N°1\n")
                    flag= False
                    win=False

                if aux >= 40:
                    if  (ytanki-10 <= posicion_Y <= ytanki+10) and (xtanki-10 <= posicion_X <= xtanki+10): 
                        print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                        print("Victoria para Jugador N°2\n")
                        flag= False
                        win=False
            aux+=1
                
        
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
    pygame.draw.rect(screen, gray, [15, 550, 100, 30])

    texto4= pygame.font.SysFont("Comic Sans MS",20)
    altura_a= texto4.render("Altura:", 0, ColorMagico)

    texto5= pygame.font.SysFont("Comic Sans MS",20)
    distancia= texto5.render(str(posicionX-5), 0, ColorMagico) # el -5 el por margen de error
    pygame.draw.rect(screen, gray, [100, 550, 100, 30])

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
    pygame.draw.rect(screen, gray, [15, 550, 100, 30])

    texto4= pygame.font.SysFont("Comic Sans MS",20)
    altura_a= texto4.render("Altura:", 0, ColorMagico)

    texto5= pygame.font.SysFont("Comic Sans MS",20)
    distancia= texto5.render(str(-1*posicionX+5), 0, ColorMagico) #el +5 es por margen de error
    pygame.draw.rect(screen, gray, [100, 550, 100, 30])

    texto6= pygame.font.SysFont("Comic Sans MS",20)
    distancia_d= texto4.render("Distancia:", 0, ColorMagico)


    screen.blit(altura_a,(15,530))
    screen.blit(altura,(15,550))
    screen.blit(distancia_d,(100,530))
    screen.blit(distancia,(100,550))
    

    return

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
    print("⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆                               Enhorabuena")
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




def textbox():
    
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(520, 560, 140, 32)
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
                        pygame.draw.rect(screen, gray, [520, 560, 200, 60])
                    else:
                        text += event.unicode
                        
        

        txt_surface = font.render(text, True, color)

        width = max(200, txt_surface.get_width()+10)
        input_box.w = width

        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

        if aux2==1:
            return aux
        
    

negro = 0,0,0
ColorMagico = 0,70,70
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

aux=True
while aux==True:
    xtanki = 0
    ytanki = 0
    xtankd = 0
    ytankd = 0
    xtanki,ytanki,xtankd,ytankd=SpawnRandom(Sreen_width)
    aux=False


size = Sreen_width, Sreen_height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Panzerquack")


auxT=True
run=True
turno=0
contador=0
win=True

base_front=pygame.font.Font(None,32)
user_text=""

while run:
    
    pygame.display.flip()
    
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit()
            
    keys=pygame.key.get_pressed()


    tank_g=pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
    tank_r=pygame.image.load("assets\sprites\PLAYERS\GREEN_R\duck_s.png")
    tank_gc=Tank(xtanki,ytanki,10,10,tank_g,1,10,10)
    tank_rc=Tank(xtankd,ytankd,10,10,tank_r,2,10,10)
    
    texto7= pygame.font.SysFont("Comic Sans MS",16,5)
    textvel= texto7.render("Velocidad:", 0, negro)
    texto8= pygame.font.SysFont("Comic Sans MS",16,5)
    textang= texto8.render("Angulo:", 0, negro)

    montana,montana2=mapa()

    if auxT == True: text()
        
    tank_gc.spawn()
    screen.blit(tank_gc.imagen,tank_gc.rect)
    tank_rc.spawn()
    screen.blit(tank_rc.imagen,tank_rc.rect)
    
    if turno==10: turno=1
    
    if keys[pygame.K_SPACE]: turno = 10

    if turno!= 0: auxT=False

    if turno == 2:
        

        print("\nTurno DOS")
        #SE IMORIME TEXTO VELOCIDAD
        screen.blit(textvel,(525, 540))

        temporalx=int(textbox())
        tank_rc.setVel(-temporalx)
        #SE BORRA EL TEXTO ANTERIOR 
        pygame.draw.rect(screen, gray, [520, 540, 200, 60])
        #Se imprime el texto angulo
        screen.blit(textang,(525, 540))

        temporaly=int(textbox())
        tank_rc.setAng(-temporaly)
        
        win=disparo(tank_rc,xtanki,ytanki,xtankd,ytankd,turno,win)
        turno=10
        if win == False:
            #victoria()
            run=False
    
    if turno == 1:
        print("\nTurno UNO")
        #SE IMORIME TEXTO VELOCIDAD
        screen.blit(textvel,(525, 540))

        temporalx=int(textbox())
        tank_gc.setVel(temporalx)

        #SE BORRA EL TEXTO ANTERIOR 
        pygame.draw.rect(screen, gray, [520, 540, 200, 60])

        #Se imprime el texto angulo
        screen.blit(textang,(525, 540))
        
        temporaly=int(textbox())
        tank_gc.setAng(temporaly)
       
        win=disparo(tank_gc,xtanki,ytanki,xtankd,ytankd,turno,win)
        turno=2
        if win == False:
            #victoria()
            run=False
    
pygame.quit()
    