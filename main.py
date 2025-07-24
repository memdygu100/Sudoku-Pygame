import pygame
import Matrizes
pygame.init()
pygame.display.set_caption('Sudoku')

x, y = 850, 850
janela = pygame.display.set_mode([x, y])

pos_x_player = 430
pos_y_player = 400
vel_nave_player = 10


pressionado = False





loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if pressionado:
            if (posicao_click_x > 140 and posicao_click_y > 230) and (posicao_click_x < 210 and posicao_click_y < 300):
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_1:
                        Matrizes.Sudoku_playground[0][0] = 1
                        pressionado = False
    teclas = pygame.key.get_pressed()




    imagem_fundo = pygame.image.load("Assets/Tabuleiro.png")
    numero_1 = pygame.image.load("Assets/Numero_1-Photoroom.jpg")
    numero_1 = pygame.transform.scale(numero_1, (55, 55))
    numero_2 = pygame.image.load("Assets/Numero_2-Photoroom.jpg")
    numero_2 = pygame.transform.scale(numero_2, (55, 55))
    numero_3 = pygame.image.load("Assets/Numero_3-Photoroom.jpg")
    numero_3 = pygame.transform.scale(numero_3, (55, 55))
    numero_4 = pygame.image.load("Assets/Numero_4-Photoroom.jpg")
    numero_4 = pygame.transform.scale(numero_4, (55, 55))
    numero_5 = pygame.image.load("Assets/Numero_5-Photoroom.jpg")
    numero_5 = pygame.transform.scale(numero_5, (55, 55))
    numero_6 = pygame.image.load("Assets/Numero_6-Photoroom.jpg")
    numero_6 = pygame.transform.scale(numero_6, (55, 55))
    numero_7 = pygame.image.load("Assets/Numero_7-Photoroom.jpg")
    numero_7 = pygame.transform.scale(numero_7, (55, 55))
    numero_8 = pygame.image.load("Assets/Numero_8-Photoroom.jpg")
    numero_8 = pygame.transform.scale(numero_8, (55, 55))
    numero_9 = pygame.image.load("Assets/Numero_9-Photoroom.jpg")
    numero_9 = pygame.transform.scale(numero_9, (55, 55))

    janela.blit(imagem_fundo, (0, 0))





    janela.blit(numero_1, (215, 240))


    y = 0
    for i in range(len(Matrizes.Sudoku_playground)):
        x = 0
        for j in range(len(Matrizes.Sudoku_playground)):
            if Matrizes.Sudoku_playground[i][j] == 1:
                janela.blit(numero_1, (Matrizes.posicoes_x[x], Matrizes.posicoes_y[y]))
            elif Matrizes.Sudoku_playground[i][j] == 2:
                janela.blit(numero_2, (Matrizes.posicoes_x[x], Matrizes.posicoes_y[y]))
            elif Matrizes.Sudoku_playground[i][j] == 3:
                janela.blit(numero_3, (Matrizes.posicoes_x[x], Matrizes.posicoes_y[y]))
            elif Matrizes.Sudoku_playground[i][j] == 4:
                janela.blit(numero_4, (Matrizes.posicoes_x[x], Matrizes.posicoes_y[y]))
            elif Matrizes.Sudoku_playground[i][j] == 5:
                janela.blit(numero_5, (Matrizes.posicoes_x[x], Matrizes.posicoes_y[y]))
            elif Matrizes.Sudoku_playground[i][j] == 6:
                janela.blit(numero_6, (Matrizes.posicoes_x[x], Matrizes.posicoes_y[y]))
            elif Matrizes.Sudoku_playground[i][j] == 7:
                janela.blit(numero_7, (Matrizes.posicoes_x[x], Matrizes.posicoes_y[y]))
            elif Matrizes.Sudoku_playground[i][j] == 8:
                janela.blit(numero_8, (Matrizes.posicoes_x[x], Matrizes.posicoes_y[y]))
            elif Matrizes.Sudoku_playground[i][j] == 9:
                janela.blit(numero_9, (Matrizes.posicoes_x[x], Matrizes.posicoes_y[y]))


            x += 1
        y += 1

    if  events.type == pygame.MOUSEBUTTONDOWN:
        posicao_click_x, posicao_click_y = pygame.mouse.get_pos()
        pressionado = True
        print(posicao_click_x, posicao_click_y)

















    pygame.display.update()
