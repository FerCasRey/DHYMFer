import pygame # type: ignore
import sys
import webbrowser
import textwrap

# Initialize Pygame
pygame.init()

# Set up window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Lanzador de DHYMFer')

# Set up fonts
font = pygame.font.Font(None, 30)

# Colors
global colorInd
colorInd = 0

color1 = [(255, 255, 255), (0,0,0), (0,40,255), (255,0,0), (0,255,0), (51,88,34)]
color2 = [(0, 0, 0), (255,255,255), (0,0,0), (0,0,0), (0,0,0), (181,165,86)]
theme = ['Noche', 'Día', 'Aqua', 'Igni', 'Matcha', 'GBoy']

def show_menu():
    window.fill(color2[colorInd])
    title_text = font.render("Bienvenido al lanzador de DHYMFer", True, color1[colorInd])
    window.blit(title_text, (50, 50))

    option1_text = font.render("1. Pong", True, color1[colorInd])
    window.blit(option1_text, (50, 100))

    option2_text = font.render("2. Space Invaders", True, color1[colorInd])
    window.blit(option2_text, (50, 150))

    option3_text = font.render("3. Tetris", True, color1[colorInd])
    window.blit(option3_text, (50, 200))

    option4_text = font.render("4. Configuración", True, color1[colorInd])
    window.blit(option4_text, (50, 250))

    option5_text = font.render("5. Créditos y más", True, color1[colorInd])
    window.blit(option5_text, (50, 300))

    option6_text = font.render("6. Cerrar", True, color1[colorInd])
    window.blit(option6_text, (50, 350))

def pong(): # Display Pong selection menu
    pygame.display.set_caption("Pong - Selector de modo")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Allow the user to press ESC to return to the main menu
                    running = False
                if event.key == pygame.K_1: # one player
                    print("Ejecutando Pong (1 vs 1)")
                    from subprocess import call
                    call(['python', 'Games/Pong/Pong1v1.py'])
                    
                if event.key == pygame.K_2: # two players
                    print("Ejecutando Pong (2 vs 2)")
                    from subprocess import call
                    call(['python', 'Games/Pong/Pong2v2.py'])
                    

        window.fill(color2[colorInd])

        
        #Instrucciones generales
        pongRul1 = font.render("Protege tu portería moviendo las palas.", True, color1[colorInd])
        pongRul1Rec = pongRul1.get_rect(center=(WINDOW_WIDTH//2, 60))
        window.blit(pongRul1, pongRul1Rec)

        pongRul2 = font.render("¡El primero en llegar a los 10 puntos gana!", True, color1[colorInd])
        pongRul2Rec = pongRul2.get_rect(center=(WINDOW_WIDTH//2, 90))
        window.blit(pongRul2, pongRul2Rec)

        #Instrucciones Pong 1v1
        pong1 = font.render("1. Pong 1 contra 1", True, color1[colorInd])
        pong1Rec = pong1.get_rect(center=(WINDOW_WIDTH // 2, 160))
        window.blit(pong1, pong1Rec)

        pong1Rul1 = font.render("Jugador 1 -> W(subir) S(bajar)", True, color1[colorInd])
        pong1Rul1Rec = pong1Rul1.get_rect(center=(WINDOW_WIDTH//2, 200))
        window.blit(pong1Rul1, pong1Rul1Rec)
        
        pong1Rul2 = font.render("Jugador 2 -> ArrUp(subir) ArrDown(bajar)", True, color1[colorInd])
        pong1Rul2Rec = pong1Rul2.get_rect(center=(WINDOW_WIDTH//2, 230))
        window.blit(pong1Rul2, pong1Rul2Rec)
        
        #Instrucciones Pong 2v2
        pong2 = font.render("2. Pong 2 contra 2", True, color1[colorInd])
        pong2Rec = pong2.get_rect(center=(WINDOW_WIDTH // 2, 300))
        window.blit(pong2, pong2Rec)

        pong2Rul1 = font.render("Jugador 1.1 -> W(subir) S(bajar)", True, color1[colorInd])
        pong2Rul1Rec = pong2Rul1.get_rect(center=(WINDOW_WIDTH//2, 360))
        window.blit(pong2Rul1, pong2Rul1Rec)
        
        pong2Rul2 = font.render("Jugador 1.2 -> T(subir) G(bajar)", True, color1[colorInd])
        pong2Rul2Rec = pong2Rul2.get_rect(center=(WINDOW_WIDTH//2, 390))
        window.blit(pong2Rul2, pong2Rul2Rec)

        pong2Rul3 = font.render("Jugador 2.1 -> O(subir) L(bajar)", True, color1[colorInd])
        pong2Rul3Rec = pong2Rul3.get_rect(center=(WINDOW_WIDTH//2, 430))
        window.blit(pong2Rul3, pong2Rul3Rec)
        
        pong2Rul4 = font.render("Jugador 2.2 -> ArrUp(subir) ArrDown(bajar)", True, color1[colorInd])
        pong2Rul4Rec = pong2Rul4.get_rect(center=(WINDOW_WIDTH//2, 460))
        window.blit(pong2Rul4, pong2Rul4Rec)


        pygame.display.update()

def SpaceInvaders(): # Display Pong selection menu
    pygame.display.set_caption("Space Invaders")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Allow the user to press ESC to return to the main menu
                    running = False
                if event.key == pygame.K_1: # one player                    
                    from subprocess import call
                    call(['python', 'Games/SpaceInvaders/SpaceInvaders.py'])

        window.fill(color2[colorInd])
        gameName = font.render("1. Space Invaders", True, color1[colorInd])
        gameNameRec = gameName.get_rect(center=(WINDOW_WIDTH//2, 100))
        window.blit(gameName, gameNameRec)

        gameRul1 = font.render("¡Dispara a los enemigos para salvar el mundo!", True, color1[colorInd])
        gameRul1Rec = gameRul1.get_rect(center=(WINDOW_WIDTH//2, 150))
        window.blit(gameRul1, gameRul1Rec)

        gameRul2 = font.render("Barra espaciadora (disparar)", True, color1[colorInd])
        gameRul2Rec = gameRul2.get_rect(center=(WINDOW_WIDTH//2, 180))
        window.blit(gameRul2, gameRul2Rec)
        
        gameRul3 = font.render("ArrLeft / ArrRight (desplazarse)", True, color1[colorInd])
        gameRul3Rec = gameRul3.get_rect(center=(WINDOW_WIDTH//2, 210))
        window.blit(gameRul3, gameRul3Rec)

        pygame.display.update()

    

def tetris():
    pygame.display.set_caption("Tetris")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Allow the user to press ESC to return to the main menu
                    running = False
                if event.key == pygame.K_1: # one player                    
                    from subprocess import call
                    call(['python', 'Games/Tetris/Tetris.py'])

        window.fill(color2[colorInd])
        gameName = font.render("1. Tetris", True, color1[colorInd])
        gameNameRec = gameName.get_rect(center=(WINDOW_WIDTH//2, 100))
        window.blit(gameName, gameNameRec)

        gameRul1 = font.render("Gana puntos completando líneas", True, color1[colorInd])
        gameRul1Rec = gameRul1.get_rect(center=(WINDOW_WIDTH//2, 150))
        window.blit(gameRul1, gameRul1Rec)

        gameRul2 = font.render("ArrUp (girar)", True, color1[colorInd])
        gameRul2Rec = gameRul2.get_rect(center=(WINDOW_WIDTH//2, 180))
        window.blit(gameRul2, gameRul2Rec)
        
        gameRul3 = font.render("ArrLeft / ArrRight (desplazar la pieza)", True, color1[colorInd])
        gameRul3Rec = gameRul3.get_rect(center=(WINDOW_WIDTH//2, 210))
        window.blit(gameRul3, gameRul3Rec)

        pygame.display.update()
    

def option3():
    print('Mostrando Configuración')
    config()

def option4():
    print("Mostrando Créditos")
    credits()
    # Add your code for Option 3 here

def main():
    pygame.display.set_caption('Lanzador de DHYMFer')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pong()
                elif event.key == pygame.K_2:
                    SpaceInvaders()
                elif event.key == pygame.K_3:
                    tetris()
                elif event.key == pygame.K_4:
                    config()
                elif event.key == pygame.K_5:
                    credits()
                elif event.key == (pygame.K_6) or event.key == (pygame.K_ESCAPE):
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
                if event.key == pygame.K_RIGHT:
                    global colorInd
                    global color1
                    if colorInd == (len(color1) - 1):
                        colorInd = 0
                    else:
                        colorInd += 1
                if event.key ==  pygame.K_LEFT:
                    if colorInd == 0:
                        colorInd = len(color1)-1
                    else:
                        colorInd -= 1




        window.fill(color2[colorInd])

        optText = font.render("- Configuración - ", True, color1[colorInd])
        optRec = optText.get_rect(center=(WINDOW_WIDTH // 2, 50))
        window.blit(optText, optRec)

        col1Text = font.render("Cambiar el tema", True, color1[colorInd])
        col1Rec = col1Text.get_rect(center=(WINDOW_WIDTH // 2, 100))
        window.blit(col1Text, col1Rec)

        colRArrow = font.render("<--", True, color1[colorInd])
        colRArrowRec = colRArrow.get_rect(center=(WINDOW_WIDTH // 2  - 70, 125))
        window.blit(colRArrow, colRArrowRec)

        col2Text = font.render(''+str(theme[colorInd]), True, color1[colorInd])
        col2Rec = col1Text.get_rect(center=(WINDOW_WIDTH // 2 + 45, 125))
        window.blit(col2Text, col2Rec)

        colLArrow = font.render("-->", True, color1[colorInd])
        colLArrowRec = colLArrow.get_rect(center=(WINDOW_WIDTH // 2  + 70, 125))
        window.blit(colLArrow, colLArrowRec)


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
                if event.key == pygame.K_b: # open issues of github repo
                    url = 'https://github.com/FerCasRey/DHYMFer/issues'
                    webbrowser.open_new_tab(url)


        window.fill(color2[colorInd])

        creTitle = font.render("- Créditos -" , True, color1[colorInd])
        optRec = creTitle.get_rect(center=(WINDOW_WIDTH // 2, 50))
        window.blit(creTitle, optRec)

        crePong = font.render("Pong - (D)iego" , True, color1[colorInd])
        pongRec = crePong.get_rect(center=(WINDOW_WIDTH // 2, 100))
        window.blit(crePong, pongRec)

        creArt = font.render("Arte - (H)ugo" , True, color1[colorInd])
        artRec = creArt.get_rect(center=(WINDOW_WIDTH // 2, 125))
        window.blit(creArt, artRec)
        
        creSpa = font.render("Space Invader - (Y)oel" , True, color1[colorInd])
        spaRec = creSpa.get_rect(center=(WINDOW_WIDTH // 2, 150))
        window.blit(creSpa, spaRec)

        creTet = font.render("Tetris - (M)ateo" , True, color1[colorInd])
        tetRec = creTet.get_rect(center=(WINDOW_WIDTH // 2, 175))
        window.blit(creTet, tetRec)

        creMen = font.render("Menú - (F)ernando" , True, color1[colorInd])
        menRec = creMen.get_rect(center=(WINDOW_WIDTH // 2, 200))
        window.blit(creMen, menRec)

        creGit = font.render('Pulsa \'B\' para reportar fallos', True, color1[colorInd])
        gitRec = creGit.get_rect(center=(WINDOW_WIDTH//2, 300))
        window.blit(creGit,gitRec)


        pygame.display.update()


if __name__ == "__main__":
    main()
