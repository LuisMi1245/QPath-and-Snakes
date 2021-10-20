#Aquí van los componentes interactivos de la interfaz como botones, gráficas y demás
import pygame
import numpy as np

# surface = superficie donde se ubica y se mide el botón (objeto surface)
# x,y = posicón (flotante)
# b,h = base y altura (flotante)
# btn_color = color del botón  (tupla)
# msg = mensaje del botón (texto)
# msg_size = tamaño del texto del botón (entero)
# msg_color = color del texto del botón (tupla)
# action = acción que genera el botón al ser presionado

def button(surface, x, y, b, h, btn_color, msg, msg_size, msg_color=(0,0,0), font_path="assets/fonts/Woodstamp.otf", action=None):
    
    mouse_x, mouse_y = pygame.mouse.get_pos() #obtiene la posición del puntero en la ventana. Tupla (x,y)
    click = pygame.mouse.get_pressed() #captura el evento de presionar click
    abs_pos_surface_x, abs_pos_surface_y = pygame.Surface.get_abs_offset(surface) #Obtiene la posición absoluta de una "surface" con respecto a la surface de primer nivel 
    abs_pos_bttn_x, abs_pos_bttn_y = abs_pos_surface_x + x, abs_pos_surface_y + y #Obtiene la posición absoluta de un botón con respecto a la superficie de primer nivel

    if (abs_pos_bttn_x + b) > mouse_x > (abs_pos_bttn_x) and (abs_pos_bttn_y + h) > mouse_y > (abs_pos_bttn_y):
        #Si el puntero está sobre el botón, imprime forma del botón con hover
        pygame.draw.rect(surface, btn_color+np.array((30,30,30)), (x,y,b,h), border_radius=5)
        #Si presionó el click, ejecuta action()
        if click[0] == 1 and action is not None:
            action() 
    else:
        #Si el puntero está fuera del área del botón, imprime forma del botón sin hover
        pygame.draw.rect(surface, btn_color, (x,y,b,h), border_radius=5)
    
    #texto del botón
    surface_msg, rect_msg = text_objects(msg, msg_size, font_path, msg_color) #Llama a la función que genera texto.
    rect_msg.center = ((x + (b / 2)), (y + (h / 2))) #Actualiza la posición del centro de la rejilla del texto en el centro de la surface donde se encuentre.

    #Se superpone la superficie "suface_msg" con "surface" 
    surface.blit(surface_msg, rect_msg)



#text = texto a renderizar (string)
#font = objeto fuente de pygame (objeto)
#color = color del texto (tupla RGB)

def text_objects(text, size, font_path, color=(0,0,0)):
    #función que retorna una tupla del texto y del rectángulo en donde se encierra el texto
    font = pygame.font.Font(font_path, size)
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()
