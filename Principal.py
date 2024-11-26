import pygame
from constantes import *
from funciones import *
from preguntas import *
from Menu import mostrar_menu
from Juego import mostrar_juego
from Opciones import mostrar_opciones
from Rankings import mostrar_rankings

pygame.init()

#----------------------------------------------------
# Configuraciones basicas de mi juego
pygame.display.set_caption('PREGUNTA Y GOL!!')
icono = pygame.image.load('img/icono.png')
pygame.display.set_icon(icono)

# MUSICA DE FONDO
pygame.mixer.music.load('sonidos/musica.mp3')
pygame.mixer.music.set_volume(0.1) 
pygame.mixer.music.play(-1)

# Configurar la pantalla
# pantalla = pygame.display.set_mode((VENTANA))
corriendo = True
reloj = pygame.time.Clock()



ventana_actual = 'menu'
#----------------------------------------------------
# CARGAR FONDO ANIMADO
fotogramas = []
fotogramas = cargar_fondo_animado('fondo_animado', 20)



while corriendo:
    # CARGAR FONDO ANIMADO
    actualizar_fotograma(pantalla,fotogramas,VELOCIDAD_FONDO)

    cola_eventos = pygame.event.get()
    reloj.tick(FPS)


    if ventana_actual == 'menu':
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == 'jugar':
        ventana_actual = mostrar_juego(pantalla,cola_eventos)
    elif ventana_actual == 'opciones':
        ventana_actual = mostrar_opciones(pantalla,cola_eventos)
    elif ventana_actual == 'rankings':
        ventana_actual = mostrar_rankings(pantalla,cola_eventos)
    elif ventana_actual == 'salir':
        print('SALIENDO')
        corriendo = False

    pygame.display.flip()

pygame.quit()