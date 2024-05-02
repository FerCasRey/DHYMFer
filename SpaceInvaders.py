import pygame
import sys
import random

# Configuración inicial
pygame.init()
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('C:/Users/Admin/Downloads/Galaxian.png')  # Carga la imagen
        self.image = pygame.transform.scale(self.image, (50, 50))  # Ajusta el tamaño de la imagen
        self.rect = self.image.get_rect(center=(ancho / 2, alto - 50))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > ancho:
            self.rect.right = ancho

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, imagenes_enemigos):
        super().__init__()
        imagenes_enemigos = ['C:/Users/Admin/Downloads/Enemy.png', 'C:/Users/Admin/Downloads/Enemy2.png', 'C:/Users/Admin/Downloads/Ufo.png', 'C:/Users/Admin/Downloads/Enemy.png']
        imagenes_enemigos = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.move_ip(0, 1)
        if self.rect.top > alto:
            self.rect.bottom = 0

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.move_ip(0, -5)
        if self.rect.bottom < 0:
            self.kill()

jugador = Jugador()
enemigos = pygame.sprite.Group()
proyectiles = pygame.sprite.Group()
todos = pygame.sprite.Group(jugador)
imagenes_enemigos = ['C:/Users/Admin/Downloads/Enemy.png', 'C:/Users/Admin/Downloads/Enemy2.png', 'C:/Users/Admin/Downloads/Ufo.png', 'C:/Users/Admin/Downloads/Enemy.png']



# Crear enemigos
for fila in range(4):
    for columna in range(10):
        x = 50 + columna * 70
        y = 50 + fila * 70
        imagen = imagenes_enemigos[fila]  # Selecciona la imagen correspondiente a la fila
        enemigo = Enemigo(x, y, imagen)
        enemigos.add(enemigo)
        todos.add(enemigo)



# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            proyectil = Proyectil(*jugador.rect.center)
            proyectiles.add(proyectil)
            todos.add(proyectil)

    # Los enemigos de la última fila disparan aleatoriamente
    enemigos_candidatos = [e for e in enemigos if e.rect.y > alto - 100]
    if enemigos_candidatos:  # La lista no está vacía
        disparador = random.choice(enemigos_candidatos)
        if disparador:
            proyectil = Proyectil(*disparador.rect.center)
            proyectiles.add(proyectil)
            todos.add(proyectil)

    todos.update()

    for proyectil in proyectiles:
        enemigos_alcanzados = pygame.sprite.spritecollide(proyectil, enemigos, True)
        for enemigo in enemigos_alcanzados:
            proyectil.kill()
            todos.remove(enemigo)

    pantalla.fill((0, 0, 0))
    todos.draw(pantalla)

    pygame.display.flip()
    pygame.time.delay(10)

