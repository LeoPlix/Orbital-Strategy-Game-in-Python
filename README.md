Este projeto implementa o jogo Órbito, um jogo de estratégia baseado na colocação e rotação de peças num tabuleiro quadrado composto por órbitas concêntricas. O jogo pode ser jogado entre dois jogadores ou entre um jogador e o computador, que dispõe de diferentes níveis de dificuldade.

Funcionalidades Principais

Tabuleiro configurável entre 2 e 5 órbitas (dimensão entre 4×4 e 10×10)

Três tipos de pedra:

Pedra preta (1)

Pedra branca (-1)

Pedra neutra (0)

Rotação automática do tabuleiro no sentido anti-horário após cada jogada

Deteção automática de linhas vencedoras horizontais, verticais e diagonais

Sistema de adjacências, tanto ortogonais como diagonais

Modos de jogo disponíveis: singleplayer e multiplayer

Inteligência artificial com níveis fácil e normal

Estrutura do Projeto

O projeto está totalmente contido no ficheiro:

FP2425P2.py 

FP2425P2

Nele encontram-se os TADs (Posição, Pedra e Tabuleiro), as funções de jogo e a implementação da IA.

TADs Implementados
1. TAD Posição

Representa coordenadas do tabuleiro como tuplos (coluna, linha)

Contém funções de construção, validação, conversão e comparação

Permite obter adjacentes ortogonais ou completos (8 direções)

2. TAD Pedra

Representação das pedras do jogo como inteiros

Funções para criação, teste, comparação e conversão para caracteres (X, O ou espaço)

3. TAD Tabuleiro

Geração de tabuleiros vazios ou preenchidos

Seletores de linhas horizontais, verticais e diagonais

Obtenção de posições com determinada pedra

Colocação e remoção de pedras

Rotação do tabuleiro

Deteção de linhas consecutivas e condições de fim do jogo

Mecânica do Jogo

O jogador (ou a IA) escolhe uma posição livre.

A pedra é colocada no tabuleiro.

O tabuleiro roda no sentido anti-horário.

Verifica-se se existe um vencedor ou se o tabuleiro está cheio.

Um jogador vence se formar uma linha de tamanho igual ao lado do tabuleiro (n×2).

Inteligência Artificial
Nível Fácil

Tenta jogar numa posição que, após a rotação, fique adjacente a uma pedra sua.

Se isso não for possível, joga na primeira posição livre segundo a ordem definida.

Nível Normal

Tenta vencer no próprio turno simulando a jogada e a rotação.

Se não for possível, tenta bloquear uma vitória iminente do adversário.

Usa simulação de jogadas futuras para determinar a melhor posição.

Modos de Jogo
Singleplayer

O jogador escolhe se joga com X ou O.

O computador joga com dificuldade definida.

O jogo alterna entre jogadas humanas e automáticas, com rotação sempre no fim do turno.

Multiplayer

Dois jogadores humanos alternam turnos.

As regras e a rotação mantêm-se exatamente iguais ao singleplayer.

Execução
python FP2425P2.py


O programa solicitará:

Número de órbitas

Modo de jogo (fácil, normal ou dois jogadores)

Pedra inicial do jogador (X ou O)
