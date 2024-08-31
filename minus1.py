# Este código crea una ventana por un segundo que muestra un corazon con un -1 y un sonido muy corto

#Importamos pygame y sys
import pygame, sys
#Iniciamos pygame
pygame.init()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('-1 life')
clock=pygame.time.Clock()
menosunpunto=pygame.image.load("C:/Users/Carolina/Desktop/sprites/heart.png")
pygame.mixer.music.load("C:/Users/Carolina/Desktop/sprites/messenger-tono-mensaje-.mp3")
pygame.mixer.music.play(1)

pygame.time.set_timer(pygame.QUIT, 1000)

#Esto crea una ventana que muestra el corazón y la llena de color blanco, también establece el parámetro para cerrar la ventana que es la x de la ventana
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    
    screen.fill((255,255,255))
    
    screen.blit(menosunpunto,(8,50))
    
    
    pygame.display.flip()
    clock.tick(60)
    