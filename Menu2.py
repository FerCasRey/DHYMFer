import pygame
import sys


# Initialize Pygame
pygame.init()

# Set up window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Lanzador de HYMFer')

# Set up fonts
font = pygame.font.Font(None, 30)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def show_menu():
    window.fill(BLACK)
    title_text = font.render("Bienvenido al lanzador de HYMFer", True, WHITE)
    window.blit(title_text, (50, 50))

    option1_text = font.render("1. Ejecutar Pong", True, WHITE)
    window.blit(option1_text, (50, 100))

    option2_text = font.render("2. Ejecutar Space Invaders", True, WHITE)
    window.blit(option2_text, (50, 150))

    option3_text = font.render("3. Configuración", True, WHITE)
    window.blit(option3_text, (50, 200))

    option4_text = font.render("4. Créditos y más", True, WHITE)
    window.blit(option4_text, (50, 250))

    option5_text = font.render("5. Cerrar", True, WHITE)
    window.blit(option5_text, (50, 300))

def option1():
    print("Ejecutando Pong")
    from subprocess import call
    call(['python', 'Pong_juego.py'])

    # Add your code for Option 1 here

def option2():
    print("Ejecutando Space Invaders")
    # Add your code for Option 2 here

def option3():
    print('Mostrando Configuración')
    config()

def option4():
    print("Mostrando créditos")
    credits()
    # Add your code for Option 3 here

def main():
    pygame.display.set_caption('Lanzador de HYMFer')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    option1()
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_2:
                    option2()
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_3:
                    option3()
                elif event.key == pygame.K_4:
                    option4()
                elif event.key == (pygame.K_5) or event.key == (pygame.K_ESCAPE):
                    print("Cerrando. Gracias por jugar.")
                    pygame.quit()
                    sys.exit()

        show_menu()
        pygame.display.update()

def config():
    pygame.display.set_caption("Configuración")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Allow the user to press ESC to return to the main menu
                    running = False

        window.fill(BLACK)
        optText = font.render("- Configuración - ", True, WHITE)
        optRec = optText.get_rect(center=(WINDOW_WIDTH // 2, 50))
        window.blit(optText, optRec)
        pygame.display.update()

def credits():
    pygame.display.set_caption("Créditos")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Allow the user to press ESC to return to the main menu
                    running = False

        window.fill(BLACK)

        creTitle = font.render("- Créditos -" , True, WHITE)
        optRec = creTitle.get_rect(center=(WINDOW_WIDTH // 2, 50))
        window.blit(creTitle, optRec)

        crePong = font.render("Pong - (M)ateo" , True, WHITE)
        pongRec = crePong.get_rect(center=(WINDOW_WIDTH // 2, 100))
        window.blit(crePong, pongRec)

        creSpa = font.render("Space Invader - (Y)oel" , True, WHITE)
        spaRec = creSpa.get_rect(center=(WINDOW_WIDTH // 2, 125))
        window.blit(creSpa, spaRec)

        creArt = font.render("Arte - (h)ugo" , True, WHITE)
        artRec = creArt.get_rect(center=(WINDOW_WIDTH // 2, 150))
        window.blit(creArt, artRec)

        creMen = font.render("Menú - (F)ernando" , True, WHITE)
        menRec = creMen.get_rect(center=(WINDOW_WIDTH // 2, 175))
        window.blit(creMen, menRec)


        pygame.display.update()


if __name__ == "__main__":
    main()
