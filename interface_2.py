import pygame
import sys
import logica_total as jogo  # Certifique-se de que este arquivo está no mesmo diretório

pygame.init()

# Configurações de tela e fonte
largura, altura = 1280, 680
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Contagem Frenética")

fonte_grande = pygame.font.SysFont(None, 120)
fonte_media = pygame.font.SysFont(None, 60)
fonte_pequena = pygame.font.SysFont(None, 40)

# Cores
ROXO = (128, 0, 128)
VERDE = (0, 255, 0)
VIOLETA = (238, 130, 238)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Botões
botao_facil = pygame.Rect(largura//2 - 150, 200, 300, 60)
botao_medio = pygame.Rect(largura//2 - 150, 300, 300, 60)
botao_dificil = pygame.Rect(largura//2 - 150, 400, 300, 60)

def mostrar_tela_inicial():
    tela.fill(ROXO)
    titulo = fonte_grande.render("CONTAGEM FRENÉTICA", True, BRANCO)
    subtitulo = fonte_pequena.render("CONTADOR INTERATIVO DE FORMAS GEOMÉTRICAS", True, BRANCO)
    subtitulo2 = fonte_media.render("APERTE QUALQUER TECLA PARA CONTINUAR", True, BRANCO)
    seta = fonte_grande.render("➭", True, VIOLETA)

    tela.blit(titulo, (largura//2 - titulo.get_width()//2, altura//5))
    tela.blit(subtitulo, (largura//2 - subtitulo.get_width()//2, altura//4 + 50))
    tela.blit(subtitulo2, (largura//2 - subtitulo2.get_width()//2, altura//2 + 10))
    tela.blit(seta, (largura//2 - seta.get_width()//2, altura//2 + 100))

def mostrar_tela_menu():
    tela.fill(VERDE)
    pygame.draw.rect(tela, VIOLETA, botao_facil)
    pygame.draw.rect(tela, VIOLETA, botao_medio)
    pygame.draw.rect(tela, VIOLETA, botao_dificil)

    facil = fonte_media.render("FÁCIL", True, PRETO)
    medio = fonte_media.render("MÉDIO", True, PRETO)
    dificil = fonte_media.render("DIFÍCIL", True, PRETO)

    tela.blit(facil, (botao_facil.centerx - facil.get_width()//2, botao_facil.centery - facil.get_height()//2))
    tela.blit(medio, (botao_medio.centerx - medio.get_width()//2, botao_medio.centery - medio.get_height()//2))
    tela.blit(dificil, (botao_dificil.centerx - dificil.get_width()//2, botao_dificil.centery - dificil.get_height()//2))

def main():
    tela_atual = "inicio"
    executando = True

    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
                break

            if tela_atual == "inicio" and evento.type == pygame.KEYDOWN:
                tela_atual = "menu"

            elif tela_atual == "menu" and evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_facil.collidepoint(evento.pos):
                    resultado = jogo.executar_jogo("facil")
                    if resultado == "voltar_inicio":
                        tela_atual = "inicio"

                elif botao_medio.collidepoint(evento.pos):
                    resultado = jogo.executar_jogo("medio")
                    if resultado == "voltar_inicio":
                        tela_atual = "inicio"

                elif botao_dificil.collidepoint(evento.pos):
                    resultado = jogo.executar_jogo("dificil")
                    if resultado == "voltar_inicio":
                        tela_atual = "inicio"

        # Exibir tela apropriada
        if tela_atual == "inicio":
            mostrar_tela_inicial()
        elif tela_atual == "menu":
            mostrar_tela_menu()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

main()
