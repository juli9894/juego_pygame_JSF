import pygame
from constantes import *
from preguntas import *
from funciones import *
from game_over import *

pygame.init()

# FUENTES DEL JUEGO
fuente_pregunta = pygame.font.SysFont('impact', 30) 
fuente_respuesta = pygame.font.SysFont('arial', 25) 
fuente_portatil = pygame.font.Font('fuentes/Minecraft.ttf', 30)

indice = 1

# OPCIONES RESPUESTAS
imagenes_respuestas = [
    'img/OPCION_1.png',
    'img/OPCION_2.png',
    'img/OPCION_3.png',
    'img/OPCION_4.png'
]

imagenes_respuestas_seleccionadas = [
    'img/OPCION_1_seleccionada.png',
    'img/OPCION_2_seleccionada.png',
    'img/OPCION_3_seleccionada.png',
    'img/OPCION_4_seleccionada.png'
]

lista_preguntas = cargar_preguntas_csv('preguntas.csv')

posiciones_botones = [(650,290), (650,360), (650,430), (650,500)]

# CARGAR IMAGENES DE LAS RESPUESTAS Y POSICIONAR
cartas_respuestas = cargar_botones_y_posicionar(imagenes_respuestas,posiciones_botones)
claves_botones = [OPCION_1, OPCION_2, OPCION_3, OPCION_4]

bandera_respuesta = False

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event], datos_juego:dict)->str:
    global indice
    global lista_preguntas
    global bandera_respuesta
    global cartas_respuestas
    
    
    pygame.display.set_caption('JUEGO')
    if bandera_respuesta == True:
        cartas_respuestas = cargar_botones_y_posicionar(imagenes_respuestas,posiciones_botones)
        bandera_respuesta = False
    retorno = 'jugar'

    # CREAR LA PREGUNTA
    carta_pregunta = {}
    carta_pregunta['superficie'] = pygame.Surface(TAMAÑO_PREGUNTA)
    carta_pregunta['rectangulo'] = carta_pregunta['superficie'].get_rect()


    # PREGUNTA inicializar
    pregunta_actual = lista_preguntas[indice]

    # GESTION DE EVENTOS
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = 'salir'
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]['rectangulo'].collidepoint(evento.pos):
                    CLICK_PELOTAZO.play()
                    cartas_respuestas[i]['superficie'] = pygame.image.load(imagenes_respuestas_seleccionadas[i])
                    if i + 1 == pregunta_actual['respuesta_correcta']:
                        marcar_respuesta_correcta(datos_juego)
                        datos_juego['nivel_actual'] = 2
                    else:
                        marcar_respuesta_incorrecta(datos_juego)
                    indice += 1
                    bandera_respuesta = True
                    if indice == len(lista_preguntas):
                        indice = 0
    
    if datos_juego['nivel_actual'] == 1:
        cargar_y_mostrar_imagen(pantalla, 'img/fondo_juego_1.png', VENTANA, (0, 0))
    elif datos_juego['nivel_actual'] == 2:
        cargar_y_mostrar_imagen(pantalla, 'img/fondo_juego_2.png', VENTANA, (0, 0))

    # CONFIGURAR PREGUNTA
    carta_pregunta['superficie'] = pygame.Surface((615,200), pygame.SRCALPHA) 
    carta_pregunta['superficie'].fill(TRANSPARENTE)

    # AGREGAR TEXTO ALA PREGUNTA
    mostrar_texto(carta_pregunta['superficie'],pregunta_actual['pregunta'],(20,20),fuente_pregunta,COLOR_NEGRO)
    # AGREGAR TEXTO ALAS RESPUESTAS
    mostrar_texto(cartas_respuestas[0]['superficie'],pregunta_actual['respuesta_1'],(120,20),fuente_respuesta,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[1]['superficie'],pregunta_actual['respuesta_2'],(120,20),fuente_respuesta,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[2]['superficie'],pregunta_actual['respuesta_3'],(120,20),fuente_respuesta,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[3]['superficie'],pregunta_actual['respuesta_4'],(120,20),fuente_respuesta,COLOR_NEGRO)
    
    
    # DIBUJAR y UBICAR PREGUNTA
    pantalla.blit(carta_pregunta['superficie'], (500, 150))

    # CARGAR PORTATIL
    cargar_y_mostrar_imagen(pantalla, 'img/portatil.png', VENTANA, (0, 0))
    # VIDAS
    dibujar_corazones_vidas(datos_juego['vidas'],pantalla)
    # PUNTUACION
    mostrar_texto(pantalla,f'{datos_juego["puntuacion"]}',(830,643),fuente_portatil,COLOR_BLANCO)

    # DIBUJAR LAS RESPUESTAS
    for i in range(len(cartas_respuestas)):
        pantalla.blit(cartas_respuestas[i]['superficie'],cartas_respuestas[i]['rectangulo'])
    
    if datos_juego['vidas'] <= 0:
        retorno = 'game_over'
        CLICK_GAME_OVER.play()
        indice = 0
        
    return retorno

    