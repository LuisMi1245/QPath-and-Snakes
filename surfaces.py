import pygame 

#Defino una unidad de medida fija de 21px
bloque = 21

#Dibujo toda la interfaz

size = (48*bloque, 31*bloque) #Width * Height
#Se genera un objeto superficie llamado screen donde se pondrán los elementos
screen = pygame.display.set_mode(size)
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#Se generan superficies hijas que se superponen con screen
head = pygame.Surface.subsurface(screen, (0,0, 48*bloque, 3*bloque))
body = pygame.Surface.subsurface(screen, (0,3*bloque, 48*bloque, 20*bloque))
footer = pygame.Surface.subsurface(screen, (0, 23*bloque, 48*bloque, 8*bloque))

#head
