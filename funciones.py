import pygame
from variables import indice_fotograma, temporizador
from constantes import *
import json
import os

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

def reiniciar_datos_juego(datos_juego: dict)-> None:
    """Reinicia el diccionario del jugador para una nueva partida

    Returns:
        dict:
    """
    datos_juego['puntuacion'] = 0
    datos_juego['vidas'] = 3
    datos_juego['acumulador_correctas'] = 0
    datos_juego['nivel_juego'] = 1

def actualizar_fotograma(pantalla, fotogramas, velocidad_fondo):
    global indice_fotograma, temporizador
    temporizador += 1
    if temporizador >= velocidad_fondo:
        indice_fotograma += 1
        if indice_fotograma >= len(fotogramas):
            indice_fotograma = 0
        temporizador = 0
    pantalla.blit(fotogramas[indice_fotograma], (0, 0))
    
def crear_diccionario_boton(ruta_imagen)->dict:
    """ Crea un diccionario con la superficie y el rectangulo del boton

    Args:
        ruta_imagen (str): path de la imagen
    """
    boton = {
    'superficie': pygame.image.load(ruta_imagen),
    'rectangulo': pygame.Rect(150, 550, 163, 61)
    }
    return boton

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

def dibujar_corazones_vidas(cantidad_vidas: int,pantalla):
    posiciones_corazones = [(380, 633), (440, 633), (500, 633)]
    ruta_imagen_celeste = 'img/corazon_celeste.png'
    ruta_imagen_gris = 'img/corazon_gris.png'
    dimensiones_corazon = (50,50)
    for i in range(3):
        if i < cantidad_vidas:
            cargar_y_mostrar_imagen(pantalla,ruta_imagen_celeste,dimensiones_corazon,posiciones_corazones[i])
        else:     
            cargar_y_mostrar_imagen(pantalla,ruta_imagen_gris,dimensiones_corazon,posiciones_corazones[i])

def marcar_respuesta_correcta(datos_juego: dict):
    CLICK_CORRECTO.play()
    datos_juego['puntuacion'] += 10
    datos_juego['acumulador_correctas'] += 1
    if datos_juego['acumulador_correctas'] >= 10:
        datos_juego['vidas'] += 1
        
def marcar_respuesta_incorrecta(datos_juego: dict):
    CLICK_INCORRECTO.play()
    datos_juego['puntuacion'] -= 5
    datos_juego['acumulador_correctas'] = 0
    datos_juego['vidas'] -= 1
        
archivo_json = "puntuaciones.json"

# Función para guardar datos en JSON
def guardar_datos_en_json(nombre, puntuacion):
    datos = {"nombre": nombre, "puntuacion": puntuacion}
    try:
        with open("puntajes.json", "r") as archivo:
            puntajes = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        puntajes = []

    puntajes.append(datos)
    with open("puntajes.json", "w") as archivo:
        json.dump(puntajes, archivo, indent=4)
        

    

    