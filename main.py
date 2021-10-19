import sys, pygame
from surfaces import *

#Inicializa los módulos de pygame
pygame.init()

color_white = 255, 255, 255 #Color del fondo de la ventana en RGB
color_red = 255, 0, 0 
color_green = 0, 217, 94
color_orange = 252, 186, 3
color_purple =  140, 3, 252

#Título de la ventana
pygame.display.set_caption("QPath & Snakes")

posx = 2*bloque
posy = 19*bloque

#Ciclo que mantiene la ejecución del juego
while True:

    #Ciclo (seguramente asíncrono) que verifica el evento de presionar el botón de cerrar ventana y dispara una orden
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() #Le ordena al sistema a cerrar la ventana
    

    #Borra la pantalla y la pinta de blanco en cada frame
    
    screen.fill(color_white)
   
    head.blit(text, (15*bloque,0.6*bloque))
    body_tablero.fill(color_red)
    body_info.fill(color_purple)
    foot_circuit.fill(color_orange)
    foot_buttons.fill(color_green)

    #pygame.draw.circle(surface, color, centro, radio, ancho_borde)
    pygame.draw.circle(screen, color_red, (posx+ 0.5*bloque, posy+ 0.5*bloque), bloque*0.5),
    pygame.draw.circle(screen, color_white, (posx + 2.5*bloque, posy + 2.5*bloque), bloque*0.5)

    #Se dibuja un objeto (object) en la superficie con un collider (rect_object)
    #screen.blit(object, rect_object)

    #Hace que todo lo que se dibuje en la superficie en cada frame se vuelva visible
    pygame.display.flip()

