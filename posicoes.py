pressionado = False

def teclas():
    if pressionado:
        if (posicao_click_x > 140 and posicao_click_y > 230) and (posicao_click_x < 210 and posicao_click_y < 300):
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_1:
                    Matrizes.Sudoku_playground[0][0] = 1
                    pressionado = False
        if (posicao_click_x > 210 and posicao_click_y > 230) and (posicao_click_x < 270 and posicao_click_y < 300):
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_1:
                    Matrizes.Sudoku_playground[0][1] = 1
                    pressionado = False
        if (posicao_click_x > 270 and posicao_click_y > 230) and (posicao_click_x < 340 and posicao_click_y < 300):
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_1:
                    Matrizes.Sudoku_playground[0][2] = 1
                    pressionado = False
        if (posicao_click_x > 340 and posicao_click_y > 230) and (posicao_click_x < 410 and posicao_click_y < 300):
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_1:
                    Matrizes.Sudoku_playground[0][3] = 1
                    pressionado = False
        if (posicao_click_x > 410 and posicao_click_y > 230) and (posicao_click_x < 480 and posicao_click_y < 300):
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_1:
                    Matrizes.Sudoku_playground[0][4] = 1
                    pressionado = False
        if (posicao_click_x > 480 and posicao_click_y > 230) and (posicao_click_x < 550 and posicao_click_y < 300):
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_1:
                    Matrizes.Sudoku_playground[0][5] = 1
                    pressionado = False
        if (posicao_click_x > 620 and posicao_click_y > 230) and (posicao_click_x < 680 and posicao_click_y < 300):
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_1:
                    Matrizes.Sudoku_playground[0][6] = 1
                    pressionado = False
        if (posicao_click_x > 680 and posicao_click_y > 230) and (posicao_click_x < 750 and posicao_click_y < 300):
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_1:
                    Matrizes.Sudoku_playground[0][7] = 1
                    pressionado = False
        if (posicao_click_x > 750 and posicao_click_y > 230) and (posicao_click_x < 820 and posicao_click_y < 300):
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_1:
                    Matrizes.Sudoku_playground[0][8] = 1
                    pressionado = False


