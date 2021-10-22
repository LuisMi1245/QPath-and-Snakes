import pygame

from components import text_objects 
pygame.font.init()

#Defino una unidad de medida fija de 21px
bloque = 21

#Rutas de fuentes
font_path_1 = "assets/fonts/RampartOne-Regular.ttf"
font_path_2 = "assets/fonts/Woodstamp.otf"


size = (59*bloque, 33*bloque) #Width * Height

#Se genera un objeto superficie llamado screen donde se pondrán los elementos
screen = pygame.display.set_mode(size)
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#Se generan superficies hijas que se superponen con screen
head = pygame.Surface.subsurface(screen, (0,0, 59*bloque, 5*bloque))
body = pygame.Surface.subsurface(screen, (0,5*bloque, 59*bloque, 20*bloque))
footer = pygame.Surface.subsurface(screen, (0, 25*bloque, 59*bloque, 8*bloque))

#Se generan superficies hijas de 2 nivel

#head 
#Cargar logo del Header
header_logo = pygame.image.load("assets/img/header_logo.png") 
#Fijar logo en el centro del header 
header_logo = pygame.transform.scale(header_logo, (33*bloque,4*bloque))
rect_header_logo = header_logo.get_rect()
rect_header_logo.center = (59*bloque/2,5*bloque/2)
#head_text, head_text_rect = text_objects("QPath & Snakes", 40, font_path_1)

#body
body_tablero = pygame.Surface.subsurface(body, (0,0, 36*bloque, 20*bloque)) 
body_info = pygame.Surface.subsurface(body, (37*bloque,0, 22*bloque, 20*bloque)) 

#foot
foot_circuit = pygame.Surface.subsurface(footer, (0, 0, 36*bloque, 8*bloque))
foot_buttons = pygame.Surface.subsurface(footer, (37*bloque, 0, 22*bloque, 8*bloque))