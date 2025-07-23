import pygame
pygame.display.set_caption('Sudoku')

x, y = 850, 850
janela = pygame.display.set_mode([x, y])

pos_x_player = 430
pos_y_player = 400
vel_nave_player = 10



loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    teclas = pygame.key.get_pressed()

    if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and pos_y_player > 1:
        pos_y_player -= vel_nave_player

    if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and pos_y_player < 440:
        pos_y_player += vel_nave_player

    if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and pos_x_player > 1:
        pos_x_player -= vel_nave_player

    if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and pos_x_player < 870:
        pos_x_player += vel_nave_player



    imagem_fundo = pygame.image.load("C:/Users/diego/OneDrive/Área de Trabalho/-/Pygame/Sudoku-Pygame/Assets/Tabuleiro.png")
    nave_player = pygame.image.load("C:/Users/diego/PycharmProjects/PythonProject/Jogos Pygame/Jogo de Aprendizado/Assets/sprite_nave_pequena.png")
    nave_player = pygame.transform.scale(nave_player, (30, 30))
    numero_um = pygame.image.load("C:/Users/diego/OneDrive/Área de Trabalho/-/Pygame/Sudoku-Pygame/Assets/Numero_1-Photoroom.jpg")
    numero_um = pygame.transform.scale(numero_um, (55, 55))




    janela.blit(imagem_fundo, (0, 0))
    janela.blit(numero_um, (420, 510))

    janela.blit(nave_player, (pos_x_player, pos_y_player))
    print(pos_x_player, pos_y_player)


    pygame.display.update()

    #230, 250 -> 215, 240