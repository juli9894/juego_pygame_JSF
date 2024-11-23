import pygame
from variables import indice_fotograma, temporizador

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


# def cargar_boton():
# def crear_lista_botones():

def cargar_fondo_animado(ruta_base,cantidad_fotogramas)->list:
    fotogramas = []
    for i in range(1,cantidad_fotogramas+1):
        ruta = f"{ruta_base}/{i}.png"
        fotogramas.append(pygame.image.load(ruta))
    return fotogramas


def actualizar_fotograma(pantalla, fotogramas, velocidad_fondo):
    global indice_fotograma, temporizador
    temporizador += 1
    if temporizador >= velocidad_fondo:
        indice_fotograma += 1
        if indice_fotograma >= len(fotogramas):
            indice_fotograma = 0
        temporizador = 0
    pantalla.blit(fotogramas[indice_fotograma], (0, 0))
    



def cargar_y_mostrar_imagen(pantalla, ruta_imagen:str, dimensiones:tuple, posicion):
    imagen = pygame.image.load(ruta_imagen)
    imagen = pygame.transform.scale(imagen, dimensiones)
    pantalla.blit(imagen, posicion)