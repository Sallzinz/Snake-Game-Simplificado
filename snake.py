import pygame
import random

pygame.init()

#Resolução da Janela. 
#Pode mudar se quiser, só deixa simetrico por favor.
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

#Posição Inicial do Jogador
x = 300
y = 200

tamanho = 20
velocidade = tamanho #Isso vai criar movimento em grid

#Direção Incial
direcao_x = 0
direcao_y = 0

cobra = [(x, y)]

#É a comida da "cobra", isso faz ela crescer, blz?
comida_x = random.randrange(0, largura - tamanho, tamanho)
comida_y = random.randrange(0, altura - tamanho, tamanho)

fonte = pygame.font.SysFont(None, 48) #Fonte do Game Over

rodando = True
game_over = False  # Pelo amor de Deus, não coloca isso no Loop!

while rodando:
    clock.tick(5)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        #Reiniciar quando morrer
        if game_over and evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            x, y = 300, 200
            direcao_x = 0
            direcao_y = 0
            cobra = [(x, y)]
            comida_x = random.randrange(0, largura - tamanho, tamanho)
            comida_y = random.randrange(0, altura - tamanho, tamanho)
            game_over = False

        #Moviemento baseado em Keybinds
        if not game_over and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d and direcao_x == 0:
                direcao_x = velocidade
                direcao_y = 0
            if evento.key == pygame.K_a and direcao_x == 0:
                direcao_x = -velocidade
                direcao_y = 0
            if evento.key == pygame.K_s and direcao_y == 0:
                direcao_x = 0
                direcao_y = velocidade
            if evento.key == pygame.K_w and direcao_y == 0:
                direcao_x = 0
                direcao_y = -velocidade

    #Só anda se tiver direção
    if not game_over and (direcao_x != 0 or direcao_y != 0):
        x += direcao_x
        y += direcao_y  

        cabeca = (x, y)
        cobra.append(cabeca)

        #morte ao se bater
        if cabeca in cobra[:-1]:
            game_over = True

        #Se não papar, sem cauda!
        if (x, y) != (comida_x, comida_y):
            cobra.pop(0)
        else:
            comida_x = random.randrange(0, largura - tamanho, tamanho)
            comida_y = random.randrange(0, altura - tamanho, tamanho)

        #Morte por sair da tela
        if x < 0 or x >= largura or y < 0 or y >= altura:
            game_over = True

    #Background
    tela.fill((0, 0, 0))

    #Desenho da Cobra
    for parte in cobra:
        pygame.draw.rect(tela, (0, 255, 0), (parte[0], parte[1], tamanho, tamanho))

    #Desenho da comida
    pygame.draw.rect(tela, (255, 0, 0), (comida_x, comida_y, tamanho, tamanho))

    #Tela de Game Over
    if game_over:
        texto1 = fonte.render("FIM DE JOGO", True, (255, 0, 0))
        texto2 = fonte.render("Pressione ESPAÇO para reiniciar", True, (255, 255, 255))

        tela.blit(texto1, (largura//2 - texto1.get_width()//2, altura//2 - 40))
        tela.blit(texto2, (largura//2 - texto2.get_width()//2, altura//2 + 10))

    pygame.display.update()

pygame.quit()
