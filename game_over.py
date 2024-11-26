import pygame
from constantes import *
from funciones import *
import os

# fuente = pygame.font.Font('fuentes/Minecraft.ttf', 30)

def game_over(pantalla, ruta_fondo, fuente, puntuacion)->str:
    # fondo = pygame.image.load('img/fondo_puntuacion.png') 
    # fondo = pygame.transform.scale(fondo, (VENTANA))  
    CLICK_GAME_OVER.play()
    guardar_nombre_y_puntaje(pantalla, ruta_fondo, fuente, puntuacion)
    # os.system('PAUSE')
    
    # guardar_nombre_y_puntaje(pantalla, fondo, fuente, puntuacion)
    return 'rankings'