import os
import pygame #type: ignore
import random

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
ball_served = False

# Variables de las paletas
PAD_WIDTH = 10
PAD_HEIGHT = 80
TEAM1_LEFT_PAD_POS = [0, HEIGHT // 4 - PAD_HEIGHT // 2]
TEAM1_RIGHT_PAD_POS = [0, 3 * HEIGHT // 4 - PAD_HEIGHT // 2]
TEAM2_LEFT_PAD_POS = [WIDTH - PAD_WIDTH, HEIGHT // 4 - PAD_HEIGHT // 2]
TEAM2_RIGHT_PAD_POS = [WIDTH - PAD_WIDTH, 3 * HEIGHT // 4 - PAD_HEIGHT // 2]
PAD_SPEED = 5

# Marcador
score_team1 = 0
score_team2 = 0
font = pygame.font.Font(None, 36)

# Función para dibujar la pelota
def draw_ball(ball_pos):
    pygame.draw.circle(WIN, WHITE, ball_pos, BALL_RADIUS)

# Función para dibujar las paletas
def draw_paddles():
    pygame.draw.rect(WIN, WHITE, pygame.Rect(TEAM1_LEFT_PAD_POS[0], TEAM1_LEFT_PAD_POS[1], PAD_WIDTH, PAD_HEIGHT))
    pygame.draw.rect(WIN, WHITE, pygame.Rect(TEAM1_RIGHT_PAD_POS[0], TEAM1_RIGHT_PAD_POS[1], PAD_WIDTH, PAD_HEIGHT))
    pygame.draw.rect(WIN, WHITE, pygame.Rect(TEAM2_LEFT_PAD_POS[0], TEAM2_LEFT_PAD_POS[1], PAD_WIDTH, PAD_HEIGHT))
    pygame.draw.rect(WIN, WHITE, pygame.Rect(TEAM2_RIGHT_PAD_POS[0], TEAM2_RIGHT_PAD_POS[1], PAD_WIDTH, PAD_HEIGHT))

# Función para dibujar el marcador
def draw_score():
    score_text = font.render(f"{team1_player1_name} & {team1_player2_name}: {score_team1} - {score_team2} :{team2_player1_name} & {team2_player2_name}", True, WHITE)
    score_rect = score_text.get_rect(center=(WIDTH // 2, 50))
    WIN.blit(score_text, score_rect)

# Función para mostrar mensaje de ganador
def display_winner(winner):
    winner_text = font.render(f"¡{winner} ha ganado!", True, WHITE)
    winner_rect = winner_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WIN.blit(winner_text, winner_rect)
    pygame.display.update()
    pygame.time.wait(2000)  # Esperar 2 segundos antes de salir del juego

# Función para obtener el nombre de un jugador dentro de la ventana del juego
def get_player_name(prompt):
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

# Solicitar nombres de jugadores dentro de la ventana del juego
team1_player1_name = get_player_name("Ingrese el nombre del jugador 1 del equipo 1: ")
team1_player2_name = get_player_name("Ingrese el nombre del jugador 2 del equipo 1: ")
team2_player1_name = get_player_name("Ingrese el nombre del jugador 1 del equipo 2: ")
team2_player2_name = get_player_name("Ingrese el nombre del jugador 2 del equipo 2: ")

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
    global ball_pos, ball_vel, ball_served, score_team1, score_team2
    clock = pygame.time.Clock()

    # Realizar la cuenta regresiva
    countdown()

    # Bucle del juego
    running = True
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if not ball_served:
                        ball_served = True
                        ball_vel = [random.choice([-5, 5]), random.choice([-5, 5])]
                    else:
                        ball_pos = [WIDTH // 2, HEIGHT // 2]
                        ball_served = False
                elif event.key == pygame.K_ESCAPE:  # Detectar la tecla ESC
                    running = False  # Salir del bucle del juego si se presiona ESC

        # Movimiento de las paletas

        # Movimiento de las paletas del equipo 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and TEAM1_LEFT_PAD_POS[1] > 0:
            TEAM1_LEFT_PAD_POS[1] -= PAD_SPEED
        if keys[pygame.K_s] and TEAM1_LEFT_PAD_POS[1] < HEIGHT // 2 - PAD_HEIGHT:
            TEAM1_LEFT_PAD_POS[1] += PAD_SPEED
        if keys[pygame.K_t] and TEAM1_RIGHT_PAD_POS[1] > HEIGHT // 2:
            TEAM1_RIGHT_PAD_POS[1] -= PAD_SPEED
        if keys[pygame.K_g] and TEAM1_RIGHT_PAD_POS[1] < HEIGHT - PAD_HEIGHT:
            TEAM1_RIGHT_PAD_POS[1] += PAD_SPEED

        # Movimiento de las paletas del equipo 2
        if keys[pygame.K_o] and TEAM2_LEFT_PAD_POS[1] > 0:
            TEAM2_LEFT_PAD_POS[1] -= PAD_SPEED
        if keys[pygame.K_l] and TEAM2_LEFT_PAD_POS[1] < HEIGHT // 2 - PAD_HEIGHT:
            TEAM2_LEFT_PAD_POS[1] += PAD_SPEED
        if keys[pygame.K_UP] and TEAM2_RIGHT_PAD_POS[1] > HEIGHT // 2:
            TEAM2_RIGHT_PAD_POS[1] -= PAD_SPEED
        if keys[pygame.K_DOWN] and TEAM2_RIGHT_PAD_POS[1] < HEIGHT - PAD_HEIGHT:
            TEAM2_RIGHT_PAD_POS[1] += PAD_SPEED

        # Iniciar el movimiento de la pelota cuando se presiona Enter
        if ball_served:
            ball_pos[0] += ball_vel[0]
            ball_pos[1] += ball_vel[1]

            # Rebotar en la parte superior e inferior de la pantalla
            if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
                ball_vel[1] = -ball_vel[1]

            # Rebotar en las paletas del equipo 1
            if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
                if ball_pos[1] >= TEAM1_LEFT_PAD_POS[1] and ball_pos[1] <= TEAM1_LEFT_PAD_POS[1] + PAD_HEIGHT:
                    ball_vel[0] = -ball_vel[0]
                elif ball_pos[1] >= TEAM1_RIGHT_PAD_POS[1] and ball_pos[1] <= TEAM1_RIGHT_PAD_POS[1] + PAD_HEIGHT:
                    ball_vel[0] = -ball_vel[0]
                else:
                    score_team2 += 1
                    ball_served = False
                    ball_pos = [WIDTH // 2, HEIGHT // 2]
                    ball_vel = [random.choice([-5, 5]), random.choice([-5, 5])]
            # Rebotar en las paletas del equipo 2
            elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
                if ball_pos[1] >= TEAM2_LEFT_PAD_POS[1] and ball_pos[1] <= TEAM2_LEFT_PAD_POS[1] + PAD_HEIGHT:
                    ball_vel[0] = -ball_vel[0]
                elif ball_pos[1] >= TEAM2_RIGHT_PAD_POS[1] and ball_pos[1] <= TEAM2_RIGHT_PAD_POS[1] + PAD_HEIGHT:
                    ball_vel[0] = -ball_vel[0]
                else:
                    score_team1 += 1
                    ball_served = False
                    ball_pos = [WIDTH // 2, HEIGHT // 2]
                    ball_vel = [random.choice([-5, 5]), random.choice([-5, 5])]

            # Verificar si un equipo ha ganado
            if score_team1 >= 10:
                display_winner(f"{team1_player1_name} & {team1_player2_name}")
                break
            elif score_team2 >= 10:
                display_winner(f"{team2_player1_name} & {team2_player2_name}")
                break

        # Limpiar la pantalla
        WIN.fill(BLACK)

        # Dibujar elementos del juego
        draw_ball(ball_pos)
        draw_paddles()
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
