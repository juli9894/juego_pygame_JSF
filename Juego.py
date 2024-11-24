import pygame
from constantes import *
from preguntas import *
from funciones import *

pygame.init()

# FUENTES DEL JUEGO
fuente_pregunta = pygame.font.SysFont('impact', 30) 
fuente_respuesta = pygame.font.SysFont('arial', 25) 
fuente_portatil = pygame.font.Font('fuentes/Minecraft.ttf', 30)

# OPCIONES RESPUESTAS
imagenes_respuestas = [
    'img/OPCION_1.png',
    'img/OPCION_2.png',
    'img/OPCION_3.png',
    'img/OPCION_4.png'
]

posiciones_botones = [(650,290), (650,360), (650,430), (650,500)]
claves_botones = [OPCION_1, OPCION_2, OPCION_3, OPCION_4]

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event])->str:
    pygame.display.set_caption('JUEGO')
    retorno = 'jugar'

    # CREAR LA PREGUNTA
    carta_pregunta = {}
    carta_pregunta['superficie'] = pygame.Surface(TAMAÑO_PREGUNTA)
    carta_pregunta['rectangulo'] = carta_pregunta['superficie'].get_rect()

    # CARGAR IMAGENES DE LAS RESPUESTAS
    cartas_respuestas = []
    for nombre_imagen in imagenes_respuestas:
        carta_respuesta = {}
        carta_respuesta['superficie'] = pygame.image.load(nombre_imagen)
        carta_respuesta['rectangulo'] = carta_respuesta['superficie'].get_rect()
        cartas_respuestas.append(carta_respuesta)

    # PREGUNTA inicializar
    pregunta_actual = lista_preguntas[0]

    # GESTION DE EVENTOS
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = 'salir'
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]['rectangulo'].collidepoint(evento.pos):
                    print('SE DIO CLICK A UNA CARTA DE RESPUESTA')

            


    # CARGAR FONDO PANTALLA
    cargar_y_mostrar_imagen(pantalla, 'img/fondo_juego_1.png', VENTANA, (0, 0))

    # CONFIGURAR PREGUNTA
    carta_pregunta['superficie'] = pygame.Surface((650,200), pygame.SRCALPHA) 
    carta_pregunta['superficie'].fill(TRANSPARENTE)

    # AGREGAR TEXTO ALA PREGUNTA
    mostrar_texto(carta_pregunta['superficie'],pregunta_actual['pregunta'],(20,20),fuente_pregunta,COLOR_NEGRO)
    # AGREGAR TEXTO ALAS RESPUESTAS
    for i in range(len(claves_botones)):
        mostrar_texto(cartas_respuestas[i]['superficie'],pregunta_actual[f'respuesta_{i+1}'],(120,20),fuente_respuesta,COLOR_NEGRO)


    # DIBUJAR y UBICAR PREGUNTA
    pantalla.blit(carta_pregunta['superficie'], (500, 150))


    # UBICAR Y DIBUJAR LAS RESPUESTAS
    for i in range(len(cartas_respuestas)):
        cartas_respuestas[i]['rectangulo'] = pantalla.blit(cartas_respuestas[i]['superficie'], posiciones_botones[i])

    pygame.draw.rect(pantalla,COLOR_VERDE, cartas_respuestas[0]['rectangulo'])
    return retorno