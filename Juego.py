import pygame
from constantes import *
from preguntas import *
from funciones import *

pygame.init()


def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event])->str:
    pygame.display.set_caption('JUEGO')
    retorno = 'jugar'

    # GESTION DE EVENTOS
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = 'salir'

    # CARGAR FONDO PANTALLA
    cargar_y_mostrar_imagen(pantalla,'img/fondo_juego_1.png',VENTANA,(0,0))


    return retorno