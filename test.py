# coding: utf-8
from graphics import *
from variaveis import *
import time, math, unittest, pygame


# Movendo as funções para fora do loop principal para testá-las
def mover_esquerda(x_cabeca):
    return x_cabeca - vel

def mover_direita(x_cabeca):
    return x_cabeca + vel

def checar_colisao_bola_parede(x_bola, raio, velx_bola):
    if x_bola + raio > x:
        if velx_bola > 0:
            velx_bola = (velx_bola * -1) * 0.7
    if x_bola - raio < 0:
        if velx_bola < 0:
            velx_bola = (velx_bola * -1) * 0.7
    return velx_bola

def checar_colisao_bola_teto(y_bola, raio, vely_bola):
    if y_bola - raio < 0:
        if vely_bola < 0:
            vely_bola = (vely_bola * -1) * 0.7
    return vely_bola


#### TESTES UNITÁRIOS ####

class TesteMovimentacao(unittest.TestCase):
    # Define os valores para as variáveis globais usadas nos testes
    global x, raio_cabeca, vel, x1_trave2, x2_trave1, raio, y1_trave, col_trave1, col_trave2

    x = 1200  # Largura da tela
    raio_cabeca = 30  # Raio da cabeça do jogador
    vel = 5  # Velocidade de movimento do jogador
    raio = 22 #Raio da bola

    # Posições das traves
    x1_trave2 = 1100 # Trave direita
    x2_trave1 = 100 # Trave esquerda
    y1_trave = 420

    # Criando objetos para teste de colisão com a trave
    col_trave1 = Circle(Point(105, 360), 5)
    col_trave2 = Circle(Point(x - 105, 360), 5)

    def teste_mover_esquerda(self):
        # Testa se o jogador se move para a esquerda corretamente
        self.assertEqual(mover_esquerda(300), 295)

    def teste_mover_direita(self):
        # Testa se o jogador se move para a direita corretamente
        self.assertEqual(mover_direita(300), 305)

    def teste_colisao_bola_parede_direita(self):
        # Testa se a colisão da bola com a parede direita funciona
        velocidade_x = 5
        velocidade_x = checar_colisao_bola_parede(1180, raio, velocidade_x)
        self.assertLess(velocidade_x, 0)  # A velocidade em x deve ser negativa após a colisão

    def teste_colisao_bola_parede_esquerda(self):
        # Testa se a colisão da bola com a parede esquerda funciona
        velocidade_x = -5
        velocidade_x = checar_colisao_bola_parede(20, raio, velocidade_x)
        self.assertGreater(velocidade_x, 0)  # A velocidade em x deve ser positiva após a colisão

    def teste_colisao_bola_teto(self):
        # Testa se a colisão da bola com o teto funciona
        velocidade_y = -5
        velocidade_y = checar_colisao_bola_teto(20, raio, velocidade_y)
        self.assertGreater(velocidade_y, 0)  # A velocidade em y deve ser positiva após a colisão
    


if __name__ == "__main__":
    unittest.main()