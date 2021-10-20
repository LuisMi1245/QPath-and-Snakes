import pygame

from components import text_objects 
pygame.font.init()

#Defino una unidad de medida fija de 21px
bloque = 21

#Rutas de fuentes
font_path_1 = "assets/fonts/RampartOne-Regular.ttf"
font_path_2 = "assets/fonts/Woodstamp.otf"

#Dibujo toda la interfaz

size = (48*bloque, 31*bloque) #Width * Height
#Se genera un objeto superficie llamado screen donde se pondrán los elementos
screen = pygame.display.set_mode(size)
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#Se generan superficies hijas que se superponen con screen
head = pygame.Surface.subsurface(screen, (0,0, 48*bloque, 3*bloque))
body = pygame.Surface.subsurface(screen, (0,3*bloque, 48*bloque, 20*bloque))
footer = pygame.Surface.subsurface(screen, (0, 23*bloque, 48*bloque, 8*bloque))

#Se generan superficies hijas de 2 nivel

#head 
head_text, head_text_rect = text_objects("QPath & Snakes", 40, font_path_1)

#body
body_tablero = pygame.Surface.subsurface(body, (0,0, 32*bloque, 20*bloque)) 
body_info = pygame.Surface.subsurface(body, (32*bloque,0, 16*bloque, 20*bloque)) 

#foot
foot_circuit = pygame.Surface.subsurface(footer, (0, 0, 32*bloque, 8*bloque))
foot_buttons = pygame.Surface.subsurface(footer, (32*bloque, 0, 16*bloque, 8*bloque))