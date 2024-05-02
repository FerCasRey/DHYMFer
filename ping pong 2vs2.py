import pygame
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

# Nombres de los jugadores
team1_player1_name = input("Ingrese el nombre del jugador 1 del equipo 1: ")
team1_player2_name = input("Ingrese el nombre del jugador 2 del equipo 1: ")
team2_player1_name = input("Ingrese el nombre del jugador 1 del equipo 2: ")
team2_player2_name = input("Ingrese el nombre del jugador 2 del equipo 2: ")

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
    score_text = font.render(f"{team1_player1_name} & {team1_player2_name}: {score_team1} - {team2_player1_name} & {team2_player2_name}: {score_team2}", True, WHITE)
    score_rect = score_text.get_rect(center=(WIDTH // 2, 50))
    WIN.blit(score_text, score_rect)

# Función principal del juego
def main():
    global ball_pos, ball_vel, score_team1, score_team2
    clock = pygame.time.Clock()

    # Bucle del juego
    running = True
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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
        if keys[pygame.K_UP] and TEAM2_LEFT_PAD_POS[1] > 0:
            TEAM2_LEFT_PAD_POS[1] -= PAD_SPEED
        if keys[pygame.K_DOWN] and TEAM2_LEFT_PAD_POS[1] < HEIGHT // 2 - PAD_HEIGHT:
            TEAM2_LEFT_PAD_POS[1] += PAD_SPEED
        if keys[pygame.K_o] and TEAM2_RIGHT_PAD_POS[1] > HEIGHT // 2:
            TEAM2_RIGHT_PAD_POS[1] -= PAD_SPEED
        if keys[pygame.K_l] and TEAM2_RIGHT_PAD_POS[1] < HEIGHT - PAD_HEIGHT:
            TEAM2_RIGHT_PAD_POS[1] += PAD_SPEED

        # Movimiento de la pelota
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
                ball_pos = [WIDTH // 2, HEIGHT // 2]
                ball_vel = [random.choice([-5, 5]), random.choice([-5, 5])]

        # Limpiar la pantalla
        WIN.fill(BLACK)

        # Dibujar elementos del juego
        draw_ball(ball_pos)
        draw_paddles()
        draw_score()

        # Verificar si un equipo ha ganado
        if score_team1 >= 10 or score_team2 >= 10:
            if score_team1 > score_team2:
                winner_text = font.render(f"{team1_player1_name} & {team1_player2_name} han ganado!", True, WHITE)
            else:
                winner_text = font.render(f"{team2_player1_name} & {team2_player2_name} han ganado!", True, WHITE)
            winner_rect = winner_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            WIN.blit(winner_text, winner_rect)
            pygame.display.update()
            pygame.time.wait(3000)  # Esperar 3 segundos antes de salir del juego
            break

        # Actualizar la pantalla
        pygame.display.update()

        # Establecer el número de fotogramas por segundo
        clock.tick(60)

    # Salir de Pygame
    pygame.quit()

# Llamar a la función principal del juego
if __name__ == "__main__":
    main()