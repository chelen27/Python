import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configurar pantalla
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Dados")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (200, 0, 0)

# Fuente
fuente = pygame.font.SysFont("arial", 32)

# Cargar imágenes de los dados
imagenes_dados = [pygame.image.load(f'dado{i}.png') for i in range(1, 7)]

# Posiciones de los dados
pos_dado1 = (150, 150)
pos_dado2 = (330, 150)

# Función para lanzar los dados
def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

# Estado inicial
dado1 = 1
dado2 = 1

# Bucle principal
while True:
    pantalla.fill(BLANCO)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton.collidepoint(evento.pos):
                dado1, dado2 = lanzar_dados()

    # Mostrar dados
    pantalla.blit(imagenes_dados[dado1 - 1], pos_dado1)
    pantalla.blit(imagenes_dados[dado2 - 1], pos_dado2)

    # Botón
    boton = pygame.Rect(230, 320, 140, 50)
    pygame.draw.rect(pantalla, ROJO, boton)
    texto_boton = fuente.render("Lanzar", True, BLANCO)
    pantalla.blit(texto_boton, (boton.x + 25, boton.y + 10))

    # Mostrar suma
    suma_texto = fuente.render(f"Suma: {dado1 + dado2}", True, NEGRO)
    pantalla.blit(suma_texto, (230, 50))

    pygame.display.update()
