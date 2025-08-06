import pygame
import random
import time

pygame.init()

# Constantes
ANCHO, ALTO = 600, 650
TAM_CASILLA = 100
PADDING = 20
MARGEN_TOP = 80
FILAS, COLUMNAS = 4, 4
FPS = 60
TIEMPO_INICIAL = 60
BONUS_TIEMPO = 5

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (200, 0, 0)
ROSA_VISIBLE = (255, 182, 193)     # Rosa pastel más visible
MENTA_PASTEL = (170, 255, 204)     # Color suave para fichas descubiertas
AZUL_AMIGABLE = (50, 130, 140)
GRIS_CLARO = (230, 230, 230)

# Crear pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Memoria")

# Reloj
reloj = pygame.time.Clock()

# Fuentes
fuente = pygame.font.SysFont(None, 44)
fuente_grande = pygame.font.SysFont(None, 52)

# Crear pares de números
numeros = list(range(1, 9)) * 2
random.shuffle(numeros)

# Crear tablero
tablero = []
for fila in range(FILAS):
    fila_tablero = []
    for columna in range(COLUMNAS):
        indice = fila * COLUMNAS + columna
        x = columna * (TAM_CASILLA + PADDING) + PADDING
        y = fila * (TAM_CASILLA + PADDING) + MARGEN_TOP
        casilla = {
            "valor": numeros[indice],
            "descubierto": False,
            "rect": pygame.Rect(x, y, TAM_CASILLA, TAM_CASILLA)
        }
        fila_tablero.append(casilla)
    tablero.append(fila_tablero)

# Variables
seleccionados = []
bloquear_input = False
tiempo_espera = 0
juego_terminado = False
fuegos = []
ganador = None

# Cronómetro
tiempo_restante = TIEMPO_INICIAL
inicio_tiempo = time.time()

# Fuegos artificiales
class Fuego:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radio = 1
        self.color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)])
        self.velocidad = random.uniform(1, 4)
        self.max_radio = random.randint(20, 40)

    def actualizar(self):
        self.radio += self.velocidad

    def dibujar(self, pantalla):
        if self.radio < self.max_radio:
            pygame.draw.circle(pantalla, self.color, (int(self.x), int(self.y)), int(self.radio), 2)
            return True
        return False

def dibujar_tablero():
    pantalla.fill(BLANCO)
    for fila in tablero:
        for casilla in fila:
            rect = casilla["rect"]
            if casilla["descubierto"]:
                pygame.draw.rect(pantalla, MENTA_PASTEL, rect, border_radius=8)
                texto = fuente.render(str(casilla["valor"]), True, NEGRO)
                pantalla.blit(texto, texto.get_rect(center=rect.center))
            else:
                pygame.draw.rect(pantalla, ROSA_VISIBLE, rect, border_radius=8)

def juego_completado():
    for fila in tablero:
        for casilla in fila:
            if not casilla["descubierto"]:
                return False
    return True

def mostrar_cronometro():
    texto = fuente.render(f"Tiempo: {int(tiempo_restante)}", True, ROJO)
    pantalla.blit(texto, (ANCHO//2 - 80, 20))

def mostrar_mensaje_cuadro(texto_final):
    # Cuadro más grande y centrado
    ancho_cuadro = 500
    alto_cuadro = 140
    cuadro_rect = pygame.Rect(
        (ANCHO - ancho_cuadro) // 2,
        (ALTO - alto_cuadro) // 2,
        ancho_cuadro,
        alto_cuadro
    )
    pygame.draw.rect(pantalla, GRIS_CLARO, cuadro_rect, border_radius=20)
    pygame.draw.rect(pantalla, AZUL_AMIGABLE, cuadro_rect, 4, border_radius=20)

    texto = fuente_grande.render(texto_final, True, AZUL_AMIGABLE)
    pantalla.blit(texto, texto.get_rect(center=cuadro_rect.center))

# Bucle principal
corriendo = True
while corriendo:
    reloj.tick(FPS)

    if not juego_terminado:
        tiempo_transcurrido = time.time() - inicio_tiempo
        tiempo_restante = TIEMPO_INICIAL - tiempo_transcurrido

        if tiempo_restante <= 0:
            juego_terminado = True
            ganador = False

    if bloquear_input and time.time() > tiempo_espera:
        if seleccionados[0]["valor"] != seleccionados[1]["valor"]:
            seleccionados[0]["descubierto"] = False
            seleccionados[1]["descubierto"] = False
        else:
            TIEMPO_INICIAL += BONUS_TIEMPO
        seleccionados.clear()
        bloquear_input = False

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        elif evento.type == pygame.MOUSEBUTTONDOWN and not bloquear_input and not juego_terminado:
            pos = pygame.mouse.get_pos()
            for fila in tablero:
                for casilla in fila:
                    if casilla["rect"].collidepoint(pos) and not casilla["descubierto"]:
                        casilla["descubierto"] = True
                        seleccionados.append(casilla)
                        if len(seleccionados) == 2:
                            bloquear_input = True
                            tiempo_espera = time.time() + 0.8

    if not juego_terminado and juego_completado():
        juego_terminado = True
        ganador = True
        fuegos = [Fuego(random.randint(50, ANCHO-50), random.randint(MARGEN_TOP + 50, ALTO-50)) for _ in range(15)]

    dibujar_tablero()
    mostrar_cronometro()

    if juego_terminado:
        if ganador:
            mostrar_mensaje_cuadro("¡Felicidades, ganaste!")
            nuevos_fuegos = []
            for fuego in fuegos:
                if fuego.dibujar(pantalla):
                    fuego.actualizar()
                    nuevos_fuegos.append(fuego)
            if len(nuevos_fuegos) < 15:
                nuevos_fuegos.append(Fuego(random.randint(50, ANCHO-50), random.randint(MARGEN_TOP + 50, ALTO-50)))
            fuegos = nuevos_fuegos
        else:
            mostrar_mensaje_cuadro("¡Se terminó el tiempo!")

    pygame.display.flip()

pygame.quit()
