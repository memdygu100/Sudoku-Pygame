Sudoku_playground = [[5, 3, '', '', 7, '', '', '', ''],
                     [6, '', '', 1, 9, 5, '', '', ''],
                     ['', 9, 8, '', '', '', '', 6, ''],
                     [8, '', '', '', 6, '', '', '', 3],
                     [4, '', '', 8, '', 3, '', '', 1],
                     [7, '', '', '', 2, '', '', '', 6],
                     ['', 6, '', '', '', '', 2, 8, ''],
                     ['', '', '', 4, 1, 9, '', '', 5],
                     ['', '', '', '', 8, '', '', 7, 9]]

posicoes_x = [150, 215, 285, 350, 420, 485, 555, 620, 690]
posicoes_y = [240, 305, 375, 440, 510, 575, 645, 710, 780]
colunas = []

def verifica_submatriz_unica(submatriz):
    numeros = [num for linha in submatriz for num in linha if num != 0]
    return len(numeros) == len(set(numeros))

def verificacao():
    submatrizes = []

    for bloco_linha in range(3):
        for bloco_coluna in range(3):
            submatriz = []
            for i in range(3):
                linha = []
                for j in range(3):
                    linha.append(Sudoku_playground[bloco_linha * 3 + i][bloco_coluna * 3 + j])
                submatriz.append(linha)
            submatrizes.append(submatriz)

    todas_validas = all(verifica_submatriz_unica(sub) for sub in submatrizes)

    for i in range(len(Sudoku_playground)):
        colunas = []
        for j in range(len(Sudoku_playground)):
            if Sudoku_playground[i].count(Sudoku_playground[i][j]) != 1:
                return False
            colunas.append(Sudoku_playground[j][i])
        for k in range(len(Sudoku_playground)):
            if colunas.count(Sudoku_playground[k][i]) != 1:
                return False
    if not todas_validas:
        return False
    return True


