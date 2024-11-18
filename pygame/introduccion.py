import pygame
from constantes import *

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    '''
    SALTO DE LINEA TEXTO
    '''
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

pygame.init()

# PANTALLA
pantalla = pygame.display.set_mode(VENTANA)
pygame.display.set_caption('PREGUNTADOS JSF') # TITULO DE LA VENTANA
corriendo = True

# PORTATIL PANTALLA FONDO PNG
portatil_pantalla = pygame.image.load('cuadro_principal.png') # cargo
portatil_pantalla = pygame.transform.scale(portatil_pantalla,((1200,800))) # escalo 

# ENCUADRE TEXTO TRANSPARENTE
encuadre_texto = pygame.Surface((350,150), pygame.SRCALPHA) 
encuadre_texto.fill(TRANSPARENTE)

# TEXTO
mensaje = 'En que ciudad Argentina nació el futbolista Lionel Andrés Messi?' 
fuente = pygame.font.SysFont('Arial Narrow', 25)
texto = fuente.render(mensaje,True, COLOR_FONDO)

# FONDO PORTATIL 1
fondo_portatil_1 = pygame.image.load('fondo_portatil_1.png')
fondo_portatil_1 = pygame.transform.scale(fondo_portatil_1,((1200,800)))

# PROTAGONISTA 1
protagonista_1 = pygame.image.load('protagonista_1.png')
protagonista_1 = pygame.transform.scale(protagonista_1, ((1200, 800)))


while corriendo:
    # EVENTOS
    # se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False

    # PANTALLA FONDO
    pantalla.fill(COLOR_PRINCIPAL) #color de pantalla

    # BLITEAR FONDO PORTATIL 1
    pantalla.blit(fondo_portatil_1,(-10,0))

    # BLITEAR PROTAGONITA 1
    pantalla.blit(protagonista_1,(-10,0))

    # BLITEAR LA CARTA EN LA PANTALLA (VA ADELANTE DE PANTALLA PARA QUE NO SE SUPERPONGA)
    pantalla.blit(portatil_pantalla,(-10,0))

    # BLITEAR ENCUADRE TEXTO
    pantalla.blit(encuadre_texto,(180,220))

    # BLITEAR TEXTO
    mostrar_texto(encuadre_texto,mensaje,(40,10),fuente,COLOR_FONDO)


    pygame.display.flip()

pygame.quit()

