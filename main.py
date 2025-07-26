import pygame
import Matrizes
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Sudoku')

x, y = 850, 850
janela = pygame.display.set_mode([x, y])

pos_x_player = 430
pos_y_player = 400
vel_nave_player = 10


pressionado = False

precisa_redesenhar = True

linha_selecionada = None
coluna_selecionada = None



loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        elif events.type == pygame.MOUSEBUTTONDOWN:
            posicao_click_x, posicao_click_y = pygame.mouse.get_pos()
            if 140 < posicao_click_x < 760 and 230 < posicao_click_y < 840:
                coluna_selecionada = (posicao_click_x - 140) // 70
                linha_selecionada = (posicao_click_y - 230) // 70
                print(f"Célula clicada: [{linha_selecionada}][{coluna_selecionada}]")
                precisa_redesenhar = True
        elif events.type == pygame.KEYDOWN:
            if linha_selecionada is not None and coluna_selecionada is not None:
                if pygame.K_1 <= events.key <= pygame.K_9:
                    valor = events.key - pygame.K_0
                    Matrizes.Sudoku_playground[linha_selecionada][coluna_selecionada] = valor
                    precisa_redesenhar = True
                elif events.key == pygame.K_0:
                    Matrizes.Sudoku_playground[linha_selecionada][coluna_selecionada] = 0
                    precisa_redesenhar = True
                elif events.key == pygame.K_RETURN:
                    if Matrizes.verificacao():
                        print("Sudoku Resolvido")
                    else:
                        print("Sudoku Incompleto")
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

    numero_imagens = {
        1: numero_1,
        2: numero_2,
        3: numero_3,
        4: numero_4,
        5: numero_5,
        6: numero_6,
        7: numero_7,
        8: numero_8,
        9: numero_9
    }
    if precisa_redesenhar:
        for i, linha in enumerate(Matrizes.Sudoku_playground):
            for j, valor in enumerate(linha):
                if valor in numero_imagens:
                    janela.blit(numero_imagens[valor], (Matrizes.posicoes_x[j], Matrizes.posicoes_y[i]))

        pygame.display.update()  # Atualiza a tela
        precisa_redesenhar = False  # Reseta a flag



    clock.tick(60)

