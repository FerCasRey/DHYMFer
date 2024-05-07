import pygame
import sys
import random

# Configuración inicial
pygame.init()
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
fuente = pygame.font.Font(None, 36)  # Fuente para mostrar el texto

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('C:/Users/Admin/Downloads/Img/Galaxian64.png')  # Carga la imagen
        self.image = pygame.transform.scale(self.image, (50, 50))  # Ajusta el tamaño de la imagen
        self.rect = self.image.get_rect(center=(ancho / 2, alto - 50))
        self.vidas = 3



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
    def __init__(self, x, y, ruta_imagen):
        super().__init__()
        self.image = pygame.image.load(ruta_imagen)  # Carga la imagen
        self.image = pygame.transform.scale(self.image, (50, 50))  # Ajusta el tamaño de la imagen
        self.rect = self.image.get_rect(center=(x, y))
        self.direccion = 1
        self.tiempo_ultimo_cambio = pygame.time.get_ticks()

    def update(self):
        self.rect.move_ip(self.direccion, 0)
        if self.rect.left < 0 or self.rect.right > ancho:
            self.direccion *= -1  # Cambia de dirección
            if pygame.time.get_ticks() - self.tiempo_ultimo_cambio > 10000:  # Han pasado 10 segundos
                self.rect.move_ip(0, self.image.get_height())  # Baja una fila
                self.tiempo_ultimo_cambio = pygame.time.get_ticks()

class Proyectil_1(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(x, y-50))
        self.velocidad = velocidad

    def update(self):
        self.rect.move_ip(0, self.velocidad)
        if self.rect.bottom < 0 or self.rect.top > alto:
            self.kill()
class Proyectil_2(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y-50))
        self.velocidad = velocidad

    def update(self):
        self.rect.move_ip(0, self.velocidad)
        if self.rect.bottom < 0 or self.rect.top > alto:
            self.kill()

jugador = Jugador()
enemigos = pygame.sprite.Group()
proyectiles_1 = pygame.sprite.Group()
proyectiles_2 = pygame.sprite.Group()
todos = pygame.sprite.Group(jugador)
imagenes_enemigos = ['C:/Users/Admin/Downloads/Img/Enemy(Porpol).png', 'C:/Users/Admin/Downloads/Img/Enemy2.png', 'C:/Users/Admin/Downloads/Img/Ufo.png', 'C:/Users/Admin/Downloads/Img/Enemy(Porpol).png']

# Crear enemigos
for fila in range(4):
    for columna in range(10):
        x = 50 + columna * 70
        y = 50 + fila * 70
        if fila < 2:  # Las primeras dos filas tienen el mismo tipo de enemigos
            imagen = imagenes_enemigos[0]
        else:  # Las últimas dos filas tienen otro tipo de enemigos
            imagen = imagenes_enemigos[1]
        enemigo = Enemigo(x, y, imagen)
        enemigos.add(enemigo)
        todos.add(enemigo)

# Bucle principal del juego
corriendo = True
tiempo_ultimo_disparo = pygame.time.get_ticks()
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            proyectil = Proyectil_1(*jugador.rect.center, -5)
            proyectiles_1.add(proyectil)
            todos.add(proyectil)

    # Los enemigos disparan aleatoriamente
    if pygame.time.get_ticks() - tiempo_ultimo_disparo > 2000:  # Han pasado 2 segundos desde el último disparo
        disparador = random.choice(enemigos.sprites())
        if disparador:
            proyectil = Proyectil_2(*disparador.rect.center, 5)
            proyectiles_2.add(proyectil)
            todos.add(proyectil)
            tiempo_ultimo_disparo = pygame.time.get_ticks()

    todos.update()
    
    for proyectil in proyectiles_1:
        
        enemigos_alcanzados = pygame.sprite.spritecollide(proyectil, enemigos, True)
        for enemigo in enemigos_alcanzados:
            proyectil.kill()
            todos.remove(enemigo)

    # Comprobar si algún proyectil ha alcanzado al jugador
    if pygame.sprite.spritecollide(jugador, proyectiles_2, True):
        jugador.vidas -= 1  # El jugador pierde una vida
        if jugador.vidas == 0:  # Si el jugador no tiene vidas, termina el juego
            texto = fuente.render("Has perdido", True, (255, 255, 255))
            pantalla.blit(texto, (ancho / 2 - texto.get_width() / 2, alto / 2 - texto.get_height() / 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

    # Comprobar si algún enemigo ha alcanzado al jugador
    if pygame.sprite.spritecollide(jugador, enemigos, False):
        jugador.vidas -= 1  # El jugador pierde una vida
        if jugador.vidas == 0:  # Si el jugador no tiene vidas, termina el juego
            texto = fuente.render("Has perdido", True, (255, 255, 255))
            pantalla.blit(texto, (ancho / 2 - texto.get_width() / 2, alto / 2 - texto.get_height() / 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

    pantalla.fill((0, 0, 0))
    todos.draw(pantalla)

    # Dibujar el contador de vidas
    texto_vidas = fuente.render(f"Vidas: {jugador.vidas}", True, (255, 255, 255))
    pantalla.blit(texto_vidas, (ancho - texto_vidas.get_width() - 10, 10))

    pygame.display.flip()
    pygame.time.delay(10)


