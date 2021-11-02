import sys
import pygame
from math import cos, sin, pi, tan, radians
import time 
from random import randint,choice
from pygame.locals import *


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TTF'
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0,160,235), (0,70,70)
        self.main_menu = MainMenu(self)
        #self.options = OptionsMenu(self)
        self.exit = ExitMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)
            self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()
            g.running=False
            break
        return
            



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.Exitx, self.Exity = self.mid_w, self.mid_h + 50
        self.Panzerx, self.Panzery = self.mid_w, self.mid_h -150
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True 
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            #self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Panzerquack", 50, self.Panzerx, self.Panzery)
            self.game.draw_text("Exit", 20, self.Exitx, self.Exity)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.Exitx + self.offset, self.Exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            

   
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Exit':
                self.game.curr_menu = self.game.Exit
            self.run_display = False



class ExitMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Thanks for Playing', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            #self.game.draw_text('Made by me', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()
            time.sleep(0.01)
            break
        exit()

        




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
                
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

class Player():
    def __init__(self, x, y, imagen):
        self.vida=100
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
    def dmge(self,dmge):
        self.vida-=dmge
        #print(self.vida)
  
class Bullet():
    def __init__(self, ang, vel,imagen,x,y,XTanke2,YTanke2):
        self.ang=ang
        self.vel=vel
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.XTanke2 = XTanke2
        self.YTanke2 = YTanke2

        #print(XTanke2)
        #print(YTanke2)

    def update(self,x_player1,y_player1,x_player2,y_player2,tanque,world,damage):
        key = pygame.key.get_pressed()
        rectangulobala = bullet_default.get_rect()
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
        sustituto=0
        contdmg=1 #contador para evitar que la bala golpee mas de una vez
        while posicionY < 600 and posicionX<800:
            time.sleep(0.01)
            posicionX = posicionX + velocidadiX * ti
            posicionY = posicionY - velocidadiY * ti +(1/2)*6*(ti**2)
            velocidadY = velocidadiY - (6 * ti)
            velocidadX = velocidadiX - (6 * ti)
            # ti modifica la velocidad del tiro
            ti += 0.01  
            flag=True
            flagLimite=True
            win=True
            
            if flag == True:
                
                flagLimite=colision(posicionY,posicionX,flagLimite,world)
                posicion_Y=posicionY
                posicion_X=posicionX 

                if turno == 2:
                    sustituto=texttankD(int(posicion_Y),int(posicion_X),tanque,sustituto)
                    #sustituto=texttankD(int(posicion_Y),int(posicion_X),tanque,sustituto)
                    if  (y_player1 <= posicion_Y <= y_player1+40) and (x_player1 <= posicion_X <= x_player1+40): 
                        if contdmg==1:
                            player1.dmge(damage)
                            print("\n (ノಠ益ಠ)ノ彡  Impacto Confirmado \n")
                            contdmg-=1
                            flag= False
                            
                        if player1.vida<=0:
                            print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                            print("Victoria para Jugador N°2\n")
                            flag= False
                            win=False
                    if aux >= 50:
                        if  (y_player2 <= posicion_Y <= y_player2+40) and (x_player2 <= posicion_X <= x_player2+40):
                            if contdmg==1:
                                player2.dmge(damage)
                                print("\n (ノಠ益ಠ)ノ彡  Impacto Confirmado \n")
                                contdmg-=1
                                flag= False
                                
                            if player2.vida<=0:
                                print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                                print("Victoria para Jugador N°1\n")
                                flag= False
                                win=False

                if turno == 1:
                    
                    sustituto=texttankI(int(posicion_Y),int(posicion_X),tanque,sustituto)
                    if  (y_player2 <= posicion_Y <= y_player2+40) and (x_player2 <= posicion_X <= x_player2+40): 
                        if contdmg==1:
                            player2.dmge(damage)
                            print("\n (ノಠ益ಠ)ノ彡  Impacto Confirmado \n")
                            contdmg-=1
                            flag= False
                            
                        if player2.vida<=0:
                            print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                            print("Victoria para Jugador N°1\n")
                            flag= False
                            win=False
                    if aux >= 50:
                        if  (y_player1 <= posicion_Y <= y_player1+40) and (x_player1 <= posicion_X <= x_player1+40): 
                            if contdmg==1:
                                player1.dmge(damage)
                                print("\n (ノಠ益ಠ)ノ彡  Impacto Confirmado \n")
                                contdmg-=1
                                flag= False
                                
                            if player1.vida<=0:
                                print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                                print("Victoria para Jugador N°2\n")
                                flag= False
                                win=False
                aux+=1

            if flagLimite == False:
                return win

            if flag == False:
                return win

            screen.blit(self.imagen,(posicionX,posicionY))
            time.sleep(0.001)
            pygame.display.flip()

class SelectBala():
    

    def text(bala105,balaPerforante,bala90):

        texto1= pygame.font.SysFont("Comic Sans MS",20)
        Titulo= texto1.render("Selecion de proyectil:", 0, negro)

        texto2= pygame.font.SysFont("Comic Sans MS",20)
        texto105mm= texto2.render("1.- 105mm:       "+str (bala105), 0, ColorMagico)

        texto3= pygame.font.SysFont("Comic Sans MS",20)
        textoPerforante= texto3.render("2.- Perforante: "+str (balaPerforante), 0, ColorMagico)

        texto4= pygame.font.SysFont("Comic Sans MS",20)
        texto90mm= texto4.render("3.- 90mm:         "+str (bala90), 0, ColorMagico)



        screen.blit(Titulo,(570, 100))
        screen.blit(texto105mm,(560, 135))
        screen.blit(textoPerforante,(560, 155))
        screen.blit(texto90mm,(560, 175))

        return


    def textBala():
        
        font = pygame.font.Font(None, 32)
        input_box = pygame.Rect(750, 150, 140, 32)
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
                            auxbala=text
                            aux2=1
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                            pygame.draw.rect(screen, blue_sky, [750, 150, 140, 32])
                        else:
                            if event.unicode == "1" or event.unicode == "2" or event.unicode == "3":
                                text += event.unicode
                            
            txt_surface = font.render(text, True, color)
            width = max(30, txt_surface.get_width()+10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            if aux2==1:
                return auxbala     
#FUNCTIONS
def SpawnRandom(posicionx,posiciony,aux):
    if aux == 1 :
        posicionx = 50*(posiciony+1)+5
        return posicionx
            
    if aux == 2 :
        posiciony = 50*posicionx
        return posiciony      
    
    if aux == 3 :
        posicionx = 50*(posiciony+1)+5
        return posicionx
            
    if aux == 4 :
        posiciony = 50*posicionx
        return posiciony

def colision(posicionY,posicionX,flagLimite,world):
        
        #print(posicionY)
        #print(posicionX)
        
        a=int(posicionY)//50
        b=int(posicionX)//50
        
        if world[a][b] != 0:
            print("\nCOLISION CON TERRENO!!!!!\n")
            
            
            world_data[a][b] = 0
            world = World(world_data)
            screen.blit(fondo, (0, 0))

    
            world.draw()
            

            flagLimite=False
            return flagLimite


        elif  posicionY <= 0  : 
            print("\nLIMITE SUPERIOR ALCANZADO!!!!!\n")
            flagLimite=False
            return flagLimite
        
        elif  posicionX <= 0  : 
            print("\nLIMITE IZQUIERDO ALCANZADO!!!!!\n")
            flagLimite=False
            return flagLimite
        
        elif  posicionX >= 790  : 
            print("\nLIMITE DERECHO ALCANZADO!!!!!\n")
            flagLimite=False
            return flagLimite

def MapaSelect(seleccion):

    world_data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0],
    [2,2,0,0,0,0,0,1,1,0,0,0,0,0,2,2],
    [1,1,2,0,0,0,0,1,1,0,0,0,0,2,1,1],
    [1,1,1,2,0,0,0,1,1,0,0,0,2,1,1,1],
    [1,1,1,1,2,2,0,1,1,0,0,2,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,2,2,1,1,1,1,1]
    ]
    world_data2 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
    [0,0,0,2,2,0,0,1,1,0,0,2,2,0,0,0],
    [0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0],
    [0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0],
    [2,2,2,1,1,0,0,1,1,0,0,1,1,2,2,2],
    [1,1,1,1,1,0,2,1,1,2,0,1,1,1,1,1]
    ]
    world_data3 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,0,2,2,0,0,0,0,0,0,2,0,0,1,1],
    [0,0,2,1,1,2,0,0,0,0,2,1,0,0,1,1],
    [0,0,1,1,1,1,0,0,0,2,1,1,0,0,1,1],
    [2,2,1,1,1,1,2,0,2,1,1,1,2,2,1,1],
    [1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1]
    ]

    if seleccion == 1:
        return world_data

    if seleccion == 2:
        return world_data2

    if seleccion == 3:
        return world_data3

#Función que dibuja las separaciónes del mapa
#esto es para visualizarlo
def draw_grid():
    for line in range(0,20):
        pygame.draw.line(screen, (255, 255, 255),
        (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255),
        (line * tile_size, 0), (line * tile_size, screen_height))

#funciones de texto
def text():

    texto1= pygame.font.SysFont("Comic Sans MS",65)
    Titulo= texto1.render("Panzerquack", 0, ColorMagico)

    texto2= pygame.font.SysFont("Comic Sans MS",20)
    SubTitulo= texto2.render("Presione espacio para comenzar", 0, ColorMagico)

    screen.blit(Titulo,(200,220))
    screen.blit(SubTitulo,(240,310))

    return

def texttankI(posicion_Y,posicion_X,tanque,sustituto):
    
    posicionY=600-posicion_Y-140   #Se le restan 140 de correccion para que la altura comiense en 0
    posicionX=posicion_X - tanque.x

    if sustituto < posicionY :
        sustituto=posicionY
        

    texto3= pygame.font.SysFont("Comic Sans MS",20)
    altura= texto3.render(str(sustituto), 0, ColorMagico)
    #pygame.draw.rect(screen, gray, [15, 550, 100, 30])

    texto4= pygame.font.SysFont("Comic Sans MS",20)
    altura_a= texto4.render("Altura Max:", 0, ColorMagico)

    texto5= pygame.font.SysFont("Comic Sans MS",20)
    distancia= texto5.render(str(posicionX), 0, ColorMagico) # el -5 el por margen de error
    #pygame.draw.rect(screen, gray, [100, 550, 100, 30])

    texto6= pygame.font.SysFont("Comic Sans MS",20)
    distancia_d= texto4.render("Distancia:", 0, ColorMagico)


    pygame.draw.rect(screen, blue_sky, [15, 10, 170, 60])
    screen.blit(altura_a,(15,10))
    screen.blit(altura,(15,30))
    screen.blit(distancia_d,(140,10))
    screen.blit(distancia,(140,30))
    
    return sustituto

def texttankD(posicion_Y,posicion_X,tanque,sustituto):

    posicionY=600-posicion_Y
    posicionX=posicion_X - tanque.x


    if sustituto < posicionY :

        sustituto=posicionY
        
    
    
    texto3= pygame.font.SysFont("Comic Sans MS",20)
    altura= texto3.render(str(sustituto), 0, ColorMagico)
    #pygame.draw.rect(screen, gray, [15, 550, 100, 30])

    texto4= pygame.font.SysFont("Comic Sans MS",20)
    altura_a= texto4.render("Altura:", 0, ColorMagico)

    texto5= pygame.font.SysFont("Comic Sans MS",20)
    distancia= texto5.render(str(-1*posicionX+30), 0, ColorMagico) #el +5 es por margen de error
    #pygame.draw.rect(screen, gray, [100, 550, 100, 30])

    texto6= pygame.font.SysFont("Comic Sans MS",20)
    distancia_d= texto4.render("Distancia:", 0, ColorMagico)


    pygame.draw.rect(screen, blue_sky, [15, 10, 130, 60])
    screen.blit(altura_a,(15,10))
    screen.blit(altura,(15,30))
    screen.blit(distancia_d,(100,10))
    screen.blit(distancia,(100,30))
    
    

    return  sustituto

def textmax(posicion_Y,posicion_X,tanque):

    posicionY=600-posicion_Y
    posicionX=posicion_X - tanque.x


    texto3= pygame.font.SysFont("Comic Sans MS",20)
    altura= texto3.render(str(posicionY), 0, ColorMagico)
    #pygame.draw.rect(screen, gray, [15, 550, 100, 30])

    texto4= pygame.font.SysFont("Comic Sans MS",20)
    altura_a= texto4.render("Altura Maxima:", 0, ColorMagico)

    texto5= pygame.font.SysFont("Comic Sans MS",20)
    distancia= texto5.render(str(posicionX-5), 0, ColorMagico) # el -5 el por margen de error
    #pygame.draw.rect(screen, gray, [100, 550, 100, 30])

    texto6= pygame.font.SysFont("Comic Sans MS",20)
    distancia_d= texto4.render("Distancia Maxima:", 0, ColorMagico)


    pygame.draw.rect(screen, blue_sky, [15, 10, 130, 60])
    screen.blit(altura_a,(15,10))
    screen.blit(altura,(15,30))
    screen.blit(distancia_d,(100,10))
    screen.blit(distancia,(100,30))
    
    

    return

def textbox():
    
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(650, 27, 140, 32)
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
                        pygame.draw.rect(screen, blue_sky, [650, 27, 140, 32])
                    else:
                        if event.unicode=="1"or event.unicode=="2"or event.unicode=="3"or event.unicode=="4"or event.unicode=="5"or event.unicode=="6"or event.unicode=="7"or event.unicode=="8"or event.unicode=="9"or event.unicode=="0":
                                text += event.unicode
                        
        txt_surface = font.render(text, True, color)
        width = max(100, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        if aux2==1:
            return aux
 
g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
    


pygame.init()
#PANTALLA
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Panzerquack')
#Load Background
fondo=pygame.image.load("assets/maps/world.png")
#Colores
negro = 0,0,0
ColorMagico = 0,70,70
gray = 127,127,127
blue_sky=0,160,235
#Tamaño de los recuadros del mapa 
tile_size = 50
mapa = randint(1,3)
#print("el mapa es: ", mapa)   
world_data=MapaSelect(mapa)
world = World(world_data)
screen.blit(fondo, (0, 0))
world.draw()
#draw_grid()
#IMAGES


#Load Background
fondo=pygame.image.load("assets/maps/world.png")
#For Player One
img_right = pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
img_right = pygame.transform.scale(img_right, (40, 40))
#For Player Tow
img_left = pygame.image.load("assets\sprites\PLAYERS\GREEN_R\duck_s.png")
img_left = pygame.transform.scale(img_left, (40, 40))
#For Turns
turn_text=pygame.image.load("assets/Textures/turn_text.png")
turn_text=pygame.transform.scale(turn_text, (120, 50))

if mapa ==1:
    valorestank1 = [[7,0],[7,1],[8,2],[9,3],[10,4],[10,5],[11,6],[6,7]]
    z = choice(valorestank1)
    a = z[0]
    b = z[1]

if mapa == 2:
    valorestank1 = [[10,0],[10,1],[10,2],[7,3],[7,4],[11,6],[5,7]]
    z = choice(valorestank1)
    a = z[0]
    b = z[1]

if mapa == 3:
    valorestank1 = [[10,0],[10,1],[8,2],[7,3],[7,4],[8,5],[10,6],[11,7]]
    z = choice(valorestank1)
    a = z[0]
    b = z[1]

#print("valor elegido: ", z)
#print("valor a: ",a)
#print("valor b :", b)
x_player1= SpawnRandom(a,b,1)
y_player1= SpawnRandom(a,b,2)
player1 = Player(x_player1-50,y_player1-40, img_right)

if mapa == 1:
    i=b
    valorestank2aux = [[6,8],[11,9],[11,10],[10,11],[9,12],[8,13],[7,14],[7,15]]
    valorestank2 = []
    while i<len(valorestank2aux):
        valorestank2.append(valorestank2aux[i])
        i+=1
    z1 = choice(valorestank2)
    c = z1[0]
    d = z1[1]

if mapa == 2:
    i=b
    valorestank2aux = [[5,8],[11,9],[7,11],[7,12],[10,13],[10,14],[10,15]]
    valorestank2 = []
    if b == 7:
        valorestank2.insert(0,[10,15])
        #print("lista: ", valorestank2)
    else:
        while i<len(valorestank2aux):
            valorestank2.append(valorestank2aux[i])
            #print("lista: ", valorestank2)
            i+=1
    z1 = choice(valorestank2)
    c = z1[0]
    d = z1[1]

if mapa == 3:
    i=b
    valorestank2aux = [[10,8],[9,9],[8,10],[7,11],[10,12],[10,13],[5,14],[5,15]]
    valorestank2 = []
    while i<len(valorestank2aux):
        valorestank2.append(valorestank2aux[i])
        i+=1
    z1 = choice(valorestank2)
    c = z1[0]
    d = z1[1]

#print("valor elegido: ", z1)
#print("valor c: ",c)
#print("valor d: ",d)
x_player2=SpawnRandom(c,d,3)
y_player2=SpawnRandom(c,d,4)
player2 = Player(x_player2-50,y_player2-40, img_left)

#For the text of Vel. and Ang.
texto7= pygame.font.SysFont("Comic Sans MS",16,5)
textvel= texto7.render("Velocidad:", 0, negro)
texto8= pygame.font.SysFont("Comic Sans MS",16,5)
textang= texto8.render("Angulo:", 0, negro)
texto9= pygame.font.SysFont("Comic Sans MS",16,5)
#For the text of health
texto10= pygame.font.SysFont("Comic Sans MS",16,5)
texto11= pygame.font.SysFont("Comic Sans MS",16,5)

#BALAS
#Variables Bala player One
bala105_1=3
balaPerforante_1=10
bala90_1=3
#Variables Bala player Tow
bala105_2=3
balaPerforante_2=10
bala90_2=3

#Variables auxiliares
run = True   #Variable while principal
auxT=0   #Variable Pantalla de inicio (texto de inicio panzerquak)
turno=10     #Variable control de turnos
win=True    #Variable control de victoria

while run:
    bala=""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed()

    

    #screen.blit(fondo, (0, 0))
    #world.draw()
    player1.update()
  
  
    
    
    
        
    if turno == 2:
        
        print("Turno DOS")
        while True:
            textvidap2 = texto11.render("Vida: "+str(player2.vida), 0, negro)
            screen.blit(textvidap2,(screen_width*0.9, screen_height*0.85))
            screen.blit(img_left,(screen_width-40,screen_height-50))
            screen.blit(turn_text,(screen_width-120,screen_height-55))
            SelectBala.text(bala105_2,balaPerforante_2,bala90_2)
            bala=SelectBala.textBala()
            if 0 < bala105_2 :
                if int (bala) == 1:
                    bullet_105mm=pygame.image.load("assets/sprites/BULLETS/Bullet105mm.png")
                    bullet_default2=bullet_105mm
                    bala105_2-=1
                    damage=50
                    break

            if  0 < balaPerforante_2 :
                if int (bala) == 2:
                    bullet_perforante=pygame.image.load("assets/sprites/BULLETS/Bulletperforante.png")
                    bullet_default2=bullet_perforante
                    balaPerforante_2-=1
                    damage=40
                    break

            if  0 < bala90_2:
                if int (bala) == 3:
                    bullet_90mm=pygame.image.load("assets/sprites/BULLETS/Bullet90mm.png")
                    bullet_default2=bullet_90mm
                    bala90_2-=1
                    damage=30
                    break

            if  0 == bala105_1 and 0 == balaPerforante_1 and 0 == bala90_1:
                print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                print("Victoria para Jugador N°1\n")
                win=False
                break
           
            
            pygame.draw.rect(screen, blue_sky, [750, 150, 140, 32])

        pygame.draw.rect(screen, blue_sky, [560, 50, 240, 152])
        #SE IMORIME TEXTO VELOCIDAD
        screen.blit(textvel,(655, 5))
        temporalvel=int(textbox())
        if temporalvel>10:
            temporalvel=10
        if temporalvel<-10:
            temporalvel=-10
        player2.setVel(-temporalvel)
        #SE BORRA EL TEXTO ANTERIOR 
        pygame.draw.rect(screen, blue_sky, [650, 5, 200, 60])
        #Se imprime el texto angulo
        screen.blit(textang,(655, 5))
        temporalang=int(textbox())
        player2.setAng(-temporalang)
        bullet2 = Bullet(-temporalang,-temporalvel,bullet_default2,x_player2-20,y_player2-40,x_player1-50,y_player1-40)
        win=bullet2.update(x_player1-50,y_player1-40,x_player2-50,y_player2-40,player2,world_data,damage)
        textvidap2 = texto11.render("Vida: "+str(player2.vida), 0, negro)
        screen.blit(textvidap2,(screen_width*0.9, screen_height*0.85))
        #Siguente turno
        turno=10
        
        if  0 == bala105_1 and 0 == balaPerforante_1 and 0 == bala90_1:
                print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                print("Victoria para Jugador N°1\n")
                win=False
                break

        if win == False:
            #victoria()
            run=False

    if turno == 1:
        
        print("Turno UNO")
        screen.blit(img_right,(screen_width-40,screen_height-50))
        screen.blit(turn_text,(screen_width-120,screen_height-55))
        textvidap1 = texto10.render("Vida: "+str(player1.vida), 0, negro)
        screen.blit(textvidap1,(screen_width*0.9, screen_height*0.85))
        while True:
            SelectBala.text(bala105_1,balaPerforante_1,bala90_1)
            bala=SelectBala.textBala()
            if 0 < bala105_1 :

                if int (bala) == 1:
                    bullet_105mm=pygame.image.load("assets/sprites/BULLETS/Bullet105mm.png")
                    bullet_default=bullet_105mm
                    bala105_1-=1
                    damage=50
                    break

            if  0 < balaPerforante_1 :
                if int (bala) == 2:
                    bullet_perforante=pygame.image.load("assets/sprites/BULLETS/Bulletperforante.png")
                    bullet_default=bullet_perforante
                    balaPerforante_1-=1
                    damage=40
                    break

            if  0 < bala90_1:
                if int (bala) == 3:
                    bullet_90mm=pygame.image.load("assets/sprites/BULLETS/Bullet90mm.png")
                    bullet_default=bullet_90mm
                    bala90_1-=1
                    damage=30
                    break

            if  0 == bala105_1 and 0 == balaPerforante_1 and 0 == bala90_1:
                print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                print("Victoria para Jugador N°2\n")
                win=False
                break
            
            pygame.draw.rect(screen, blue_sky, [750, 150, 140, 32])
            
        pygame.draw.rect(screen, blue_sky, [560, 50, 240, 152])
        #SE IMORIME TEXTO VELOCIDAD
        screen.blit(textvel,(655, 5))
        temporalvel=int(textbox())
        if temporalvel>10:
            temporalvel=10
        if temporalvel<-10:
            temporalvel=-10
        player1.setVel(temporalvel)
        #SE BORRA EL TEXTO ANTERIOR 
        pygame.draw.rect(screen, blue_sky, [650, 5, 200, 60])
        #Se imprime el texto angulo
        screen.blit(textang,(655, 5))
        temporalang=int(textbox())
        player1.setAng(temporalang)
        
        bullet1 = Bullet(temporalang,temporalvel,bullet_default,x_player1-50,y_player1-40,x_player2-50,y_player2-40)
        win=bullet1.update(x_player1-50,y_player1-40,x_player2-50,y_player2-40,player1,world_data,damage)
        textvidap1 = texto10.render("Vida: "+str(player1.vida), 0, negro)
        screen.blit(textvidap1,(screen_width*0.9, screen_height*0.85))
        #Siguente turno
        turno=2

        if  0 == bala105_1 and 0 == balaPerforante_1 and 0 == bala90_1:
            print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
            print("Victoria para Jugador N°2\n")
            win=False
            
        if win == False:
            #victoria()
            run=False
    pygame.display.update()

    if turno==10:
        turno=1
    

pygame.quit()
