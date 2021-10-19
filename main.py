import sys, pygame
pygame.init()

size = 1360, 768 #Es una tupla de Width * Height (Tamaño de la ventana)
color_white = 255, 255, 255 #Color del fondo de la ventana

#Se genera un objeto superficie llamado screen donde se pondrán los elementos
screen = pygame.display.set_mode(size)

#Se definen las imágenes que representan cada jugador y se define la rejilla rectangular que delimitada el objeto
player = [pygame.image.load("assets/img/einstein.jpg"), pygame.image.load("assets/img/newton.jpg")]
rect = [player[0].get_rect(), player[1].get_rect()] 

#Ciclo que mantiene la ejecución del juego
while True:
    
    #Ciclo que verifica el evento de presionar el botón de cerrar ventana y dispara una orden
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() #Le ordena al sistema a cerrar la ventana
    
    rect[0] = rect[0].move(1,0)
    screen.fill(color_white)
    screen.blit(player[0], rect[0])
    pygame.display.flip()