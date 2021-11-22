import sys
import pygame
from math import cos, sin, pi, tan, radians,floor
import time 
from random import randint,choice
from pygame.locals import *
import button
#variables importantes
screen_width = 800
screen_height = 800
#Tamaño de los recuadros del mapa 
tile_width =int(screen_width//40)
tile_height=int(screen_height//40)
globala=0 #variable global que define que tipo de bala está seleccionada (no me siento orgulloso)
clock = pygame.time.Clock()
#sonidos
pygame.mixer.init()
soundObj = pygame.mixer.Sound('assets/sound/sfx/quack_sfx.mp3')
#Colores
negro = 0,0,0
ColorMagico = 0,70,70
gray = 127,127,127
blue_sky=0,160,235
#numero players
num_jugadores=2;
class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = screen_width, screen_height
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'TIEWING.TTF'
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0,160,235), (0,70,70)
        self.main_menu = MainMenu(self)
        #self.options = OptionsMenu(self)
        
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)
            self.draw_text('Cargando...', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
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

def textboxConfig(self):
        #create button instances
        exit_img = pygame.image.load('assets/sprites/exit_btn.png').convert_alpha()
        exit_button = button.Button(screen_width*0.0075, screen_height*0.0083, exit_img, 0.3)
    
        font = pygame.font.Font(None, 32)
        input_box = pygame.Rect(screen_width*0.5,screen_height*0.2, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color("black")
        color = color_inactive
        active = False
        text = ''
        done = False
        aux2=0
        while not done:

            if exit_button.draw(self.game.display):
                print('\nExit')
                sys.exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
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
                            pygame.draw.rect(self.game.display, blue_sky, [screen_width*0.8125,screen_height*0.045, 140, 32])
                        else:
                            if event.unicode=="1"or event.unicode=="2"or event.unicode=="3"or event.unicode=="4"or event.unicode=="5"or event.unicode=="6"or event.unicode=="7"or event.unicode=="8"or event.unicode=="9"or event.unicode=="0":
                                    text += event.unicode
                            
            txt_surface = font.render(text, True, color)
            width = max(100, txt_surface.get_width()+10)
            input_box.w = width
            self.game.display.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(self.game.display, color, input_box, 2)
            pygame.display.flip()
            
            self.game.window.blit(self.game.display, (0, 0))
            pygame.display.update()

            if aux2==1:
                return aux
                
class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, self.game.DISPLAY_W*0.025,self.game.DISPLAY_W*0.025 )
        self.offset = - 150

    def draw_cursor(self):
        self.game.draw_text('x', 20, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        #self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.Configx,self.Configy=self.mid_w,self.mid_h+60
        self.Exitx, self.Exity = self.mid_w, self.mid_h + 90
        self.Panzerx, self.Panzery = self.mid_w, self.mid_h -150
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
    def display_menu(self):
        self.run_display = True 
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            #self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            #self.game.draw_text("Comenzar Juego", 20, self.startx, self.starty)
            self.game.draw_text("Panzerquack", 90, self.Panzerx, self.Panzery)
            self.game.draw_text("Comenzar Juego", 30, self.startx, self.starty)
            self.game.draw_text("Configuraciones", 30, self.Configx, self.Configy)
            self.game.draw_text("Salir", 30, self.Exitx, self.Exity)
            flor_img = pygame.image.load('assets/sprites/grass.png')
            #flor_img =pygame.transform.scale(flor_img , (int(screen_width*0.50),int(screen_height*0.50)))
            self.game.display.blit(flor_img, (screen_width*0, screen_height*0.940))
            panzer_img = pygame.image.load('assets/sprites/panzer.png')
            panzer_img =pygame.transform.scale(panzer_img , (int(screen_width*0.50),int(screen_height*0.50)))
            self.game.display.blit(panzer_img, (screen_width*0.200, screen_height*0.550))

            self.draw_cursor()
            self.blit_screen()
        
    def display_config(self):
        self.run_config=True
        while self.run_config:
  
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("configuraciones", 50, self.game.DISPLAY_W/2.5, self.game.DISPLAY_H/10)
            flor_img = pygame.image.load('assets/sprites/grass.png')
            self.game.display.blit(flor_img, (screen_width*0, screen_height*0.940))
            duck_g = pygame.image.load('assets/Textures/duck_1.png')
            duck_g =pygame.transform.scale(duck_g , (int(screen_width),int(screen_height)))
            self.game.display.blit(duck_g, (0, 0))

            a=textboxConfig(self)
            print(a)

            self.blit_screen()
            self.game.reset_keys()
            return
            
            

            
        
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.Configx + self.offset, self.Configy)
                self.state = 'Configuraciones'
            elif self.state == 'Configuraciones':
                self.cursor_rect.midtop=(self.Exitx+self.offset,self.Exity)
                self.state = 'Exit'
            elif self.state=='Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        if self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.Exitx + self.offset, self.Exity)
                self.state = 'Exit'
                #self.cursor_rect.midtop=(self.Configx+self.offset,self.Configy)
                #self.state = 'Configuraciones'
            elif self.state=='Configuraciones':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state='Start'   
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.Configx + self.offset, self.Configy)
                self.state = 'Configuraciones'
            
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Configuraciones':
                self.display_config()
                
            elif self.state == 'Exit':
                sys.exit()
            self.run_display = False

class World():
    def __init__(self, data):
        self.tile_list = []
        #definición de texturas 
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_width, tile_height))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_width)
                    img_rect.y = (row_count * tile_height)
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_width, tile_height))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_width)
                    img_rect.y = (row_count * tile_height)
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
        
    def update(self,player):
        #(draw) player onto screen
        screen.blit(player.imagen, player.rect)
        

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

    def update(self,x_player1,y_player1,x_player2,y_player2,tanque,world,damage,wind,gravity,intensidad_v,intensidad_g):
        key = pygame.key.get_pressed()
        #rectangulobala = bullet_default.get_rect()
        #rectangulobala = rectangulobala.move(1,1)
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
        var_viento=(intensidad_v/10) #variable para aplicar el viento
        while posicionY < screen_height and posicionX<screen_width:
            time.sleep(0.01)
            
            if wind == False and gravity == False:
                posicionX = posicionX + velocidadiX * ti
                posicionY = posicionY - velocidadiY * ti +(1/2)*6*(ti**2)
                velocidadY = velocidadiY - (6 * ti)
                velocidadX = velocidadiX - (6 * ti)
            
            if wind == True and gravity == False:
                posicionX = (posicionX + velocidadiX * ti)+var_viento
                posicionY = (posicionY - velocidadiY * ti +(1/2)*6*(ti**2))+var_viento
                velocidadY = velocidadiY - (6 * ti)
                velocidadX = velocidadiX - (6 * ti)
            
            if wind == False and gravity == True:
                posicionX = posicionX + velocidadiX * ti
                posicionY = posicionY - velocidadiY * ti +(1/2)*intensidad_g*(ti**2)
                velocidadY = velocidadiY - (intensidad_g * ti)
                velocidadX = velocidadiX - (intensidad_g * ti)
            
            if wind == True and gravity == True:
                posicionX = (posicionX + velocidadiX * ti)+var_viento
                posicionY = (posicionY - velocidadiY * ti +(1/2)*intensidad_g*(ti**2))+var_viento
                velocidadY = velocidadiY - (intensidad_g * ti)
                velocidadX = velocidadiX - (intensidad_g * ti)

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
                            screen.fill(blue_sky)
                            world = World(world_data)
                            screen.blit(fondo, (0, 0))
                            world.draw()
                            
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
                                screen.fill(blue_sky)
                                world = World(world_data)
                                screen.blit(fondo, (0, 0))
                                world.draw()
                                
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
                            screen.fill(blue_sky)
                            world = World(world_data)
                            screen.blit(fondo, (0, 0))
                            world.draw()
                            
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
                                screen.fill(blue_sky)
                                world = World(world_data)
                                screen.blit(fondo, (0, 0))
                                world.draw()
                                
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

        screen.blit(Titulo,(screen_width*0.7125, screen_height*0.0066))
        screen.blit(texto105mm,(screen_width*0.7, screen_height*0.035))
        screen.blit(textoPerforante,(screen_width*0.7, screen_height*0.0583))
        screen.blit(texto90mm,(screen_width*0.7, screen_height*0.0816))

        return


    def textBala():
        
        font = pygame.font.Font(None, 32)
        input_box = pygame.Rect(screen_width*0.9375, screen_height*0.05, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color("black")
        color = color_inactive
        active = False
        text = ''
        done = False
        aux2=0
        while not done:

            if restart_button.draw(screen):
                print('\nReStart')
                restar=100
                return restar

            if exit_button.draw(screen):
                print('\nExit')
                sys.exit()
            #event handler
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
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
                            pygame.draw.rect(screen, blue_sky, [screen_width*0.9375, screen_height*0.05, 140, 32])
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
        
        a=int(posicionY)//20
        b=int(posicionX)//20
        #print("\n-y-",a,"__X_",b)
        
        
        if  posicionY < 0  : 
            print("\nLIMITE SUPERIOR ALCANZADO!!!!!\n")
            world = World(world_data)
            screen.blit(fondo, (0, 0))
            world.draw()
            flagLimite=False
            return flagLimite
        
        elif  posicionY <= 0  : 
            print("\nLIMITE INFERIOR ALCANZADO!!!!!\n")
            screen.fill(blue_sky)
            world = World(world_data)
            screen.blit(fondo, (0, 0))
            world.draw()
            flagLimite=False
            return flagLimite
        
        elif  posicionX <= 0  : 
            print("\nLIMITE IZQUIERDO ALCANZADO!!!!!\n")
            screen.fill(blue_sky)
            world = World(world_data)
            screen.blit(fondo, (0, 0))
            world.draw()
            flagLimite=False
            return flagLimite
        
        elif  posicionX > screen_width-10  : 
            print("\nLIMITE DERECHO ALCANZADO!!!!!\n")
            screen.fill(blue_sky)
            world = World(world_data)
            screen.blit(fondo, (0, 0))
            world.draw()
            flagLimite=False
            return flagLimite
            

        elif world[a][b] != 0:
            print("\nCOLISION CON TERRENO!!!!!\n")
            
            if globala == 1:            
                world_data[a][b] = 0
                world_data[a][b+1] = 0
                world_data[a][b-1] = 0
        
            if globala == 2:
                world_data[a][b] = 0
                
            if globala == 3:
                world_data[a][b] = 0
                world_data[a-1][b] = 0

            screen.fill(blue_sky)
            world = World(world_data)
            screen.blit(fondo, (0, 0))
            world.draw()

            flagLimite=False
            return flagLimite

def MapaSelect(seleccion):

    world_data = [
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,0,0,0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,2,1,1],
    [0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,0,0,0,0,0,0,2,2,1,1,1],
    [2,2,0,0,0,0,0,1,1,0,0,0,0,0,2,2,0,0,0,0,2,2,0,0,0,1,1,1,1,0,0,0,0,0,2,1,1,1,1,1],
    [1,1,2,0,0,0,0,1,1,0,0,0,0,2,1,1,2,0,0,2,1,1,0,0,0,1,1,1,1,0,0,0,0,2,1,1,1,1,1,1],
    [1,1,1,2,0,0,0,1,1,0,0,0,2,1,1,1,1,0,0,1,1,1,2,2,2,1,1,1,1,2,2,0,0,1,1,1,1,1,1,1],
    [1,1,1,1,2,2,0,1,1,0,0,2,1,1,1,1,1,2,0,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,2,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    world_data2 = [
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,0,0,2,2,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,2,2,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,0,0,0,0,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,2,1,1,2,0,0,0],
    [0,0,0,0,0,0,0,2,1,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,0,0,1,1,1,1,2,2,2],
    [2,2,2,2,2,0,0,1,1,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1],
    [1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    world_data3 = [
    
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#0
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#1
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#2
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#3
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#4
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#5
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#6
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#7
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#8
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#9
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#10
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#11
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#12
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#13
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#14
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#15
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#16
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#17
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#18
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#19
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#20
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#21
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#22
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#23
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#24
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#25
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#26
    [2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#27
    [1,1,1,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#28
    [1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#29
    [1,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#30
    [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0],#31
    [1,1,1,1,1,1,1,1,1,0,0,0,0,0,2,2,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0],#32
    [1,1,1,1,1,1,1,1,1,0,0,0,0,2,1,1,2,0,0,2,1,1,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,2,0,0],#33
    [1,1,1,1,1,1,1,1,1,0,0,0,2,1,1,1,1,0,0,1,1,1,2,0,0,0,0,0,0,2,2,0,0,1,1,1,1,1,2,2],#34
    [1,1,1,1,1,1,1,1,1,0,0,2,1,1,1,1,1,2,0,1,1,1,1,0,0,0,0,0,0,1,1,2,2,1,1,1,1,1,1,1],#35
    [1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,2,1,1,1,1,2,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1],#36
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1],#37
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#38
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#39
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] #40
    ]

    if seleccion == 1:
        return world_data

    if seleccion == 2:
        return world_data2

    if seleccion == 3:
        return world_data3

#Función que dibuja las separaciónes del mapa
#esto es para visualizarlo
# def draw_grid():
#     for line in range(0,100):
#         pygame.draw.line(screen, (255, 255, 255),
#         (0, line * tile_size), (screen_width, line * tile_size))
#         pygame.draw.line(screen, (255, 255, 255),
#         (line * tile_size, 0), (line * tile_size, screen_height))

#funciones de texto
def text():

    texto1= pygame.font.SysFont("Comic Sans MS",65)
    Titulo= texto1.render("Panzerquack", 0, ColorMagico)

    texto2= pygame.font.SysFont("Comic Sans MS",20)
    SubTitulo= texto2.render("Presione espacio para comenzar", 0, ColorMagico)

    screen.blit(Titulo,(screen_width*0.25,screen_height*0.366))
    screen.blit(SubTitulo,(screen_width*0.3,screen_height*0.5166))

    return

def texttankI(posicion_Y,posicion_X,tanque,sustituto):
    
    posicionY=screen_height-posicion_Y   #Se le restan 140 de correccion para que la altura comiense en 0
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


    pygame.draw.rect(screen, blue_sky, [screen_width*0.01875,screen_height*0.0166, 220, 60])
    screen.blit(altura_a,(screen_width*0.01875,screen_height*0.0166))
    screen.blit(altura,(screen_width*0.01875,screen_height*0.05))
    screen.blit(distancia_d,(screen_width*0.175,screen_height*0.0166))
    screen.blit(distancia,(screen_width*0.175,screen_height*0.05))
    
    return sustituto

def texttankD(posicion_Y,posicion_X,tanque,sustituto):

    posicionY=screen_height-posicion_Y
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


    pygame.draw.rect(screen, blue_sky, [screen_width*0.01875,screen_height*0.0166, 220, 60])
    screen.blit(altura_a,(screen_width*0.01875,screen_height*0.0166))
    screen.blit(altura,(screen_width*0.01875,screen_height*0.05))
    screen.blit(distancia_d,(screen_width*0.175,screen_height*0.0166))
    screen.blit(distancia,(screen_width*0.175,screen_height*0.05))
    
    

    return  sustituto

def textmax(posicion_Y,posicion_X,tanque):

    posicionY=screen_height-posicion_Y
    posicionX=posicion_X - tanque.x


    texto3= pygame.font.SysFont("Comic Sans MS",20)
    altura= texto3.render(str(posicionY), 0, ColorMagico)
    #pygame.draw.rect(screen, gray, [15, 550, 100, 30])

    texto4= pygame.font.SysFont("Comic Sans MS",20)
    altura_a= texto4.render("Altura Maxima:", 0, ColorMagico)

    texto5= pygame.font.SysFont("Comic Sans MS",20)
    distancia= texto5.render(str(posicionX-5), 0, ColorMagico) # el -5 el por margen de error
    #pygame.draw.rect(screen, gray, [100, 550, 100, 30])
    # texto6= pygame.font.SysFont("Comic Sans MS",20)
    distancia_d= texto4.render("Distancia Maxima:", 0, ColorMagico)
    pygame.draw.rect(screen, blue_sky, [screen_width*0.01875,screen_height*0.0166, 220, 60])
    screen.blit(altura_a,(screen_width*0.01875,screen_height*0.0166))
    screen.blit(altura,(screen_width*0.01875,screen_height*0.05))
    screen.blit(distancia_d,(screen_width*0.175,screen_height*0.0166))
    screen.blit(distancia,(screen_width*0.175,screen_height*0.05))
    return

def textbox():
        
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(screen_width*0.8125,screen_height*0.045, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color("black")
    color = color_inactive
    active = False
    text = ''
    done = False
    aux2=0
    while not done:

        if restart_button.draw(screen):
            print('\nReStart')
            restar=100
            return restar

        if exit_button.draw(screen):
            print('\nExit')
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
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
                        pygame.draw.rect(screen, blue_sky, [screen_width*0.8125,screen_height*0.045, 140, 32])
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
    
   #imagenes de balas
bullet_105mm=pygame.image.load("assets/sprites/BULLETS/Bullet105mm.png")
bullet_perforante=pygame.image.load("assets/sprites/BULLETS/Bulletperforante.png")
bullet_90mm=pygame.image.load("assets/sprites/BULLETS/Bullet90mm.png")
fondo=pygame.image.load("assets/maps/world.png")
    #For Player One / Green
img_right = pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s.png")
img_right = pygame.transform.scale(img_right, (tile_width,tile_height))
img_right_l = pygame.image.load("assets\sprites\PLAYERS\GREEN_P\duck_s_L.png") #Efecto espejo
    #For Player Tow  / Red
img_left = pygame.image.load("assets\sprites\PLAYERS\GREEN_R\duck_s.png")
img_left = pygame.transform.scale(img_left, (tile_width,tile_height))
img_left_l = pygame.image.load("assets\sprites\PLAYERS\GREEN_R\duck_s_L.png")#Efecto espejo
    #For Player Blue
img_Pblue = pygame.image.load("assets\sprites\PLAYERS\GREEN_B\duck_s.png")
img_Pblue = pygame.transform.scale(img_Pblue, (tile_width,tile_height))
img_Pblue_l = pygame.image.load("assets\sprites\PLAYERS\GREEN_B\duck_s_L.png")#Efecto espejo
 #For Player Purple
img_Ppurple = pygame.image.load("assets\sprites\PLAYERS\GREEN_Pu\duck_s.png")
img_Ppurple = pygame.transform.scale(img_Ppurple, (tile_width,tile_height))
img_Ppurple_l = pygame.image.load("assets\sprites\PLAYERS\GREEN_Pu\duck_s_L.png")#Efecto espejo
 #For Player White
img_Pwhite = pygame.image.load("assets\sprites\PLAYERS\GREEN_W\duck_s.png")
img_Pwhite = pygame.transform.scale(img_Pwhite, (tile_width,tile_height))
img_Pwhite_l = pygame.image.load("assets\sprites\PLAYERS\GREEN_W\duck_s_L.png")#Efecto espejo
#For Player Yellow
img_Pyellow = pygame.image.load("assets\sprites\PLAYERS\GREEN_Y\duck_s.png")
img_Pyellow = pygame.transform.scale(img_Pyellow, (tile_width,tile_height))
img_Pyellow_l = pygame.image.load("assets\sprites\PLAYERS\GREEN_Y\duck_s_L.png")#Efecto espejo
    #For Turns
turn_text=pygame.image.load("assets/Textures/turn_text.png")
turn_text=pygame.transform.scale(turn_text, (int(screen_width*0.15),int(screen_height*0.0833)))
######IMAGENES MAPA############
dirt_img =pygame.image.load("assets/textures/grassCenter.png")
grass_img = pygame.image.load("assets/textures/grass.png")
dirt_cliff=pygame.image.load("assets/textures/grassHillLeft.png")
dirt_cliff2 = pygame.transform.flip(dirt_cliff, True, False)
grass_corner=pygame.image.load("assets/textures/grassHillLeft2.png")
grass_corner2 = pygame.transform.flip(grass_corner, True, False)
#For the text of Vel. and Ang.
texto7= pygame.font.SysFont("Comic Sans MS",16,5)
textvel= texto7.render("Velocidad:", 0, negro)
texto8= pygame.font.SysFont("Comic Sans MS",16,5)
textang= texto8.render("Angulo:", 0, negro)
texto9= pygame.font.SysFont("Comic Sans MS",16,5)
#For the text of health
texto10= pygame.font.SysFont("Comic Sans MS",16,5)
texto11= pygame.font.SysFont("Comic Sans MS",16,5)


Master_flag=True

while Master_flag==True:

    pygame.init()
    #PANTALLA
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(blue_sky)
    pygame.display.set_caption('Panzerquack')
    
    pygame.display.update()
    #Seleccionador randomico de mapa 
    mapa = randint(1,3)
    world_data=MapaSelect(mapa)
    world = World(world_data)
    screen.blit(fondo, (0, 0))
    world.draw()
    # draw_grid()
    restart_img = pygame.image.load('assets/sprites/restart_btn.png').convert_alpha()
    exit_img = pygame.image.load('assets/sprites/exit_btn.png').convert_alpha()
    #create button instances
    restart_button = button.Button(screen_width*0.4, screen_height*0.0083, restart_img, 0.3)
    exit_button = button.Button(screen_width*0.5375, screen_height*0.0083, exit_img, 0.3)
    
   
    
    #------------------------------------------------------------------------------------
    #spawn player 1
    if mapa ==1:
        valorestank1 = [[27,0],[27,1],[27,2],[9,3],[10,4],[10,5],[11,6],[6,7]]
        z = choice(valorestank1)
        a = z[0]
        b = z[1]
    if mapa == 2:
        valorestank1 = [[10,0],[10,1],[10,2],[7,3],[7,4],[11,6],[5,7]]
        z = choice(valorestank1)
        a = z[0]
        b = z[1]
    if mapa == 3:
        valorestank1 = [[26,0],[26,1],[26,2],[27,3],[27,4],[27,5],[27,6],[28,7],[29,8],[35,9],[35,10]]
        z = choice(valorestank1)
        a = z[0]
        b = z[1]

    x_player1= SpawnRandom(a,b,1)
    y_player1= SpawnRandom(a,b,2)
    player1 = Player(x_player1,y_player1, img_right)
    #------------------------------------------------------------------------------------
    #spawn player 2
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
        valorestank2aux = [[11,8],[10,9],[9,10],[8,11],[11,12],[12,13],[6,14],[6,15]]
        valorestank2 = []
        while i<len(valorestank2aux):
            valorestank2.append(valorestank2aux[i])
            i+=1
        z1 = choice(valorestank2)
        c = z1[0]
        d = z1[1]

    x_player2=SpawnRandom(c,d,3)
    y_player2=SpawnRandom(c,d,4)
    player2 = Player(x_player2,y_player2, img_left)
    #------------------------------------------------------------------------------------
    
    player3 = Player(x_player1*0.3,y_player1, img_Pblue)
    player4 = Player(x_player1*0.6,y_player1, img_Ppurple)
    player5 = Player(x_player1*0.9,y_player1, img_Pwhite)
    player6 = Player(x_player1*0.12,y_player1, img_Pyellow)

    #BALAS
    #Variables Bala player One
    bala105_1=10
    balaPerforante_1=10
    bala90_1=10
    #Variables Bala player Tow
    bala105_2=10
    balaPerforante_2=10
    bala90_2=10

    #Variables auxiliares
    numero10=10    #valor estatico
    numero100=100  #valor estatico
    run = True   #Variable while principal
    auxT=0   #Variable Pantalla de inicio (texto de inicio panzerquak)
    arregloTurnos=turn_aleat()
    i=0;#valor i usado para turnos (es para evitar que se resetee que esta fuera del while)
    turno=1    #Variable control de turnos
    win=True    #Variable control de victoria
    
    valores_random=[True,False]
    gravedad = choice(valores_random)
    viento = choice(valores_random)
    intensidad_gravedad = randint(0,15)
    print("la gravedad esta activada: ",gravedad) #si no esta activada la gravedad por defecto es 6
    print("la intensidad de la gravedad es de: ",intensidad_gravedad)

    while run:
        bala=""
        clock.tick(30)
        player1.update(player1)
        player2.update(player2) 
    #===========================================================================================================================
        if turno == 2:
            print("el viento esta activado: ", viento)
            print("la intensidad del viento es de: ", intensidad_viento)
            print("Turno DOS")
            screen.blit(img_left,(screen_width*0.95,screen_height*0.9166))
            screen.blit(turn_text,(screen_width*0.85,screen_height*0.9083))
            textvidap2 = texto11.render("Vida: "+str(player2.vida), 0, negro)
            screen.blit(textvidap2,(screen_width*0.9, screen_height*0.88))
            player1.update(player1)
            player2.update(player2)
            while True:
                SelectBala.text(bala105_2,balaPerforante_2,bala90_2)
                bala=SelectBala.textBala()
                #para hacer funcionar el boton reset
                if bala==numero100:
                    break

                if 0 < bala105_2 :
                    if int (bala) == 1:
                        globala=1
                        bullet_default2=bullet_105mm
                        bala105_2-=1
                        damage=50
                        break
                if  0 < balaPerforante_2 :
                    if int (bala) == 2:
                        globala=2
                        bullet_default2=bullet_perforante
                        balaPerforante_2-=1
                        damage=40
                        break
                if  0 < bala90_2:
                    if int (bala) == 3:
                        globala=3
                        bullet_default2=bullet_90mm
                        bala90_2-=1
                        damage=30
                        break
                if  0 == bala105_2 and 0 == balaPerforante_2 and 0 == bala90_2:
                    print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                    print("Victoria para Jugador N°1\n")
                    win=False
                    break

            #para hacer funcionar el boton reset
            if bala==numero100:
                break 
            
            pygame.draw.rect(screen, blue_sky, [screen_width*0.7, screen_height*0, 340, 152])
            #SE IMORIME TEXTO VELOCIDAD
            screen.blit(textvel,(screen_width*0.818, screen_height*0.0083))
            temporalvel=int(textbox())
                #para hacer funcionar el boton reset
            if temporalvel==numero100:
                break    

            if temporalvel>numero10:
                temporalvel=numero10
            if temporalvel<-numero10:
                temporalvel=-numero10
            player2.setVel(-temporalvel)
            #SE BORRA EL TEXTO ANTERIOR 
            pygame.draw.rect(screen, blue_sky, [screen_width*0.8125, screen_height*0.0083, 200, 60])
            #Se imprime el texto angulo
            screen.blit(textang,(screen_width*0.81875, screen_height*0.0083))
            temporalang=int(textbox())
                #para hacer funcionar el boton reset
            if temporalang==numero100:
                break    

            player2.setAng(-temporalang)
            pygame.draw.rect(screen, blue_sky, [screen_width*0.7, screen_height*0, 340, 152])

            textvidap2 = texto11.render("Vida: "+str(player2.vida), 0, negro)
            screen.blit(textvidap2,(screen_width*0.9, screen_height*0.88))

            bullet2 = Bullet(-temporalang,-temporalvel,bullet_default2,x_player2,y_player2,x_player1,y_player1)
            win=bullet2.update(x_player1,y_player1,x_player2,y_player2,player2,world_data,damage,viento,gravedad,intensidad_viento,intensidad_gravedad)
            
            #borra texto max atura, vel
            pygame.draw.rect(screen, blue_sky, [screen_width*0.018, screen_height*0.0166, 220, 60])
            
            # screen.fill(blue_sky)
            world = World(world_data)
            screen.blit(fondo, (0, 0))
            world.draw()

            #Siguente turno
            turno=1
            
            if  0 == bala105_1 and 0 == balaPerforante_1 and 0 == bala90_1:
                    print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                    print("Victoria para Jugador N°1\n")
                    win=False

            if win == False:
                #victoria()
                run=False
    #===========================================================================================================================
        intensidad_viento = randint(-10,10)

        if turno == 1:
            player1.update(player1)
            player2.update(player2)  
            print("el viento esta activado: ", viento)
            print("la intensidad del viento es de: ", intensidad_viento)
            print("Turno UNO")
            screen.blit(img_right,(screen_width*0.95,screen_height*0.9166))
            screen.blit(turn_text,(screen_width*0.85,screen_height*0.9083))
            textvidap1 = texto10.render("Vida: "+str(player1.vida), 0, negro)
            screen.blit(textvidap1,(screen_width*0.9, screen_height*0.88))

            while True:
                SelectBala.text(bala105_1,balaPerforante_1,bala90_1)
                bala=SelectBala.textBala()
                #para hacer funcionar el boton reset
                if bala==numero100:
                    break

                if 0 < bala105_1 :
                    if int (bala) == 1:
                        globala=1
                        bullet_default=bullet_105mm
                        bala105_1-=1
                        damage=50
                        break
                if  0 < balaPerforante_1 :
                    if int (bala) == 2:
                        globala=2
                        bullet_default=bullet_perforante
                        balaPerforante_1-=1
                        damage=40
                        break
                if  0 < bala90_1:
                    if int (bala) == 3:
                        globala=3
                        bullet_default=bullet_90mm
                        bala90_1-=1
                        damage=30
                        break
                if  0 == bala105_1 and 0 == balaPerforante_1 and 0 == bala90_1:
                    print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                    print("Victoria para Jugador N°2\n")
                    win=False
                    break
                
                
            #para hacer funcionar el boton reset
            if bala==numero100:
                break    

            pygame.draw.rect(screen, blue_sky, [screen_width*0.7, screen_height*0, 340, 152])
            #SE IMORIME TEXTO VELOCIDAD
            screen.blit(textvel,(screen_width*0.818, screen_height*0.0083))
            temporalvel=int(textbox())
                #para hacer funcionar el boton reset
            if temporalvel==numero100:
                break    

            if temporalvel>numero10:
                temporalvel=numero10
            if temporalvel<-numero10:
                temporalvel=-numero10
            player1.setVel(temporalvel)
            #SE BORRA EL TEXTO ANTERIOR 
            pygame.draw.rect(screen, blue_sky, [screen_width*0.8125, screen_height*0.0083, 200, 60])
            #Se imprime el texto angulo
            screen.blit(textang,(screen_width*0.818, screen_height*0.0083))
            temporalang=int(textbox())
                #para hacer funcionar el boton reset
            if temporalang==numero100:
                break    

            player1.setAng(temporalang)
            pygame.draw.rect(screen, blue_sky, [screen_width*0.7, screen_height*0, 340, 152])
            textvidap1 = texto10.render("Vida: "+str(player1.vida), 0, negro)
            screen.blit(textvidap1,(screen_width*0.9, screen_height*0.88))

            bullet1 = Bullet(temporalang,temporalvel,bullet_default,x_player1,y_player1,x_player2,y_player2)
            win=bullet1.update(x_player1,y_player1,x_player2,y_player2,player1,world_data,damage,viento,gravedad,intensidad_viento,intensidad_gravedad)
            
            #borra texto max atura, vel
            pygame.draw.rect(screen, blue_sky, [screen_width*0.018, screen_height*0.0166, 220, 60])
            
            # screen.fill(blue_sky)
            world = World(world_data)
            screen.blit(fondo, (0, 0))
            world.draw()
            
            #Siguente turno
            turno=2

            if  0 == bala105_1 and 0 == balaPerforante_1 and 0 == bala90_1:
                print("\n ༼ つ ◕ _ ◕ ༽つ━━☆ﾟ.*･｡ﾟ\n")
                print("Victoria para Jugador N°2\n")
                win=False
                
            if win == False:
                #victoria()
                run=False   
    #===========================================================================================
        # if turno==3:
        #     print("turno 3")
        #     player3.update(player3) 
        #     screen.fill(blue_sky)
        #     world = World(world_data)
        #     screen.blit(fondo, (0, 0))
        #     world.draw()
        #     if i>6:
        #         i=0
        #     else:
        #         i=i+1
        #     turno=arregloTurnos[i]
        # if turno==4:
        #     print("turno 4")
        #     player4.update(player4) 
        #     screen.fill(blue_sky)
        #     world = World(world_data)
        #     screen.blit(fondo, (0, 0))
        #     world.draw()
        #     if i>6:
        #         i=0
        #     else:
        #         i=i+1
        #     turno=arregloTurnos[i]
        # if turno==5:
        #     print("turno 5")
        #     player5.update(player5) 
        #     screen.fill(blue_sky)
        #     world = World(world_data)
        #     screen.blit(fondo, (0, 0))
        #     world.draw()
        #     if i>6:
        #         i=0
        #     else:
        #         i=i+1
        #     turno=arregloTurnos[i]
        # if turno==6:
        #     print("Turno 6")
        #     player6.update(player6)   
        #     screen.fill(blue_sky)
        #     world = World(world_data)
        #     screen.blit(fondo, (0, 0))
        #     world.draw()
        #     i=0
            
        #     turno=arregloTurnos[i]
    
sys.exit()
