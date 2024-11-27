import pygame
from constantes import *
from funciones import *

# fuente = pygame.font.Font('fuentes/Minecraft.ttf', 30)

# def game_over(pantalla, ruta_fondo, fuente, puntuacion)->str:
#     # fondo = pygame.image.load('img/fondo_puntuacion.png') 
#     # fondo = pygame.transform.scale(fondo, (VENTANA))  
#     guardar_nombre_y_puntaje(pantalla, ruta_fondo, fuente, puntuacion)
#     # os.system('PAUSE')
    
#     # guardar_nombre_y_puntaje(pantalla, fondo, fuente, puntuacion)
#     return 'rankings'
#     CLICK_GAME_OVER.play()
boton_salir = crear_diccionario_boton('img/boton_salir.png')
boton_salir_seleccionado = crear_diccionario_boton('img/boton_salir_seleccionado.png')

def mostrar_game_over(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event], datos_juego:dict)->str:
    pygame.display.set_caption('GAME_OVER')
    retorno = 'game_over'
    # GESTION DE EVENTOS
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = 'salir'
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_salir['rectangulo'].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                boton_salir['superficie'] = boton_salir_seleccionado['superficie']
                retorno = 'menu'
                #GUARDAR RANKINGS
                reiniciar_datos_juego(datos_juego)
                print("Sali del game over")

    # CARGAR FONDO PANTALLA
    cargar_y_mostrar_imagen(pantalla,'img/fondo_puntuacion.png',VENTANA,(0,0))
    # CARGAR BOTON VOLVER
    cargar_y_mostrar_imagen(pantalla, 'img/boton_salir.png', (163,61), (150, 550))
    # CARGAR PORTATIL
    cargar_y_mostrar_imagen(pantalla, 'img/portatil.png', VENTANA, (0, 0))
    
    # ACTUALIZAR BOTON VOLVER SELECCIONADO
    boton_salir['rectangulo'] = pantalla.blit(boton_salir['superficie'], boton_salir['rectangulo'].topleft)
    # REINICIAR BOTON VOLVER SELECCIONADO
    boton_salir['superficie'] = pygame.image.load('img/boton_salir.png')
    boton_salir['rectangulo'] = pygame.Rect(150, 550, 163, 61)

    return retorno