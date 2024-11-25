import pygame
from variables import indice_fotograma, temporizador
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


def cargar_botones_y_posicionar(imagenes:list,posiciones:list):
    if len(imagenes) != len(posiciones):
        retorno = 'ERROR! la cantidad de imagenes no coinciden con la cantidad de posiciones'
    else:
        cartas = []
        for i in range(len(imagenes)):
            carta = {}
            carta['superficie'] = pygame.image.load(imagenes[i])
            carta['rectangulo'] = carta['superficie'].get_rect(topleft=posiciones[i])
            cartas.append(carta)
        retorno = cartas
    return retorno

def dibujar_corazones_vidas(cantidad_vidas,pantalla):
    posiciones_corazones = [(380, 633), (440, 633), (500, 633)]
    ruta_imagen_celeste = 'img/corazon_celeste.png'
    ruta_imagen_gris = 'img/corazon_gris.png'
    dimensiones_corazon = (50,50)
    for i in range(3):
        if i < cantidad_vidas:
            cargar_y_mostrar_imagen(pantalla,ruta_imagen_celeste,dimensiones_corazon,posiciones_corazones[i])
        else:     
            cargar_y_mostrar_imagen(pantalla,ruta_imagen_gris,dimensiones_corazon,posiciones_corazones[i])

def verificar_respuesta(datos_juego:dict,pregunta_actual:dict,respuesta:int)->bool:
    if pregunta_actual['respuesta correcta'] == respuesta:
        datos_juego['puntuacion'] += PUNTUACION_ACIERTO
        retorno = True
    else:
        datos_juego['puntuacion'] -= PUNTUACION_ERROR
        datos_juego['vidas'] -= 1
        retorno = False
    retorno