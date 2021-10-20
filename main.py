import sys, pygame
import numpy as np
from surfaces import *
from components import *

def jugar(): 
    print("hola")
    foot_buttons = pygame.Surface.subsurface(footer, (0, 0, 32*bloque, 8*bloque))
    #button(foot_buttons, 2*bloque, 2*bloque, 12*bloque, 4*bloque, color_snake_complement, "Superponer Dado", 43, color_white, action=None)

def salir(): sys.exit()

#Inicializa los módulos de pygame
pygame.init()

empty_color = pygame.Color(0,0,0,0) 
color_white = np.array((255, 255, 255)) #Color del fondo de la ventana (en RGB)
color_red = np.array((255, 0, 0))
color_green = np.array((0, 217, 94))
color_orange = np.array((252, 186, 3))
color_purple = np.array(( 140, 3, 252))
color_snake = np.array((161, 245, 170))
color_snake_complement = np.array((165, 39, 19))
color_black = np.array((0, 0, 0))

#Título de la ventana
pygame.display.set_caption("QPath & Snakes")

posx = 2*bloque
posy = 19*bloque

#Ciclo que mantiene la ejecución del juego
while True:

    #Ciclo (seguramente asíncrono) que verifica el evento de presionar el botón de cerrar ventana y dispara una orden
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT: sys.exit() #Le ordena al sistema a cerrar la ventana
    

    #Borra la pantalla y la pinta de blanco en cada frame
    screen.fill(color_white)
   
    head.blit(head_text, (16*bloque,0))
    #body_tablero.fill(color_red)
    #body_info.fill(color_purple)
    foot_circuit.fill(color_snake)
    foot_buttons.fill(color_snake)

    button(foot_buttons, 2*bloque, 2*bloque, 5*bloque, 4*bloque, color_snake_complement, "Juega", 43, color_white, action=jugar)
    button(foot_buttons, 9*bloque, 2*bloque, 5*bloque, 4*bloque, color_snake_complement, "Salir", 43, color_white, action=salir)
    

    #pygame.draw.circle(surface, color, centro, radio, ancho_borde)
    #pygame.draw.circle(screen, color_red, (posx+ 0.5*bloque, posy+ 0.5*bloque), bloque*0.5),
    #pygame.draw.circle(screen, color_white, (posx + 2.5*bloque, posy + 2.5*bloque), bloque*0.5)

    #Hace que todo lo que se dibuje en la superficie en cada frame se vuelva visible
    pygame.display.flip()

