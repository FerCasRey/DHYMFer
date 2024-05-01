import pygame
import sys


# Initialize Pygame
pygame.init()

# Set up window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Lanzador de HYMFer')

# Set up fonts
font = pygame.font.Font(None, 30)

# Colors
global colorInd1
colorInd1 = 0
global colorInd2
colorInd2 = 0

color1 = [(255, 255, 255), (0,0,0), (0,40,255), (255,0,0), (0,255,0), (51,88,34)]
color2 = [(0, 0, 0), (255,255,255), (0,0,0), (0,0,0), (0,0,0), (181,165,86)]
theme = ['Noche', 'Día', 'Aqua', 'Igni', 'Matcha', 'GBoy']
colorInd1Len = len(color1) - 1
colorInd2Len = len(color2) - 1

def changeColor():
    global colorInd1
    global colorInd2
    if colorInd1 < colorInd1Len: 
        colorInd1 += 1
        colorInd2 += 1 
    else:
        colorInd1 = 0
        colorInd2 = 0

def show_menu():
    window.fill(color2[colorInd2])
    title_text = font.render("Bienvenido al lanzador de HYMFer", True, color1[colorInd1])
    window.blit(title_text, (50, 50))

    option1_text = font.render("1. Ejecutar Pong", True, color1[colorInd1])
    window.blit(option1_text, (50, 100))

    option2_text = font.render("2. Ejecutar Space Invaders", True, color1[colorInd1])
    window.blit(option2_text, (50, 150))

    option3_text = font.render("3. Configuración", True, color1[colorInd1])
    window.blit(option3_text, (50, 200))

    option4_text = font.render("4. Créditos y más", True, color1[colorInd1])
    window.blit(option4_text, (50, 250))

    option5_text = font.render("5. Cerrar", True, color1[colorInd1])
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
    print("Mostrando Créditos")
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
                if event.key == pygame.K_c:
                    changeColor()



        window.fill(color2[colorInd2])
        optText = font.render("- Configuración - ", True, color1[colorInd1])
        optRec = optText.get_rect(center=(WINDOW_WIDTH // 2, 50))
        window.blit(optText, optRec)

        col1Text = font.render("Pulsa \'c\' para cambiar el color del tema", True, color1[colorInd1])
        col1Rec = col1Text.get_rect(center=(WINDOW_WIDTH // 2, 100))
        window.blit(col1Text, col1Rec)

        col2Text = font.render("Tema actual:  " + str(theme[colorInd1] + " "), True, color1[colorInd1])
        col2Rec = col1Text.get_rect(center=(WINDOW_WIDTH // 2, 125))
        window.blit(col2Text, col2Rec)


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

        window.fill(color2[colorInd2])

        creTitle = font.render("- Créditos -" , True, color1[colorInd1])
        optRec = creTitle.get_rect(center=(WINDOW_WIDTH // 2, 50))
        window.blit(creTitle, optRec)

        creArt = font.render("Arte - (H)ugo" , True, color1[colorInd1])
        artRec = creArt.get_rect(center=(WINDOW_WIDTH // 2, 100))
        window.blit(creArt, artRec)
        
        creSpa = font.render("Space Invader - (Y)oel" , True, color1[colorInd1])
        spaRec = creSpa.get_rect(center=(WINDOW_WIDTH // 2, 125))
        window.blit(creSpa, spaRec)

        crePong = font.render("Pong - (M)ateo" , True, color1[colorInd1])
        pongRec = crePong.get_rect(center=(WINDOW_WIDTH // 2, 150))
        window.blit(crePong, pongRec)

        creMen = font.render("Menú - (F)ernando" , True, color1[colorInd1])
        menRec = creMen.get_rect(center=(WINDOW_WIDTH // 2, 175))
        window.blit(creMen, menRec)


        pygame.display.update()


if __name__ == "__main__":
    main()
