import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('HYMFer Launcher')

# Set up fonts
font = pygame.font.Font(None, 30)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def show_menu():
    window.fill(WHITE)
    title_text = font.render("Bienvenido al lanzador de HYMFer", True, BLACK)
    window.blit(title_text, (50, 50))

    option1_text = font.render("1. Ejecutar Pong", True, BLACK)
    window.blit(option1_text, (50, 100))

    option2_text = font.render("2. Ejecutar Space Invaders", True, BLACK)
    window.blit(option2_text, (50, 150))

    option3_text = font.render("3. Créditos y más", True, BLACK)
    window.blit(option3_text, (50, 200))

    option4_text = font.render("4. Cerrar", True, BLACK)
    window.blit(option4_text, (50, 250))

def option1():
    print("Ejecutando Pong")
    # Add your code for Option 1 here

def option2():
    print("Ejecutando Space Invaders")
    # Add your code for Option 2 here

def option3():
    print("Mostrando créditos")
    # Add your code for Option 3 here

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    option1()
                elif event.key == pygame.K_2:
                    option2()
                elif event.key == pygame.K_3:
                    option3()
                elif event.key == pygame.K_4:
                    print("Cerrando. Gracias por jugar.")
                    pygame.quit()
                    sys.exit()

        show_menu()
        pygame.display.update()

if __name__ == "__main__":
    main()
