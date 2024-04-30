import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SPEED = 5
PADDLE_SPEED = 5

# Function to draw paddles
def draw_paddle(paddle):
    pygame.draw.rect(SCREEN, WHITE, paddle)

# Function to draw ball
def draw_ball(ball):
    pygame.draw.circle(SCREEN, WHITE, ball, BALL_RADIUS)

# Function to move ball
def move_ball(ball, ball_speed, ball_direction):
    ball[0] += ball_speed * ball_direction[0]
    ball[1] += ball_speed * ball_direction[1]

# Function to check collision with paddle
def check_collision(ball, paddle1, paddle2):
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        return True
    return False

# Main function
def main():
    # Initialize paddles and ball
    paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = [WIDTH // 2, HEIGHT // 2]
    ball_direction = [random.choice([-1, 1]), random.choice([-1, 1])]

    # Dictionary to keep track of pressed keys
    keys = {pygame.K_w: False, pygame.K_s: False, pygame.K_UP: False, pygame.K_DOWN: False}

    # Game loop
    while True:
        SCREEN.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key in keys:
                    keys[event.key] = True
            elif event.type == pygame.KEYUP:
                if event.key in keys:
                    keys[event.key] = False

        # Move paddles based on key states
        if keys[pygame.K_w] and paddle1.top > 0:
            paddle1.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
            paddle1.y += PADDLE_SPEED
        if keys[pygame.K_UP] and paddle2.top > 0:
            paddle2.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
            paddle2.y += PADDLE_SPEED

        # Move ball
        move_ball(ball, BALL_SPEED, ball_direction)

        # Draw paddles and ball
        draw_paddle(paddle1)
        draw_paddle(paddle2)
        draw_ball(ball)

        # Check collision with paddles
        if ball[0] <= 0 or ball[0] >= WIDTH:
            ball_direction[0] *= -1
        if ball[1] <= 0 or ball[1] >= HEIGHT:
            ball_direction[1] *= -1
        if check_collision(pygame.Rect(ball[0] - BALL_RADIUS, ball[1] - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2), paddle1, paddle2):
            ball_direction[0] *= -1

        # Update display
        pygame.display.update()

        # Set FPS
        pygame.time.Clock().tick(60)

# Run the game
if __name__ == "__main__":
    main()
