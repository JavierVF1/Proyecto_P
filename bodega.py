# #########################  SHELL #########################
# class Shell(pygame.sprite.Sprite):
#     def __init__(self,imagen):
#         self.imagem=imagen
#         self.rect=self.imagen.get_rect()
#     def pos(self,x,y):
#         self.x=x
#         self.y=y
#########################  TORRETA #########################
#class Turret(pygame.sprite.Sprite):
#    def __init__(self,vel,ang):
#        # self.imagen=imagen
#        # self.rect=self.imagen.get_rect()
#        self.vel=vel
#        self.ang=ang
#        self.rect.top=10
#        self.rect.left=20
            



#########################  TANQUE #########################

        # if keys[pygame.K_SPACE]:
        #     disparo()
    #codigo para despues, cuando pidan movimiento será util ~JR
    # def boundaries(self):
    #     if self.rect.move <0:
    #         self.rect.move(2,0)
    #     if self.rect.move > 600:
    #         self.rect.move(-2,0)
        
#########################  MAPA #########################
# class Map(pygame.sprite.Sprite):
#     def __init__(self,imagen,turno):
#         self.imagen=imagen
#         self.rect=self.imagen.get_rect()
#         self.turno_map=turno_map
#         self.rect.top=800
#         self.rect.left=600
#         # self.gravityt=gravity
#     def turno(self,Tank):
#         if Tank.turno==self.turno_map:
#             Tank.move=True
#         else:
#             Tank.move=False
#     # def gravedad(self,gravedad):
#     #     self.gravedad=gravedad
#     #     Tank.rect
##########################################################
    #tank obj
    #ejemplo para futuro:
    #tank_x=pygame.image.load("assets\Sprites\PLAYERS\X_P\duck_s.png)
    #El comando de arriba quiere decir que se cargara la imagen duck_s (duck still), que se usara...
    #en la creación del tanque
    #tank_xc=Tank(x,y,width,height,tank_x,turno)
    #este de aquí arriba es el objeto tank
    #tiene coordenadas x e y que serán su punto de spawn
    #un ancho y alto
    #un sprite tank_x
    #y finalmente un numero de turno que debiese ser modificado manualmente
        #tank green

        #tank red
    # tank_r=pygame.image.load("assets\sprites\PLAYERS\RED_P\duck_s.png")


    
# def disparo(self):
    #     speed = [1,1]
    #     ti = 0
    #     bala = pygame.image.load("imagen.png")
    #     rectangulobala = bala.get_rect()
    #     rectangulobala = rectangulobala.move(speed)
    #     velocidadiY = self.vel * sin(self.ang)
    #     velocidadiX = self.vel * cos(self.ang) 
    #     if posicionX < 900:
    #         posicionX = posicionX + velocidadiX * ti
    #         posicionY = posicionY - velocidadiY * ti +(1/2)*6*(ti**2)
    #         velocidadY = velocidadiY - (6 * ti)
    #         # ti modifica la velocidad del tiro
    #         ti += 0.001
    
    # if posicionX < 900:
    #     posicionX = posicionX + velocidadiX * ti
    #     posicionY = posicionY - velocidadiY * ti +(1/2)*6*(ti**2)
    #     velocidadY = velocidadiY - (6 * ti)
    #     # ti modifica la velocidad del tiro
    #     ti += 0.01



        
        """
        if posicionY in range (490,500) and posicionX in range (100,110):
            print("BOOM!")
            break
        if posicionY in range (480,490) and posicionX in range (110,120):
            print("BOOM!")
            break
        if posicionY in range (470,480) and posicionX in range (120,130):
            print("BOOM!")
            break
        if posicionY in range (460,470) and posicionX in range (130,140):
            print("BOOM!")
            break
        if posicionY in range (450,460) and posicionX in range (140,150):
            print("BOOM!")
            break
        if posicionY in range (440,450) and posicionX in range (150,175):
            print("BOOM!")
            break
        if posicionY in range (440,450) and posicionX in range (175,200):
            print("BOOM!")
            break
        if posicionY in range (450,460) and posicionX in range (200,210):
            print("BOOM!")
            break
        if posicionY in range (460,470) and posicionX in range (210,220):
            print("BOOM!")
            break
        if posicionY in range (470,480) and posicionX in range (220,230):
            print("BOOM!")
            break
        if posicionY in range (480,490) and posicionX in range (230,240):
            print("BOOM!")
            break
        if posicionY in range (490,500) and posicionX in range (240,250):
            print("BOOM!")
            break
        """

        if posicionY in range ((490,500),(480,490),(470,480)) and posicionX in range ((100,110),(110,120),(120,130)):
            print("BOOM!")
            return
        if posicionY in range ((460,470),(450,460),(440,450)) and posicionX in range ((130,140),(140,150),(150,175)):
            print("BOOM!")
            return
        
        if posicionY in range ((440,450),(450,460),(460,470)) and posicionX in range ((175,200),(200,210),(210,220)):
            print("BOOM!")
            return
        if posicionY in range ((470,480),(480,490),(490,500)) and posicionX in range ((175,200),(200,210),(210,220)):
            print("BOOM!")
            return



    """print(" ༼ つ ◕_◕ ༽つ━━☆ﾟ.*･｡ﾟ")
    print("")
    print("")
    print("⠀⠟⠑⡄⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣤⣤⣤⣀⡀")
    print("⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀")
    print("⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆                     Enorabuena")
    print("⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆")
    print("⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆          Has Ganado <3 ")
    print("⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿")
    print("⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉")
    print("⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇")
    print("⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇")
    print("⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇")
    print("⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇")
    print("⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇")
    print("⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃")    """
    