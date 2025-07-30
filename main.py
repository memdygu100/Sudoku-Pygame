from idlelib.mainmenu import menudefs
from site import abs_paths

import pygame
import Matrizes
import time
import random
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Sudoku')
tempo_inicial = time.time()
tempo_decorrido = 0

x, y = 850, 850
janela = pygame.display.set_mode([x, y])

largura_janela_vitoria = 400
altura_janela_vitoria = 200
posicao_x = (x - largura_janela_vitoria) // 2
posicao_y = (y - altura_janela_vitoria) // 2


text_color = (0, 0, 0)
font = pygame.font.Font("Fonts/PressStart2P-Regular.ttf", 25)
text = "Este número não pode ser alterado"
text_surface = font.render(text, True, text_color)
text_rect = text_surface.get_rect()
text_rect.center = (434, 200)

text_2 = 'Resposta Incorreta'
text_2_surface = font.render(text_2, True, text_color)
text_2_rect = text_2_surface.get_rect()
text_2_rect.center = (465, 200)

text_vitoria_color = (0, 0, 0)
font_text_vitoria = pygame.font.Font("Fonts/PressStart2P-Regular.ttf", 25)
linha1 = "Parabéns,"
linha2 = "você completou o sudoku em:"
surface_linha1 = font_text_vitoria.render(linha1, True, text_vitoria_color)
surface_linha2 = font_text_vitoria.render(linha2, True, text_vitoria_color)
rect_linha1 = surface_linha1.get_rect(center=(posicao_x + 220, posicao_y + 20))
rect_linha2 = surface_linha2.get_rect(center=(posicao_x + 220, posicao_y + 60))

text_time_font = pygame.font.SysFont("Fonts/PressStart2P-Regular.ttf", 80)

text_facil_color = (4, 143, 27)
text_facil = "FÁCIL"
font_text_facil = pygame.font.Font("Fonts/PressStart2P-Regular.ttf", 35)
text_facil_surface = font_text_facil.render(text_facil, True, text_facil_color)
text_facil_rect = text_facil_surface.get_rect()
text_facil_rect.center = (425, 440)

text_medio_color = (245, 150, 27)
text_medio = "MÉDIO"
text_medio_surface = font_text_facil.render(text_medio, True, text_medio_color)
text_medio_rect = text_medio_surface.get_rect()
text_medio_rect.center = (425, 540)

text_dificil_color = (217, 13, 13)
text_dificil = "DIFÍCL"
text_dificil_surface = font_text_facil.render(text_dificil, True, text_dificil_color)
text_dificil_rect = text_dificil_surface.get_rect()
text_dificil_rect.center = (425, 640)

text_boas_vindas_1 = "Selecione a dificuldade"
text_boas_vindas_2 = "do SUDOKU:"
font_text_boas_vindas = pygame.font.Font("Fonts/PressStart2P-Regular.ttf", 23)
text_boas_vindas_color = (0, 0, 0)
text_boas_vindas_1_surface = font_text_boas_vindas.render(text_boas_vindas_1, True, text_boas_vindas_color)
text_boas_vindas_2_surface = font_text_boas_vindas.render(text_boas_vindas_2, True, text_boas_vindas_color)
text_boas_vindas_1_rect = text_boas_vindas_1_surface.get_rect(center=(435, 200))
text_boas_vindas_2_rect = text_boas_vindas_2_surface.get_rect(center=(435, 240))

text_derrota_1 = "Você errou suas 3 tentativas,"
text_derrota_2 = "boa sorte na próxima vez"
font_text_derrota = pygame.font.Font("Fonts/PressStart2P-Regular.ttf", 23)
text_derrota_color = (247, 5, 5)
text_derrota_1_surface = font_text_derrota.render(text_derrota_1, True, text_derrota_color)
text_derrota_2_surface = font_text_derrota.render(text_derrota_2, True, text_derrota_color)
text_derrota_1_rect = text_derrota_1_surface.get_rect(center=(posicao_x + 220, posicao_y + 20))
text_derrota_2_rect = text_derrota_2_surface.get_rect(center=(posicao_x + 220, posicao_y + 60))

som_click = pygame.mixer.Sound("Sounds/AUDIODECLICK.mp3")
som_vitoria = pygame.mixer.Sound("Sounds/AUDIOVITORIA.mp3")
som_erro = pygame.mixer.Sound("Sounds/SOMERRADO.mp3")
som_derrota = pygame.mixer.Sound("Sounds/TUQUERISSOMESMO.mp3")

numeros_removidos = 0

pos_x_player = 430
pos_y_player = 400
vel_nave_player = 10

sudoku_correto = None

pressionado = False

precisa_redesenhar = False

linha_selecionada = None
coluna_selecionada = None

jogo_finalizado = False

jogo_rodando = False

apagar_matriz = False

var_aux = 10

vidas = 3
def desenhar_vidas_sprite(janela, vidas, coracao):
    for i in range(vidas):
        janela.blit(coracao, (20 + i * 40, 20))

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
janela_fundo_vitoria = pygame.image.load("Assets/Janela Fundo Vitoria.jpg")
janela_fundo_vitoria = pygame.transform.scale(janela_fundo_vitoria, (750, 200))
botao_fundo_menu = pygame.image.load("Assets/Janela Fundo Vitoria.jpg")
botao_fundo_menu = pygame.transform.scale(janela_fundo_vitoria, (300, 75))
quadrado_menu = pygame.image.load("Assets/Janela Fundo Vitoria.jpg")
quadrado_menu = pygame.transform.scale(janela_fundo_vitoria, (600, 150))
quadrado_selecao = pygame.image.load("Assets/New Piskel (1).png")
quadrado_selecao = pygame.transform.scale(quadrado_selecao, (72, 72))
coracao = pygame.image.load("Assets/Coração.png").convert_alpha()
coracao = pygame.transform.scale(coracao, (40, 40))




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

numeros_bloqueados = [["." for _ in range(9)] for _ in range(9)]
def remocao_numeros():
    for quad_linha in range(0, 9, 3):
        for quad_coluna in range(0, 9, 3):

            posicoes = [(i, j) for i in range(quad_linha, quad_linha + 3)
                               for j in range(quad_coluna, quad_coluna + 3)]
            random.shuffle(posicoes)

            for i, j in posicoes[:numeros_removidos]:
                Sudoku_playground[i][j] = 0

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



loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if jogo_rodando:
            if apagar_matriz is True:
                remocao_numeros()
                apagar_matriz = False
            if not(jogo_finalizado):
                if events.type == pygame.MOUSEBUTTONDOWN:
                    som_click.play()
                    posicao_click_x, posicao_click_y = pygame.mouse.get_pos()
                    if 140 < posicao_click_x < 760 and 230 < posicao_click_y < 840:
                        coluna_selecionada = (posicao_click_x - 140) // 70
                        linha_selecionada = (posicao_click_y - 230) // 70
                        print(f"Célula clicada: [{linha_selecionada}][{coluna_selecionada}]")
                        precisa_redesenhar = True
                        pressionado = True
                elif events.type == pygame.KEYDOWN:
                    if linha_selecionada is not None and coluna_selecionada is not None:
                        if Sudoku_playground[linha_selecionada][coluna_selecionada] != numeros_bloqueados[linha_selecionada][coluna_selecionada]:
                            if pygame.K_1 <= events.key <= pygame.K_9:
                                valor = events.key - pygame.K_0
                                Sudoku_playground[linha_selecionada][coluna_selecionada] = valor
                                precisa_redesenhar = True
                            elif events.key == pygame.K_0:
                                Sudoku_playground[linha_selecionada][coluna_selecionada] = 0
                                precisa_redesenhar = True
                    if events.key == pygame.K_RETURN:
                        if verificacao():
                            print("Sudoku Resolvido")
                            sudoku_correto = True
                        else:
                            som_erro.play()
                            print("Sudoku Incompleto")
                            sudoku_correto = False
                            vidas -= 1
                            print(vidas)
                        precisa_redesenhar = True

            tempo_atual = time.time()
            tempo_decorrido = int(tempo_atual - tempo_inicial)
            minutos = tempo_decorrido // 60
            segundos = tempo_decorrido % 60

            teclas = pygame.key.get_pressed()



            janela.blit(imagem_fundo, (0, 0))
            desenhar_vidas_sprite(janela, vidas, coracao)

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
                for i, linha in enumerate(Sudoku_playground):
                    for j, valor in enumerate(linha):
                        if valor in numero_imagens:
                            janela.blit(numero_imagens[valor], (Matrizes.posicoes_x[j], Matrizes.posicoes_y[i]))
                if Sudoku_playground[linha_selecionada][coluna_selecionada] == numeros_bloqueados[linha_selecionada][coluna_selecionada]:
                    janela.blit(text_surface, text_rect)
                elif sudoku_correto is False:
                    janela.blit(text_2_surface, text_2_rect)
                    sudoku_correto = None
                elif sudoku_correto is True:
                    som_vitoria.play()
                    janela.blit(janela_fundo_vitoria, (posicao_x - 150 , posicao_y - 25))
                    janela.blit(surface_linha1, rect_linha1)
                    janela.blit(surface_linha2, rect_linha2)
                    text_time = f"{minutos:02d}:{segundos:02d}"
                    text_time_surface = text_time_font.render(text_time, True, text_color)
                    text_time_rect = text_time_surface.get_rect()
                    text_time_rect.center = (posicao_x + 220, posicao_y + 110)
                    janela.blit(text_time_surface, text_time_rect)
                    jogo_finalizado = True
                if pressionado and Sudoku_playground[linha_selecionada][coluna_selecionada] != numeros_bloqueados[linha_selecionada][coluna_selecionada] :
                    janela.blit(quadrado_selecao, (Matrizes.posicoes_x[coluna_selecionada] - 8, Matrizes.posicoes_y[linha_selecionada] - 9))
                if vidas <= 0:
                    som_derrota.play()
                    janela.blit(janela_fundo_vitoria, (posicao_x - 150, posicao_y - 50))
                    janela.blit(text_derrota_1_surface, text_derrota_1_rect)
                    janela.blit(text_derrota_2_surface, text_derrota_2_rect)
                    jogo_finalizado = True
                pygame.display.update()
                precisa_redesenhar = False
                pressionado = False

        else:
            menu = pygame.display.set_mode((x, y))
            posicao_click_x, posicao_click_y = pygame.mouse.get_pos()
            janela.blit(botao_fundo_menu,(275, 400))
            janela.blit(botao_fundo_menu, (275, 500))
            janela.blit(botao_fundo_menu, (275, 600))
            janela.blit(quadrado_menu, (135, 150))
            janela.blit(text_facil_surface, text_facil_rect)
            janela.blit(text_medio_surface, text_medio_rect)
            janela.blit(text_dificil_surface,text_dificil_rect)
            janela.blit(text_boas_vindas_1_surface, text_boas_vindas_1_rect)
            janela.blit(text_boas_vindas_2_surface, text_boas_vindas_2_rect)
            if 280 < posicao_click_x < 570:
                if  400 < posicao_click_y < 480:
                    #facil
                    numeros_removidos = 4
                    jogo_rodando = True
                    apagar_matriz = True
                elif 500 < posicao_click_y < 570:
                    #medio
                    numeros_removidos = 5
                    jogo_rodando = True
                    apagar_matriz = True
                elif 600 < posicao_click_y < 670:
                    #dificil
                    numeros_removidos = 6
                    jogo_rodando = True
                    apagar_matriz = True
            pygame.display.update()
    clock.tick(60)

