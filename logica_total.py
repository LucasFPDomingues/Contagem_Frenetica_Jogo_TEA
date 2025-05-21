
import pygame
import time
import random
import math

pygame.init()
tela = pygame.display.set_mode((1280, 680))
pygame.display.set_caption("Jogo TEA - Versão Teclado")
fonte = pygame.font.SysFont(None, 36)

VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

fase_facil = {
    'circulos_vermelhos': random.randint(5, 8),
    'circulos_azuis': random.randint(5, 8),
    'quadrados_vermelhos': random.randint(5, 8),
    'quadrados_azuis': random.randint(5, 8),
    'tempo_limite': 30
}

fase_medio = {
    'circulos_vermelhos': random.randint(8, 11),
    'circulos_azuis': random.randint(8, 11),
    'quadrados_vermelhos': random.randint(8, 11),
    'quadrados_azuis': random.randint(8, 11),
    'tempo_limite': 45
}

fase_dificil = {
    'circulos_vermelhos': random.randint(11, 13),
    'circulos_azuis': random.randint(11, 13),
    'quadrados_vermelhos': random.randint(11, 13),
    'quadrados_azuis': random.randint(11, 13),
    'tempo_limite': 60
}

def nivel_fase(dificuldade):
    if dificuldade == "facil":
        return fase_facil
    elif dificuldade == "medio":
        return fase_medio
    elif dificuldade == "dificil":
        return fase_dificil

contadores = {
    'circulos_vermelhos': 0,
    'circulos_azuis': 0,
    'quadrados_vermelhos': 0,
    'quadrados_azuis': 0
}

formas = []
formato_tamanho = 40
nivel = {}

def formas_sobrepostas(x, y, lista):
    for forma in lista:
        distancia = math.hypot(x - forma['x'], y - forma['y'])
        if distancia < formato_tamanho + 10:
            return True
    return False

def gerar_formas():
    tipos = [
        ('circulo', VERMELHO, nivel['circulos_vermelhos'], 'circulos_vermelhos'),
        ('circulo', AZUL, nivel['circulos_azuis'], 'circulos_azuis'),
        ('quadrado', VERMELHO, nivel['quadrados_vermelhos'], 'quadrados_vermelhos'),
        ('quadrado', AZUL, nivel['quadrados_azuis'], 'quadrados_azuis')
    ]

    for tipo, cor, quantidade, chave in tipos:
        for _ in range(quantidade):
            while True:
                x = random.randint(30, 1250)
                y = random.randint(30, 650)
                if not formas_sobrepostas(x, y, formas):
                    formas.append({
                        'tipo': tipo,
                        'cor': cor,
                        'x': x,
                        'y': y,
                        'chave': chave
                    })
                    break

def desenhar_figuras():
    tela.fill(BRANCO)
    for forma in formas:
        if forma['tipo'] == 'circulo':
            pygame.draw.circle(tela, forma['cor'], (forma['x'], forma['y']), formato_tamanho // 2)
        elif forma['tipo'] == 'quadrado':
            pygame.draw.rect(tela, forma['cor'], pygame.Rect(forma['x'], forma['y'], formato_tamanho, formato_tamanho))

def desenhar_rodape(tempo_restante):
    y_base = 590
    textos = [
        f"Círculos Vermelhos: {contadores['circulos_vermelhos']}",
        f"Círculos Azuis: {contadores['circulos_azuis']}",
        f"Quadrados Vermelhos: {contadores['quadrados_vermelhos']}",
        f"Quadrados Azuis: {contadores['quadrados_azuis']}",
        f"Tempo Restante: {tempo_restante} segundos"
    ]
    for i, texto in enumerate(textos):
        t = fonte.render(texto, True, PRETO)
        tela.blit(t, (20, y_base + i * 15))

def verificar_resposta():
    mensagens = []
    tudo_certo = True
    for chave in contadores:
        esperado = nivel[chave]
        informado = contadores[chave]
        if informado != esperado:
            tudo_certo = False
            mensagens.append(f"{chave.replace('_', ' ').capitalize()}: Quantidade correta: {esperado}, Contagem: {informado}")
        else:
            mensagens.append(f"{chave.replace('_', ' ').capitalize()}: Correto: ({esperado})")
    mensagens.insert(0, "ACERTOU!" if tudo_certo else "ERROU!")
    return mensagens

def executar_jogo(dificuldade):
    global nivel
    nivel = nivel_fase(dificuldade)
    gerar_formas()
    desenhar_figuras()
    inicio = time.time()
    executando = True

    while executando:
        tempo_passado = time.time() - inicio
        tempo_restante = max(0, int(nivel['tempo_limite'] - tempo_passado))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:
                    contadores['circulos_vermelhos'] += 1
                if evento.key == pygame.K_a:
                    if contadores['circulos_vermelhos'] > 0:
                        contadores['circulos_vermelhos'] -= 1
                if evento.key == pygame.K_w:
                    contadores['circulos_azuis'] += 1
                if evento.key == pygame.K_s:
                    if contadores['circulos_azuis'] > 0:
                        contadores['circulos_azuis'] -= 1
                if evento.key == pygame.K_e:
                    contadores['quadrados_vermelhos'] += 1
                if evento.key == pygame.K_d:
                    if contadores['quadrados_vermelhos'] > 0:
                        contadores['quadrados_vermelhos'] -= 1
                if evento.key == pygame.K_r:
                    contadores['quadrados_azuis'] += 1
                if evento.key == pygame.K_f:
                    if contadores['quadrados_azuis'] > 0:
                        contadores['quadrados_azuis'] -= 1
                if evento.key == pygame.K_SPACE:
                    resultados = verificar_resposta()
                    tela.fill(BRANCO)
                    for i, linha in enumerate(resultados):
                        msg = fonte.render(linha, True, PRETO)
                        tela.blit(msg, (100, 250 + i * 30))
                    pygame.display.flip()
                    time.sleep(10)
                    return "voltar_inicio"

        if tempo_passado > nivel['tempo_limite']:
            resultados = verificar_resposta()
            tela.fill(BRANCO)
            msg_tempo = fonte.render("TEMPO ESGOTADO!", True, (200, 0, 0))
            tela.blit(msg_tempo, (100, 220))
            for i, linha in enumerate(resultados):
                msg = fonte.render(linha, True, PRETO)
                tela.blit(msg, (100, 260 + i * 30))
            pygame.display.flip()
            time.sleep(10)
            return "voltar_inicio"

        desenhar_figuras()
        desenhar_rodape(tempo_restante)
        pygame.display.flip()
