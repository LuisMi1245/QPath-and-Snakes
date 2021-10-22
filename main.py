import sys, os, pygame
import numpy as np
from surfaces import *
from components import *
from circuit import *

def jugar(): 
    print("hola")
    global menu_state
    menu_state = 1

def salir(): sys.exit()

def superponer_dado():
    print("Definan esta función")

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
pygame.display.set_caption("QPath & Snakes v0.1")

#Variable Global que controla el estado del menú
menu_state = 0

posx = 2*bloque
posy = 19*bloque

#Circuito imagen
qc_circuit = StartCircuit()
qc_circuit = AssembleCircuit(qc_circuit, 'Rx')
DrawCircuit(qc_circuit, 1)
img_circuit = pygame.image.load("__stored_img__/circuit.png")

#Grafico
plot_qc(qc_circuit)

img_plot = pygame.image.load("__stored_img__/plot_qcc.png")


#Ciclo que mantiene la ejecución del juego
while True:

    #Ciclo (seguramente asíncrono) que verifica el evento de presionar el botón de cerrar ventana y dispara una orden
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            os.remove("__stored_img__/circuit.png")
            os.remove("__stored_img__/plot_qcc.png") 
            sys.exit() #Le ordena al sistema a cerrar la ventana
    

    #Borra la pantalla y la pinta de blanco en cada frame
    screen.fill(color_white)
    
    head.blit(header_logo, rect_header_logo)
    #head.fill(color_orange)
    body_tablero.fill(color_snake_complement)
    foot_buttons.fill(color_orange)
    foot_circuit.fill(color_orange)
    pygame.draw.rect(body_info, color_green, (0, 0, 22*bloque, 20*bloque), border_top_left_radius=10)
    #foot_buttons.fill(color_orange)
    footer.blit(img_circuit,(0,0))
    body_info.blit(img_plot,(11*bloque,0*bloque))


    if menu_state == 0:
        button(foot_buttons, 2*bloque, 2*bloque, 8*bloque, 4*bloque, color_snake_complement, "Iniciar", 43, color_white, action=jugar)
        button(foot_buttons, 12*bloque, 2*bloque, 8*bloque, 4*bloque, color_snake_complement, "Salir", 43, color_white, action=salir)
        
        cuadricula(4*bloque, 0*bloque, 4*bloque, 4*bloque, (5,7), body_tablero, borde=10)
        red_celda = cuadricula(0, 0, 4*bloque, 4*bloque, (5,1), body_tablero, color_red)
        green_celda = cuadricula(32*bloque, 0, 4*bloque, 4*bloque, (5,1), body_tablero, color_green)
        #print(green_celda[0][0])
    elif menu_state == 1:
        button(foot_buttons, 2*bloque, 2*bloque, 18*bloque, 4*bloque, color_snake_complement, "Superponer estados del Dado", 43, color_white, action=superponer_dado())

    #pygame.draw.circle(surface, color, centro, radio, ancho_borde)
    #pygame.draw.circle(screen, color_red, (posx+ 0.5*bloque, posy+ 0.5*bloque), bloque*0.5),
    #pygame.draw.circle(screen, color_white, (posx + 2.5*bloque, posy + 2.5*bloque), bloque*0.5)

    #Hace que todo lo que se dibuje en la superficie en cada frame se vuelva visible
    pygame.display.flip()

