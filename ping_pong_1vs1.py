import os
import pygame
import random
import time

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana del juego
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Variables de la pelota
BALL_RADIUS = 10
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [random.choice([-5, 5]), random.choice([-5, 5])]
ball_moving = False

# Variables de las paletas
PAD_WIDTH = 10
PAD_HEIGHT = 80
LEFT_PAD_POS = [0, HEIGHT // 2 - PAD_HEIGHT // 2]
RIGHT_PAD_POS = [WIDTH - PAD_WIDTH, HEIGHT // 2 - PAD_HEIGHT // 2]
PAD_SPEED = 5

# Marcador
score_left = 0
score_right = 0
font = pygame.font.Font(None, 36)

# Función para dibujar la pelota
def draw_ball(ball_pos):
    pygame.draw.circle(WIN, WHITE, ball_pos, BALL_RADIUS)

# Función para dibujar las paletas
def draw_paddles(pad1_pos, pad2_pos):
    pygame.draw.rect(WIN, WHITE, pygame.Rect(pad1_pos[0], pad1_pos[1], PAD_WIDTH, PAD_HEIGHT))
    pygame.draw.rect(WIN, WHITE, pygame.Rect(pad2_pos[0], pad2_pos[1], PAD_WIDTH, PAD_HEIGHT))

# Función para dibujar el marcador
def draw_score():
    score_text = font.render(f"{player1_name}: {score_left} - {score_right} :{player2_name}", True, WHITE)
    score_rect = score_text.get_rect(center=(WIDTH // 2, 50))
    WIN.blit(score_text, score_rect)

# Función para mostrar mensaje de ganador
def display_winner(winner):
    winner_text = font.render(f"¡{winner} ha ganado!", True, WHITE)
    winner_rect = winner_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WIN.blit(winner_text, winner_rect)
    pygame.display.update()
    pygame.time.wait(3000)  # Esperar 3 segundos antes de salir del juego

# Función para obtener el nombre de los jugadores
def get_player_names():
    global player1_name, player2_name
    player1_name = get_input("Ingrese el nombre del jugador 1: ")
    player2_name = get_input("Ingrese el nombre del jugador 2: ")
    countdown()

# Función para obtener entrada del usuario dentro de la ventana del juego
def get_input(prompt):
    user_input = ""
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode
        draw_input_prompt(prompt + user_input)
        pygame.display.update()
    return user_input

# Función para dibujar el prompt de entrada de usuario
def draw_input_prompt(prompt):
    WIN.fill(BLACK)
    input_text = font.render(prompt, True, WHITE)
    input_rect = input_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WIN.blit(input_text, input_rect)

# Función para la cuenta regresiva antes de que comience el juego
def countdown():
    for i in range(5, 0, -1):
        WIN.fill(BLACK)
        countdown_text = font.render(f"{i}", True, WHITE)
        countdown_rect = countdown_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        WIN.blit(countdown_text, countdown_rect)
        pygame.display.update()
        pygame.time.wait(1000)

# Función principal del juego
def main():
    global ball_pos, ball_vel, ball_moving, score_left, score_right
    clock = pygame.time.Clock()

    # Obtener los nombres de los jugadores
    get_player_names()

    # Bucle del juego
    running = True
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if not ball_moving:
                        ball_moving = True
                        ball_vel = [random.choice([-5, 5]), random.choice([-5, 5])]
                    else:
                        ball_pos = [WIDTH // 2, HEIGHT // 2]
                        ball_moving = False

        # Movimiento de las paletas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and LEFT_PAD_POS[1] > 0:
            LEFT_PAD_POS[1] -= PAD_SPEED
        if keys[pygame.K_s] and LEFT_PAD_POS[1] < HEIGHT - PAD_HEIGHT:
            LEFT_PAD_POS[1] += PAD_SPEED
        if keys[pygame.K_UP] and RIGHT_PAD_POS[1] > 0:
            RIGHT_PAD_POS[1] -= PAD_SPEED
        if keys[pygame.K_DOWN] and RIGHT_PAD_POS[1] < HEIGHT - PAD_HEIGHT:
            RIGHT_PAD_POS[1] += PAD_SPEED

        # Actualizar la posición de la pelota si está en movimiento
        if ball_moving:
            ball_pos[0] += ball_vel[0]
            ball_pos[1] += ball_vel[1]

            # Rebotar en la parte superior e inferior de la pantalla
            if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
                ball_vel[1] = -ball_vel[1]

            # Rebotar en las paletas
            if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
                if ball_pos[1] >= LEFT_PAD_POS[1] and ball_pos[1] <= LEFT_PAD_POS[1] + PAD_HEIGHT:
                    ball_vel[0] = -ball_vel[0]
                else:
                    score_right += 1
                    if score_right == 10:
                        display_winner(player2_name)
                        running = False
                    ball_pos = [WIDTH // 2, HEIGHT // 2]
                    ball_moving = False
            elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
                if ball_pos[1] >= RIGHT_PAD_POS[1] and ball_pos[1] <= RIGHT_PAD_POS[1] + PAD_HEIGHT:
                    ball_vel[0] = -ball_vel[0]
                else:
                    score_left += 1
                    if score_left == 10:
                        display_winner(player1_name)
                        running = False
                    ball_pos = [WIDTH // 2, HEIGHT // 2]
                    ball_moving = False

        # Limpiar la pantalla
        WIN.fill(BLACK)

        # Dibujar elementos del juego
        draw_ball(ball_pos)
        draw_paddles(LEFT_PAD_POS, RIGHT_PAD_POS)
        draw_score()

        # Actualizar la pantalla
        pygame.display.update()

        # Establecer el número de fotogramas por segundo
        clock.tick(60)

    # Salir de Pygame
    pygame.quit()

# Llamar a la función principal del juego
if __name__ == "__main__":
    main()
