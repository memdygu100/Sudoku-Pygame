import random

numeros_removidos = 5

posicoes_x = [150, 215, 285, 350, 420, 485, 555, 620, 690]
posicoes_y = [240, 305, 375, 440, 510, 575, 645, 710, 780]
colunas = []

Sudoku_playground = [[0 for _ in range(9)] for _ in range(9)]

def numero_valido(linha, coluna, numero):

    for i in range(9):
        if Sudoku_playground[linha][i] == numero or Sudoku_playground[i][coluna] == numero:
            return False


    inicio_linha = 3 * (linha // 3)
    inicio_coluna = 3 * (coluna // 3)
    for i in range(3):
        for j in range(3):
            if Sudoku_playground[inicio_linha + i][inicio_coluna + j] == numero:
                return False

    return True

def preencher_tabuleiro():
    for linha in range(9):
        for coluna in range(9):
            if Sudoku_playground[linha][coluna] == 0:
                numeros = list(range(1, 10))
                random.shuffle(numeros)
                for numero in numeros:
                    if numero_valido(linha, coluna, numero):
                        Sudoku_playground[linha][coluna] = numero
                        if preencher_tabuleiro():
                            return True
                        Sudoku_playground[linha][coluna] = 0
                return False
    return True

preencher_tabuleiro()



for quad_linha in range(0, 9, 3):
    for quad_coluna in range(0, 9, 3):

        posicoes = [(i, j) for i in range(quad_linha, quad_linha + 3)
                           for j in range(quad_coluna, quad_coluna + 3)]
        random.shuffle(posicoes)

        for i, j in posicoes[:numeros_removidos]:
            Sudoku_playground[i][j] = 0

#FIM DA CRIAÇÃO DO SUDOKU

numeros_bloqueados = [["." for _ in range(9)] for _ in range(9)]
for a in range(len(numeros_bloqueados)):
    for b in range(len(numeros_bloqueados)):
        if Sudoku_playground[a][b] != 0:
            numeros_bloqueados[a][b] = Sudoku_playground[a][b]

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



