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
            if posicao_click_y > 230 and posicao_click_y < 300:

                if posicao_click_x > 140 and posicao_click_x < 210:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[0][0] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[0][0] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[0][0] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[0][0] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[0][0] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[0][0] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[0][0] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[0][0] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[0][0] = 9
                            pressionado = False
                elif posicao_click_x > 210 and posicao_click_x < 270:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[0][1] = 1
                            pressionado = False
                        if events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[0][1] = 2
                            pressionado = False
                        if events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[0][1] = 3
                            pressionado = False
                        if events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[0][1] = 4
                            pressionado = False
                        if events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[0][1] = 5
                            pressionado = False
                        if events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[0][1] = 6
                            pressionado = False
                        if events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[0][1] = 7
                            pressionado = False
                        if events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[0][1] = 8
                            pressionado = False
                        if events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[0][1] = 9
                            pressionado = False
                elif posicao_click_x > 270 and posicao_click_x < 340:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[0][2] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[0][2] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[0][2] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[0][2] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[0][2] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[0][2] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[0][2] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[0][2] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[0][2] = 9
                            pressionado = False
                elif posicao_click_x > 340 and posicao_click_x < 410:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[0][3] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[0][3] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[0][3] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[0][3] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[0][3] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[0][3] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[0][3] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[0][3] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[0][3] = 9
                            pressionado = False
                elif posicao_click_x > 410 and posicao_click_x < 480:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[0][4] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[0][4] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[0][4] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[0][4] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[0][4] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[0][4] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[0][4] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[0][4] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[0][4] = 9
                            pressionado = False
                elif posicao_click_x > 480 and posicao_click_x < 550:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[0][5] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[0][5] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[0][5] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[0][5] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[0][5] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[0][5] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[0][5] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[0][5] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[0][5] = 9
                            pressionado = False
                elif posicao_click_x > 550 and posicao_click_x < 620:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[0][6] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[0][6] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[0][6] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[0][6] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[0][6] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[0][6] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[0][6] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[0][6] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[0][6] = 9
                            pressionado = False
                elif posicao_click_x > 620 and posicao_click_x < 690:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[0][7] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[0][7] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[0][7] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[0][7] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[0][7] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[0][7] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[0][7] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[0][7] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[0][7] = 9
                            pressionado = False
                elif posicao_click_x > 690 and posicao_click_x < 760:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[1][0] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[1][0] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[1][0] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[1][0] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[1][0] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[1][0] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[1][0] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[1][0] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[1][0] = 9
                            pressionado = False
            elif posicao_click_y > 300 and posicao_click_y < 370:

                if posicao_click_x > 140 and posicao_click_x < 210:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[1][0] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[1][0] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[1][0] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[1][0] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[1][0] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[1][0] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[1][0] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[1][0] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[1][0] = 9
                            pressionado = False
                elif posicao_click_x > 210 and posicao_click_x < 270:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[1][1] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[1][1] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[1][1] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[1][1] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[1][1] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[1][1] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[1][1] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[1][1] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[1][1] = 9
                            pressionado = False
                elif posicao_click_x > 270 and posicao_click_x < 340:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[1][2] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[1][2] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[1][2] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[1][2] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[1][2] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[1][2] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[1][2] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[1][2] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[1][2] = 9
                            pressionado = False
                elif posicao_click_x > 340 and posicao_click_x < 410:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[1][3] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[1][3] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[1][3] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[1][3] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[1][3] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[1][3] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[1][3] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[1][3] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[1][3] = 9
                            pressionado = False
                elif posicao_click_x > 410 and posicao_click_x < 480:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[1][4] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[1][4] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[1][4] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[1][4] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[1][4] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[1][4] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[1][4] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[1][4] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[1][4] = 9
                            pressionado = False
                elif posicao_click_x > 480 and posicao_click_x < 550:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[1][5] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[1][5] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[1][5] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[1][5] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[1][5] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[1][5] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[1][5] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[1][5] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[1][5] = 9
                            pressionado = False
                elif posicao_click_x > 550 and posicao_click_x < 620:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[1][6] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[1][6] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[1][6] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[1][6] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[1][6] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[1][6] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[1][6] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[1][6] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[1][6] = 9
                            pressionado = False
                elif posicao_click_x > 620 and posicao_click_x < 690:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[1][7] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[1][7] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[1][7] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[1][7] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[1][7] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[1][7] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[1][7] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[1][7] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[1][7] = 9
                            pressionado = False
                elif posicao_click_x > 690 and posicao_click_x < 760:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[1][8] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[1][8] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[1][8] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[1][8] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[1][8] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[1][8] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[1][8] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[1][8] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[1][8] = 9
                            pressionado = False
            elif posicao_click_y > 370 and posicao_click_y < 430:

                if posicao_click_x > 140 and posicao_click_x < 210:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[2][0] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[2][0] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[2][0] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[2][0] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[2][0] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[2][0] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[2][0] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[2][0] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[2][0] = 9
                            pressionado = False
                elif posicao_click_x > 210 and posicao_click_x < 270:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[2][1] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[2][1] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[2][1] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[2][1] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[2][1] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[2][1] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[2][1] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[2][1] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[2][1] = 9
                            pressionado = False
                elif posicao_click_x > 270 and posicao_click_x < 340:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[2][2] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[2][2] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[2][2] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[2][2] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[2][2] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[2][2] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[2][2] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[2][2] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[2][2] = 9
                            pressionado = False
                elif posicao_click_x > 340 and posicao_click_x < 410:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[2][3] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[2][3] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[2][3] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[2][3] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[2][3] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[2][3] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[2][3] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[2][3] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[2][3] = 9
                            pressionado = False
                elif posicao_click_x > 410 and posicao_click_x < 480:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[2][4] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[2][4] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[2][4] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[2][4] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[2][4] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[2][4] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[2][4] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[2][4] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[2][4] = 9
                            pressionado = False
                elif posicao_click_x > 480 and posicao_click_x < 550:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[2][5] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[2][5] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[2][5] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[2][5] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[2][5] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[2][5] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[2][5] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[2][5] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[2][5] = 9
                            pressionado = False
                elif posicao_click_x > 550 and posicao_click_x < 620:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[2][6] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[2][6] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[2][6] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[2][6] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[2][6] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[2][6] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[2][6] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[2][6] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[2][6] = 9
                            pressionado = False
                elif posicao_click_x > 620 and posicao_click_x < 690:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[2][7] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[2][8] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[2][8] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[2][8] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[2][8] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[2][8] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[2][8] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[2][8] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[2][8] = 9
                            pressionado = False
                elif posicao_click_x > 690 and posicao_click_x < 760:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[2][8] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[2][8] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[2][8] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[2][8] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[2][8] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[2][8] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[2][8] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[2][8] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[2][8] = 9
                            pressionado = False
            elif posicao_click_y > 430 and posicao_click_y < 500:

                if posicao_click_x > 140 and posicao_click_x < 210:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[3][0] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[3][0] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[3][0] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[3][0] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[3][0] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[3][0] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[3][0] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[3][0] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[3][0] = 9
                            pressionado = False
                elif posicao_click_x > 210 and posicao_click_x < 270:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[3][1] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[3][1] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[3][1] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[3][1] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[3][1] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[3][1] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[3][1] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[3][1] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[3][1] = 9
                            pressionado = False
                elif posicao_click_x > 270 and posicao_click_x < 340:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[3][2] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[3][2] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[3][2] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[3][2] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[3][2] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[3][2] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[3][2] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[3][2] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[3][2] = 9
                            pressionado = False
                elif posicao_click_x > 340 and posicao_click_x < 410:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[3][3] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[3][3] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[3][3] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[3][3] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[3][3] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[3][3] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[3][3] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[3][3] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[3][3] = 9
                            pressionado = False
                elif posicao_click_x > 410 and posicao_click_x < 480:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[3][4] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[3][4] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[3][4] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[3][4] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[3][4] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[3][4] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[3][4] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[3][4] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[3][4] = 9
                            pressionado = False
                elif posicao_click_x > 480 and posicao_click_x < 550:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[3][5] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[3][5] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[3][5] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[3][5] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[3][5] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[3][5] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[3][5] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[3][5] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[3][0] = 9
                            pressionado = False
                elif posicao_click_x > 550 and posicao_click_x < 620:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[3][6] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[3][6] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[3][6] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[3][6] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[3][6] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[3][6] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[3][6] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[3][6] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[3][6] = 9
                            pressionado = False
                elif posicao_click_x > 620 and posicao_click_x < 690:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[3][7] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[3][7] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[3][7] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[3][7] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[3][7] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[3][7] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[3][7] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[3][7] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[3][7] = 9
                            pressionado = False
                elif posicao_click_x > 690 and posicao_click_x < 760:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[3][8] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[3][8] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[3][8] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[3][8] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[3][8] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[3][8] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[3][8] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[3][8] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[3][8] = 9
                            pressionado = False
            elif posicao_click_y > 500 and posicao_click_y < 570:

                if posicao_click_x > 140 and posicao_click_x < 210:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[4][0] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[4][0] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[4][0] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[4][0] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[4][0] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[4][0] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[4][0] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[4][0] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[4][0] = 9
                            pressionado = False
                elif posicao_click_x > 210 and posicao_click_x < 270:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[4][1] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[4][1] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[4][1] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[4][1] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[4][1] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[4][1] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[4][1] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[4][1] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[4][1] = 9
                            pressionado = False
                elif posicao_click_x > 270 and posicao_click_x < 340:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[4][2] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[4][2] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[4][2] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[4][2] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[4][2] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[4][2] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[4][2] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[4][2] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[4][2] = 9
                            pressionado = False
                elif posicao_click_x > 340 and posicao_click_x < 410:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[4][3] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[4][3] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[4][3] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[4][3] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[4][3] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[4][3] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[4][3] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[4][3] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[4][3] = 9
                            pressionado = False
                elif posicao_click_x > 410 and posicao_click_x < 480:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[4][4] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[4][4] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[4][4] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[4][4] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[4][4] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[4][4] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[4][4] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[4][4] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[4][4] = 9
                            pressionado = False
                elif posicao_click_x > 480 and posicao_click_x < 550:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[4][5] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[4][5] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[4][5] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[4][5] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[4][5] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[4][5] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[4][5] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[4][5] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[4][5] = 9
                            pressionado = False
                elif posicao_click_x > 550 and posicao_click_x < 620:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[4][6] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[4][6] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[4][6] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[4][6] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[4][6] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[4][6] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[4][6] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[4][6] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[4][6] = 9
                            pressionado = False
                elif posicao_click_x > 620 and posicao_click_x < 690:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[4][7] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[4][7] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[4][7] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[4][7] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[4][7] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[4][7] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[4][7] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[4][7] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[4][7] = 9
                            pressionado = False
                elif posicao_click_x > 690 and posicao_click_x < 760:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[4][8] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[4][8] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[4][8] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[4][8] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[4][8] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[4][8] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[4][8] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[4][8] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[4][8] = 9
                            pressionado = False
            elif posicao_click_y > 570 and posicao_click_y < 640:

                if posicao_click_x > 140 and posicao_click_x < 210:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[5][0] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[5][0] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[5][0] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[5][0] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[5][0] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[5][0] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[5][0] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[5][0] = 9
                            pressionado = False
                elif posicao_click_x > 210 and posicao_click_x < 270:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[5][1] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[5][1] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[5][1] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[5][1] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[5][1] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[5][1] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[5][1] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[5][1] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[5][1] = 9
                            pressionado = False
                elif posicao_click_x > 270 and posicao_click_x < 340:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[5][2] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[5][2] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[5][2] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[5][2] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[5][2] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[5][2] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[5][2] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[5][2] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[5][2] = 9
                            pressionado = False
                elif posicao_click_x > 340 and posicao_click_x < 410:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[5][3] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[5][3] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[5][3] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[5][3] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[5][3] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[5][3] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[5][3] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[5][3] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[5][3] = 9
                            pressionado = False
                elif posicao_click_x > 410 and posicao_click_x < 480:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[5][4] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[5][4] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[5][4] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[5][4] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[5][4] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[5][4] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[5][4] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[5][4] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[5][4] = 9
                            pressionado = False
                elif posicao_click_x > 480 and posicao_click_x < 550:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[5][5] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[5][5] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[5][5] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[5][5] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[5][5] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[5][5] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[5][5] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[5][5] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[5][5] = 9
                            pressionado = False
                elif posicao_click_x > 550 and posicao_click_x < 620:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[5][6] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[5][6] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[5][6] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[5][6] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[5][6] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[5][6] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[5][6] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[5][6] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[5][6] = 9
                            pressionado = False
                elif posicao_click_x > 620 and posicao_click_x < 690:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[5][7] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[5][7] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[5][7] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[5][7] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[5][7] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[5][7] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[5][7] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[5][7] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[5][7] = 9
                            pressionado = False
                elif posicao_click_x > 690 and posicao_click_x < 760:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[5][8] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[5][8] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[5][8] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[5][8] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[5][8] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[5][8] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[5][8] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[5][8] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[5][8] = 9
                            pressionado = False
            elif posicao_click_y > 640 and posicao_click_y < 700:

                if posicao_click_x > 140 and posicao_click_x < 210:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[6][0] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[6][0] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[6][0] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[6][0] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[6][0] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[6][0] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[6][0] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[6][0] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[6][0] = 9
                            pressionado = False
                elif posicao_click_x > 210 and posicao_click_x < 270:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[6][1] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[6][1] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[6][1] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[6][1] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[6][1] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[6][1] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[6][1] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[6][1] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[6][1] = 9
                            pressionado = False
                elif posicao_click_x > 270 and posicao_click_x < 340:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[6][2] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[6][2] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[6][2] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[6][2] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[6][2] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[6][2] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[6][2] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[6][2] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[6][2] = 9
                            pressionado = False
                elif posicao_click_x > 340 and posicao_click_x < 410:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[6][3] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[6][3] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[6][3] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[6][3] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[6][3] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[6][3] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[6][3] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[6][3] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[6][3] = 9
                            pressionado = False
                elif posicao_click_x > 410 and posicao_click_x < 480:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[6][4] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[6][4] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[6][4] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[6][4] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[6][4] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[6][4] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[6][4] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[6][4] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[6][4] = 9
                            pressionado = False
                elif posicao_click_x > 480 and posicao_click_x < 550:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[6][5] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[6][5] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[6][5] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[6][5] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[6][5] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[6][5] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[6][5] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[6][5] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[6][5] = 9
                            pressionado = False
                elif posicao_click_x > 550 and posicao_click_x < 620:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[6][6] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[6][6] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[6][6] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[6][6] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[6][6] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[6][6] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[6][6] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[6][6] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[6][6] = 9
                            pressionado = False
                elif posicao_click_x > 620 and posicao_click_x < 690:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[6][7] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[6][7] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[6][7] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[6][7] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[6][7] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[6][7] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[6][7] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[6][7] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[6][7] = 9
                            pressionado = False
                elif posicao_click_x > 690 and posicao_click_x < 760:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[6][8] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[6][8] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[6][8] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[6][8] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[6][8] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[6][8] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[6][8] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[6][8] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[6][8] = 9
                            pressionado = False
            elif posicao_click_y > 700 and posicao_click_y < 770:

                if posicao_click_x > 140 and posicao_click_x < 210:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[7][0] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[7][0] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[7][0] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[7][0] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[7][0] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[7][0] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[7][0] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[7][0] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[7][0] = 9
                            pressionado = False
                elif posicao_click_x > 210 and posicao_click_x < 270:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[7][1] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[7][1] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[7][1] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[7][1] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[7][1] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[7][1] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[7][1] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[7][1] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[7][1] = 9
                            pressionado = False
                elif posicao_click_x > 270 and posicao_click_x < 340:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[7][2] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[7][2] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[7][2] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[7][2] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[7][2] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[7][2] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[7][2] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[7][2] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[7][2] = 9
                            pressionado = False
                elif posicao_click_x > 340 and posicao_click_x < 410:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[7][3] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[7][3] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[7][3] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[7][3] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[7][3] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[7][3] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[7][3] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[7][3] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[7][3] = 9
                            pressionado = False
                elif posicao_click_x > 410 and posicao_click_x < 480:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[7][4] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[7][4] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[7][4] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[7][4] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[7][4] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[7][4] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[7][4] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[7][4] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[7][4] = 9
                            pressionado = False
                elif posicao_click_x > 480 and posicao_click_x < 550:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[7][5] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[7][5] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[7][5] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[7][5] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[7][5] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[7][5] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[7][5] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[7][5] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[7][5] = 9
                            pressionado = False
                elif posicao_click_x > 550 and posicao_click_x < 620:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[7][6] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[7][6] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[7][6] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[7][6] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[7][6] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[7][6] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[7][6] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[7][6] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[7][6] = 9
                            pressionado = False
                elif posicao_click_x > 620 and posicao_click_x < 690:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[7][7] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[7][7] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[7][7] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[7][7] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[7][7] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[7][7] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[7][7] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[7][7] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[7][7] = 9
                            pressionado = False
                elif posicao_click_x > 690 and posicao_click_x < 760:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[7][8] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[7][8] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[7][8] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[7][8] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[7][8] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[7][8] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[7][8] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[7][8] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[7][8] = 9
                            pressionado = False
            elif posicao_click_y > 770 and posicao_click_y < 840:

                if posicao_click_x > 140 and posicao_click_x < 210:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[8][0] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[8][0] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[8][0] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[8][0] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[8][0] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[8][0] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[8][0] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[8][0] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[8][0] = 9
                            pressionado = False
                elif posicao_click_x > 210 and posicao_click_x < 270:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[8][1] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[8][1] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[8][1] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[8][1] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[8][1] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[8][1] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[8][1] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[8][1] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[8][1] = 9
                            pressionado = False
                elif posicao_click_x > 270 and posicao_click_x < 340:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[8][2] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[8][2] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[8][2] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[8][2] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[8][2] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[8][2] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[8][2] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[8][2] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[8][2] = 9
                            pressionado = False
                elif posicao_click_x > 340 and posicao_click_x < 410:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[8][3] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[8][3] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[8][3] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[8][3] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[8][3] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[8][3] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[8][3] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[8][3] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[8][3] = 9
                            pressionado = False
                elif posicao_click_x > 410 and posicao_click_x < 480:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[8][4] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[8][4] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[8][4] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[8][4] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[8][4] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[8][4] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[8][4] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[8][4] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[8][4] = 9
                            pressionado = False
                elif posicao_click_x > 480 and posicao_click_x < 550:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[8][5] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[8][5] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[8][5] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[8][5] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[8][5] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[8][5] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[8][5] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[8][5] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[8][5] = 9
                            pressionado = False
                elif posicao_click_x > 550 and posicao_click_x < 620:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[8][6] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[8][6] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[8][6] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[8][6] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[8][6] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[8][6] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[8][6] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[8][6] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[8][6] = 9
                            pressionado = False
                elif posicao_click_x > 620 and posicao_click_x < 690:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[8][7] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[8][7] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[8][7] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[8][7] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[8][7] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[8][7] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[8][7] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[8][7] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[8][7] = 9
                            pressionado = False
                elif posicao_click_x > 690 and posicao_click_x < 760:
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1:
                            Matrizes.Sudoku_playground[8][8] = 1
                            pressionado = False
                        elif events.key == pygame.K_2:
                            Matrizes.Sudoku_playground[8][8] = 2
                            pressionado = False
                        elif events.key == pygame.K_3:
                            Matrizes.Sudoku_playground[8][8] = 3
                            pressionado = False
                        elif events.key == pygame.K_4:
                            Matrizes.Sudoku_playground[8][8] = 4
                            pressionado = False
                        elif events.key == pygame.K_5:
                            Matrizes.Sudoku_playground[8][8] = 5
                            pressionado = False
                        elif events.key == pygame.K_6:
                            Matrizes.Sudoku_playground[8][8] = 6
                            pressionado = False
                        elif events.key == pygame.K_7:
                            Matrizes.Sudoku_playground[8][8] = 7
                            pressionado = False
                        elif events.key == pygame.K_8:
                            Matrizes.Sudoku_playground[8][8] = 8
                            pressionado = False
                        elif events.key == pygame.K_9:
                            Matrizes.Sudoku_playground[8][8] = 9
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
