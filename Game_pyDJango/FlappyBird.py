# Importando bibliotecas necessárias #

import pygame
import os
import random

# Configurações iniciais #
TELA_LARGURA = 500

TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(
    pygame.image.load(os.path.join("pipe.png")))

IMAGEM_CHAO = pygame.transform.scale2x(
    pygame.image.load(os.path.join("base.png")))

IMAGEM_BACKGROUD = pygame.transform.scale2x(
    pygame.image.load(os.path.join("bg.png")))

IMAGENS_PASSARO = [pygame.transform.scale2x(
    pygame.image.load(os.path.join("bird1.png"))),
    pygame.transform.scale2x(
    pygame.image.load(os.path.join("bird2.png"))),
    pygame.transform.scale2x(
    pygame.image.load(os.path.join("bird3.png")))]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)
