import sys, os, pygame
import numpy as np
from surfaces import *
from components import *
from circuit import *
from Dado import *

def jugar(): 
    global menu_state
    menu_state = 1
    
def salir(): sys.exit()

def superponer_dado():
    global resultado_decimal
    global img_dado_res
    global num_movimientos

    #dibujar fichas
    #pygame.draw.circle(screen, color_red, (posx+ 0.5*bloque, posy+ 0.5*bloque), bloque*0.5),
    #pygame.draw.circle(screen, color_white, (posx + 2.5*bloque, posy + 2.5*bloque), bloque*0.5)

    resultado_binario = dice(qc_dado) 
    resultado_decimal = binario_a_decimal(resultado_binario)
    
    num_movimientos +=1
    
    img_dado_res = pygame.image.load("__stored_img__/im_dado.png")
    
    #mover fichas
    mover_jugador()

#Jugador 1 es impar
#Jugador 2 es par
def mover_jugador():
    global resultado_decimal, jugador, jugador_position_1, jugador_position_2

    if num_movimientos % 2 != 0:
        jugador = 1
        jugador_position_1 = resultado_decimal
    else: 
        jugador = 2
        jugador_position_2 = resultado_decimal


def binario_a_decimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal


def draw_pointer(player, x, y):
    if player == 1:
        pygame.draw.circle(body_tablero, color_purple, (x, y), 1*bloque, 0)
    else:
        pygame.draw.circle(body_tablero, color_black, (x, y), 1*bloque, 0)


#Inicializa los módulos de pygame
pygame.init()

clock = pygame.time.Clock()
empty_color = pygame.Color(0,0,0,0) 
color_white = np.array((255, 255, 255)) #Color del fondo de la ventana (en RGB)
color_red = np.array((255, 0, 0))
color_green = np.array((0, 217, 94))
color_orange = np.array((252, 186, 3))
color_purple = np.array(( 140, 3, 222))
color_snake = np.array((161, 245, 170))
color_snake_complement = np.array((165, 39, 19))
color_black = np.array((0, 0, 0))

colors = [
    (230, 154, 119),
    (108, 177, 230),
    (230, 203, 96),
    (230, 154, 119),
    (108, 177, 230),
    (230, 203, 96),
    (230, 154, 119),
    (108, 177, 230),
    (230, 203, 96),
    (230, 154, 119),
    (108, 177, 230),
    (230, 203, 96),
    (230, 154, 119),
    (108, 177, 230),
    (230, 203, 96),
    #(217, 184, 222),
    #(214, 201, 163),
    #(174, 152, 214),
    #(214, 102, 9),
    #(148, 159, 214),
    #(138, 134, 19),
    #(214, 48, 183),
    #(230, 154, 119),
    #(108, 177, 230),
    #(230, 203, 96),
    #(217, 184, 222)
]
#Título de la ventana
pygame.display.set_caption("QPath & Snakes v0.1")

#Variable Global que controla el estado del menú
menu_state = 0
num_movimientos = 0
jugador = 1
resultado_decimal = 0
jugador_position_1 = 0
jugador_position_2 = 0

#Circuito imagen
qc_circuit = StartCircuit()
qc_circuit = AssembleCircuit(qc_circuit, 'Rx')
DrawCircuit(qc_circuit, 1)
img_circuit = pygame.image.load("__stored_img__/circuit.png")

#Grafico
plot_qc(qc_circuit)

img_plot = pygame.image.load("__stored_img__/plot_qcc.png")

img_dado_res = pygame.image.load('assets/img/img_dados/6.png')

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
    #body_tablero.fill(color_snake_complement)
    foot_buttons.fill(color_orange)
    foot_circuit.fill(color_orange)
    pygame.draw.rect(body_info, color_green, (0, 0, 22*bloque, 20*bloque), border_top_left_radius=10)
    #foot_buttons.fill(color_orange)
    footer.blit(img_circuit,(0,0))
    body_info.blit(img_plot,(11*bloque,0*bloque))
    
    #Se dibuja el tablero
    tablero_celdas = cuadricula(4*bloque, 0*bloque, 4*bloque, 4*bloque, (5,7), body_tablero, colors, True)
    red_celdas = cuadricula(0, 0, 4*bloque, 4*bloque, (4,1), body_tablero, color_red)
    green_celdas = cuadricula(32*bloque, 4*bloque, 4*bloque, 4*bloque, (4,1), body_tablero, color_green)
    start_celda = pygame.draw.rect(body_tablero, color_green, (32*bloque,0, 4*bloque, 4*bloque), border_top_right_radius=10)
    finish_celda = pygame.draw.rect(body_tablero, color_red, (0,16*bloque, 4*bloque, 4*bloque))
    
    #= pygame.draw.rect(body_tablero, color_red, (32*bloque, 0, 4*bloque, 4*bloque),border_top_right_radius=10)
    #green_celdas[0][0].update(20*bloque,0,4*bloque,4*bloque)
    #pygame.Rect.update(green_celdas[0][0], width=20)
    print(tablero_celdas[4][0].y / bloque)
    if menu_state == 0:
        button(foot_buttons, 2*bloque, 2*bloque, 8*bloque, 4*bloque, color_snake_complement, "Iniciar", 43, color_white, action=jugar)
        button(foot_buttons, 12*bloque, 2*bloque, 8*bloque, 4*bloque, color_snake_complement, "Salir", 43, color_white, action=salir)
    elif menu_state == 1:
        if num_movimientos % 2 == 0:
            button(foot_buttons, 2*bloque, 2*bloque, 18*bloque, 4*bloque, color_purple, "Player_1: Superponer dado", 43, color_white, action=superponer_dado)
            #body_info.blit(img_dado_res,(0,0))
        else:
            button(foot_buttons, 2*bloque, 2*bloque, 18*bloque, 4*bloque, color_black, "Player_2: Superponer dado", 43, color_white, action=superponer_dado)
            #body_info.blit(img_dado_res,(0,0))
        body_info.blit(img_dado_res,(0,0))
        draw_pointer(1, 1*bloque, 16*bloque+1*bloque)
        draw_pointer(2, 3*bloque, 16*bloque+3*bloque)
        print(resultado_decimal)
    #clock.tick(30)
    #Hace que todo lo que se dibuje en la superficie en cada frame se vuelva visible
    pygame.display.flip()

