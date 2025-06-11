Contagem_Frenetica_Jogo_TEA
🎮 Contagem Frenética

Contagem Frenética é um jogo sério interativo desenvolvido como projeto acadêmico para auxiliar no desenvolvimento de habilidades cognitivas, perceptivas e motoras de crianças com Transtorno do Espectro Autista (TEA).  

O jogo consiste em contar corretamente formas geométricas de diferentes cores e tamanhos dentro de um tempo limite, utilizando teclado ou botões físicos conectados a um Arduino.

Objetivo

Estimular:
- Percepção visual (formas e cores);
- Atenção seletiva e foco;
- Coordenação motora e tempo de resposta;
- Capacidade de contagem e correção.

💡 Como Funciona

O jogador vê formas geométricas aleatórias (círculos e quadrados, vermelhos e azuis), deve contá-las e informar a quantidade usando teclas ou botões físicos. Ao fim do tempo ou ao pressionar o botão de confirmar, o jogo avalia a resposta e fornece feedback imediato (não punitivo).

🕹️ Controles

Via teclado:
- `Q` / `A`: Adiciona/subtrai círculo vermelho  
- `W` / `S`: Adiciona/subtrai círculo azul  
- `E` / `D`: Adiciona/subtrai quadrado vermelho  
- `R` / `F`: Adiciona/subtrai quadrado azul  
- `ESPACO`: Confirmar contagem

Via hardware (Arduino):
- Botões físicos mapeados com os mesmos comandos acima, conectados por comunicação serial.

📂 Estrutura do Projeto

- `interface_2.py` — Interface inicial e menu do jogo  
- `logica_total.py` — Lógica principal de geração de formas e verificação  
- `contagem_frenetica2.ino` — Código Arduino para envio de comandos via botões físicos 
