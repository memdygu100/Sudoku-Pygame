import pygame
pygame.display.set_caption('Sudoku')

x, y = 893, 850
janela = pygame.display.set_mode([x, y])

loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
    imagem_fundo = pygame.image.load("C:/Users/diego/OneDrive/Área de Trabalho/-/Pygame/Sudoku-Pygame/Assets/Tabuleiro.png")



    janela.blit(imagem_fundo, (0, 0))