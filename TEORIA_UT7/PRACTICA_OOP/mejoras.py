import pygame
from random import randint
pygame.init()
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("GOKU NO PUEDE HACER LA GENKIDAMA")
ball = pygame.image.load("PRACTICA_OOP/player2.png")
ball = pygame.transform.scale(ball, (25,25))
ballrect = ball.get_rect()
# La velocidad se calcular con un valor pseudialeatorio entre 3,6
speed = [randint(9,18),randint(3,6)]
ballrect.move_ip(0,0)
bate = pygame.image.load("PRACTICA_OOP/goku.png")
bate = pygame.transform.scale(bate, (120,160))
baterect = bate.get_rect()
baterect.move_ip(25,350)
# Esta es la fuente que usaremos para el texto que aparecerá en pantalla (tamaño 36)
fuente = pygame.font.Font(None, 136)
# Bucle principal
jugando = True
while jugando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False     
    keys = pygame.key.get_pressed()
    # RESTRICCIÓN: para no salir por la izquierda
    if keys[pygame.K_LEFT] and baterect.left > 0:
        baterect = baterect.move(-10,0)
        
    # RESTRICCIÓN: para no salir por la derecha
    if keys[pygame.K_RIGHT] and baterect.right < ventana.get_width():
        baterect = baterect.move(10,0)
        
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
        ballrect.bottom = baterect.top
        
    ballrect = ballrect.move(speed)
    
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]

    if ballrect.top < 0: 
        speed[1] = -speed[1]
        
    # Si la pelota toca el border inferior, has perdido ("Game Over")
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (125,125,125))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    else:
        ventana.fill((120, 30, 0))
        ventana.blit(ball, ballrect)
        # Dibujo el bate
        ventana.blit(bate, baterect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()