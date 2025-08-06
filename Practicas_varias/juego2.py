import pygame
import random
import sys

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Space Invaders Mejorado")

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (50, 130, 140)
GRIS = (100, 100, 100)

fuente_grande = pygame.font.SysFont(None, 64)
fuente_media = pygame.font.SysFont(None, 36)

class Jugador:
    def __init__(self):
        self.img = pygame.Surface((50, 30))
        self.img.fill(VERDE)
        self.rect = self.img.get_rect(midbottom=(ANCHO // 2, ALTO - 50))
        self.vel = 6
        self.vidas = 3

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.vel
        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x += self.vel

    def dibujar(self, pantalla):
        pantalla.blit(self.img, self.rect)

class Bala:
    def __init__(self):
        self.img = pygame.Surface((5, 15))
        self.img.fill(ROJO)
        self.rect = self.img.get_rect()
        self.vel = 10
        self.activa = False

    def disparar(self, x, y):
        if not self.activa:
            self.rect.midbottom = (x, y)
            self.activa = True
            # disparo_sonido.play()  # <-- comentado

    def mover(self):
        if self.activa:
            self.rect.y -= self.vel
            if self.rect.bottom < 0:
                self.activa = False

    def dibujar(self, pantalla):
        if self.activa:
            pantalla.blit(self.img, self.rect)

class Enemigo:
    def __init__(self, x, y):
        self.img = pygame.Surface((40, 30))
        self.img.fill(AZUL)
        self.rect = self.img.get_rect(topleft=(x, y))

    def dibujar(self, pantalla):
        pantalla.blit(self.img, self.rect)

def crear_enemigos(filas, columnas):
    enemigos = []
    for fila in range(filas):
        for col in range(columnas):
            x = 60 + col * 60
            y = 50 + fila * 50
            enemigos.append(Enemigo(x, y))
    return enemigos

def mostrar_texto_centrado(texto, fuente, color, pantalla, y):
    render = fuente.render(texto, True, color)
    rect = render.get_rect(center=(ANCHO // 2, y))
    pantalla.blit(render, rect)

def mostrar_vidas(vidas, pantalla):
    texto = fuente_media.render(f"Vidas: {vidas}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

def pantalla_inicio():
    pantalla.fill(NEGRO)
    mostrar_texto_centrado("SPACE INVADERS", fuente_grande, VERDE, pantalla, ALTO // 3)
    mostrar_texto_centrado("Presiona ENTER para jugar", fuente_media, BLANCO, pantalla, ALTO // 2)
    pygame.display.flip()

def pantalla_game_over(puntos):
    pantalla.fill(NEGRO)
    mostrar_texto_centrado("¡GAME OVER!", fuente_grande, ROJO, pantalla, ALTO // 3)
    mostrar_texto_centrado(f"Puntos: {puntos}", fuente_media, BLANCO, pantalla, ALTO // 2)
    mostrar_texto_centrado("Presiona R para reiniciar o ESC para salir", fuente_media, BLANCO, pantalla, ALTO // 1.5)
    pygame.display.flip()

def juego():
    jugador = Jugador()
    bala = Bala()
    enemigos = crear_enemigos(5, 10)
    vel_enemigo = 1
    direccion_enemigo = 1
    descenso_enemigo = 20
    puntos = 0
    reloj = pygame.time.Clock()
    juego_terminado = False

    while not juego_terminado:
        reloj.tick(60)
        pantalla.fill(NEGRO)
        teclas = pygame.key.get_pressed()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    bala.disparar(jugador.rect.centerx, jugador.rect.top)

        jugador.mover(teclas)
        bala.mover()

        borde_tocado = False
        for enemigo in enemigos:
            enemigo.rect.x += vel_enemigo * direccion_enemigo
            if enemigo.rect.right >= ANCHO or enemigo.rect.left <= 0:
                borde_tocado = True
        if borde_tocado:
            direccion_enemigo *= -1
            for enemigo in enemigos:
                enemigo.rect.y += descenso_enemigo

        if bala.activa:
            for enemigo in enemigos:
                if enemigo.rect.colliderect(bala.rect):
                    enemigos.remove(enemigo)
                    bala.activa = False
                    puntos += 10
                    # explosion_sonido.play()  # <-- comentado
                    break

        for enemigo in enemigos:
            if enemigo.rect.bottom >= jugador.rect.top:
                jugador.vidas = 0
                break

        jugador.dibujar(pantalla)
        bala.dibujar(pantalla)
        for enemigo in enemigos:
            enemigo.dibujar(pantalla)

        mostrar_vidas(jugador.vidas, pantalla)
        mostrar_texto_centrado(f"Puntos: {puntos}", fuente_media, BLANCO, pantalla, 30)

        if jugador.vidas <= 0 or len(enemigos) == 0:
            juego_terminado = True

        pygame.display.flip()

    return puntos

def main():
    jugando = False
    puntos = 0
    while True:
        if not jugando:
            pantalla_inicio()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        jugando = True
                        puntos = juego()
                    elif evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
        else:
            pantalla_game_over(puntos)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        jugando = True
                        puntos = juego()
                    elif evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    main()

