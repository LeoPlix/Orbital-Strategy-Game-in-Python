letras_possiveis = ("a","b","c","d","e","f","g","h", "i", "j")

def cria_posicao(letra, num):
    if isinstance(letra, str) and isinstance(num, int):
        if len(letra) == 1 and letra in letras_possiveis and num in range(1,11):
            return (letra, num)
    raise ValueError('cria_posicao: argumentos invalidos')

def obtem_pos_col(posicao):
    return posicao[0]

def obtem_pos_lin(posicao):
    return posicao[1]

def eh_posicao(arg):
    return isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], str) and isinstance(arg[1], int) and arg[0] in letras_possiveis and arg[1] in range(1,11)

def posicoes_iguais(pos1, pos2):
    return pos1 == pos2

def posicao_para_str(pos):
    return pos[0] + str(pos[1])

def str_para_posicao(s):
    if isinstance(s, str) and len(s) == 2 and s[0] in letras_possiveis and s[1].isdigit() in range(1,10):
        return cria_posicao(s[0], int(s[1]))
    if isinstance(s, str) and len(s) == 3 and s[0] in letras_possiveis and s[1:3] == "10":
        return cria_posicao(s[0], 10)
    return False

def eh_posicao_valida(posicao, n):
    if eh_posicao(posicao):
        return obtem_pos_lin(posicao) <= n*2 and obtem_pos_col(posicao) in letras_possiveis[:n*2]

def obtem_posicoes_adjacentes(posicao, n, d):
    if eh_posicao_valida(posicao, n):
        col = obtem_pos_col(posicao)
        lin = obtem_pos_lin(posicao)
        letras_possiveis = [chr(i) for i in range(97, 97 + n * 2)]
        
        adjacentes = []
        
        # Posições ortogonais
        ortogonais = [(col, lin - 1),  (col, lin + 1),  # Abaixo e acima
        (letras_possiveis[letras_possiveis.index(col) - 1], lin) if letras_possiveis.index(col) > 0 else None, (letras_possiveis[letras_possiveis.index(col) + 1], lin) if letras_possiveis.index(col) < len(letras_possiveis) - 1 else None]
        
        if d:
            diagonais = [
            (letras_possiveis[letras_possiveis.index(col) - 1], lin + 1) if letras_possiveis.index(col) > 0 else None,  # Acima à esquerda
            (letras_possiveis[letras_possiveis.index(col) + 1], lin + 1) if letras_possiveis.index(col) < len(letras_possiveis) - 1 else None,  # Acima à direita
            (letras_possiveis[letras_possiveis.index(col) - 1], lin - 1) if letras_possiveis.index(col) > 0 else None,  # Abaixo à esquerda
            (letras_possiveis[letras_possiveis.index(col) + 1], lin - 1) if letras_possiveis.index(col) < len(letras_possiveis) - 1 else None]
            adjacentes.extend(diagonais)
        adjacentes.extend(ortogonais)
        
        adjacentes_validas = [
        cria_posicao(c, l) for adj in adjacentes if adj is not None
        for c, l in [adj] if c in letras_possiveis and 1 <= l <= n*2]
            
        ordem_horaria = [(0, -1), (1, -1),(1, 0),(1, 1),(0, 1),(-1, 1),(-1, 0),(-1, -1),]
        
        def diferenca(pos1, pos2):
                col1, lin1 = pos1
                col2, lin2 = pos2
                return (letras_possiveis.index(col1) - letras_possiveis.index(col2), lin1 - lin2)
            
            # Ordenar as posições válidas em sentido horário
        adjacentes_validas.sort(key=lambda pos: ordem_horaria.index(diferenca(pos, (col, lin))))
        return tuple(adjacentes_validas)

def orbita(posicao, n):
    colunas = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
    centro = (n + 0.5, n + 0.5)
    distancia = max(abs(colunas[obtem_pos_col(posicao)] - centro[0]), abs(obtem_pos_lin(posicao) - centro[1]))
    return int(distancia+0.5)

def ordena_posicoes(posicoes, n):
    return tuple(sorted(posicoes, key=lambda x: (orbita(x,n), obtem_pos_lin(x), obtem_pos_col(x))))
  
def cria_pedra_branca():
    return -1  

def cria_pedra_preta():
    return 1

def cria_pedra_neutra():
    return 0

def eh_pedra(arg):
    return arg in (-1, 0, 1)

def eh_pedra_branca(arg):
    return arg == -1 or arg == 'O'

def eh_pedra_preta(arg):
    return arg == 1 or arg == 'X'

def pedras_iguais(pedra1, pedra2):
    return pedra1 == pedra2

def pedra_para_str(pedra):
    if pedra == -1:
        return 'O'
    elif pedra == 1:
        return 'X'
    else:
        return ' '
    
def eh_pedra_jogador(pedra):
    return pedra in (-1, 1)

def pedra_para_int(pedra):
    if eh_pedra_branca(pedra):
        return -1
    if eh_pedra_preta(pedra):
        return 1
    return 0

def cria_tabuleiro_vazio(n):
    if 2<=n<=5 and isinstance(n, int):
        return [[0 for i in range(n * 2)] for i in range(n * 2)]
    raise ValueError('cria_tabuleiro_vazio: argumento invalido')

def cria_tabuleiro(n, tuplo_pretas, tuplo_brancas):
    if type(tuplo_pretas) == tuple and type(tuplo_brancas) == tuple and 2<=n<=5:
            tabuleiro = cria_tabuleiro_vazio(n)
            for posicao in tuplo_pretas:
                if not eh_posicao_valida(posicao, n) or posicao in tuplo_brancas:
                    raise ValueError('cria_tabuleiro: argumentos invalidos')
                linha = obtem_pos_lin(posicao) - 1
                coluna = letras_possiveis.index(obtem_pos_col(posicao))
                tabuleiro[linha][coluna] = cria_pedra_preta()
                
            for posicao in tuplo_brancas:
                if not eh_posicao_valida(posicao, n) or posicao in tuplo_pretas:
                    raise ValueError('cria_tabuleiro: argumentos invalidos')
                linha = obtem_pos_lin(posicao) - 1  # Converte linha para índice de 0 a n-1
                coluna = letras_possiveis.index(obtem_pos_col(posicao))  # Converte coluna para índice
                tabuleiro[linha][coluna] = cria_pedra_branca()  # Marca a pedra branca na posição correta
            
            return tabuleiro
    
    raise ValueError('cria_tabuleiro: argumentos invalidos')

def cria_copia_tabuleiro(tabuleiro):
    return [[tabuleiro[i][j] for j in range(len(tabuleiro[i]))] for i in range(len(tabuleiro))]

def obtem_numero_orbitas(tabuleiro):
    return len(tabuleiro) // 2

def obtem_pedra(tabuleiro, posicao):
    if eh_posicao_valida(posicao, obtem_numero_orbitas(tabuleiro)):
        linha = obtem_pos_lin(posicao) - 1
        coluna = letras_possiveis.index(obtem_pos_col(posicao))
        return tabuleiro[linha][coluna]

def obtem_linha_horizontal(tabuleiro, posicao):
    if eh_posicao_valida(posicao, obtem_numero_orbitas(tabuleiro)):
        linha = posicao[1]
        linha_index = linha - 1  # Convert row number to index
        linha_horizontal = []
        
        for i in range(len(tabuleiro[linha_index])):
            pos = cria_posicao(letras_possiveis[i], linha)
            pedra = tabuleiro[linha_index][i]
            linha_horizontal.append((pos, pedra))
        
        return tuple(linha_horizontal)

def obtem_linha_vertical(tabuleiro, posicao):
    if eh_posicao_valida(posicao, obtem_numero_orbitas(tabuleiro)):
        coluna = obtem_pos_col(posicao)
        coluna_index = letras_possiveis.index(coluna)  # Convert column letter to index
        linha_vertical = []
        
        for i in range(len(tabuleiro)):
            pos = cria_posicao(coluna, i + 1)
            pedra = tabuleiro[i][coluna_index]
            linha_vertical.append((pos, pedra))
        
        return tuple(linha_vertical)

def ordenar_diagonais(diagonal, tipo):
    if tipo == 'diagonal':
        # Sort diagonal (top-left to bottom-right)
        return sorted(diagonal, key=lambda pos: (obtem_pos_lin(pos[0]), letras_possiveis.index(obtem_pos_col(pos[0]))))
    if tipo == 'antidiagonal':
        # Sort antidiagonal (bottom-left to top-right)
        return sorted(diagonal, key=lambda pos: (-obtem_pos_lin(pos[0]), letras_possiveis.index(obtem_pos_col(pos[0]))))
    
def obtem_linhas_diagonais(tabuleiro, posicao):
    if eh_posicao_valida(posicao, obtem_numero_orbitas(tabuleiro)):
        diagonal = []
        antidiagonal = []
        # Índice da linha (convertendo para índice 0)
        
        def fazer_diagonais():
            col_index = letras_possiveis.index(obtem_pos_col(posicao))  # Índice da coluna
            lin_index = obtem_pos_lin(posicao) - 1
        # Diagonal principal (descendente da esquerda para a direita)
            i, j = lin_index, col_index
            while i >= 0 and j >= 0:  # Percorre diagonal acima/esquerda
                diagonal.append((cria_posicao(letras_possiveis[j], i+1), tabuleiro[i][j]))
                i -= 1
                j -= 1
            i, j = lin_index + 1, col_index + 1
            while i < len(tabuleiro) and j < len(tabuleiro):  # Percorre diagonal abaixo/direita
                diagonal.append((cria_posicao(letras_possiveis[j], i+1), tabuleiro[i][j]))
                i += 1
                j += 1
            return diagonal
        
        def fazer_antidiagonais():
            col_index = letras_possiveis.index(obtem_pos_col(posicao))  # Índice da coluna
            lin_index = obtem_pos_lin(posicao) - 1
        # Antidiagonal (ascendente da esquerda para a direita)
            i, j = lin_index, col_index
            while i >= 0 and j < len(tabuleiro):  # Percorre antidiagonal acima/direita
                antidiagonal.append((cria_posicao(letras_possiveis[j], i + 1), tabuleiro[i][j]))
                i -= 1
                j += 1
            i, j = lin_index + 1, col_index - 1
            while i < len(tabuleiro) and j >= 0:  # Percorre antidiagonal abaixo/esquerda
                antidiagonal.append((cria_posicao(letras_possiveis[j], i + 1), tabuleiro[i][j]))
                i += 1
                j -= 1
                
            return antidiagonal
        
        diagonal = fazer_diagonais()
        antidiagonal = fazer_antidiagonais()
        # Ordenar e retornar as diagonais
        return tuple(ordenar_diagonais(diagonal, "diagonal")), tuple(ordenar_diagonais(antidiagonal, "antidiagonal"))
    

def obtem_posicoes_pedra(tabuleiro, pedra):
    if eh_pedra(pedra):
        posicoes = ()
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)):
                if tabuleiro[i][j] == pedra:
                    posicoes += (cria_posicao(letras_possiveis[j], i + 1),)
        return tuple(ordena_posicoes(posicoes, obtem_numero_orbitas(tabuleiro)))

def coloca_pedra(tabuleiro, posicao, pedra):
    if eh_tabuleiro(tabuleiro) and eh_posicao_valida(posicao, obtem_numero_orbitas(tabuleiro)) and eh_pedra(pedra):
        linha = obtem_pos_lin(posicao) - 1
        coluna = letras_possiveis.index(obtem_pos_col(posicao))
        tabuleiro[linha][coluna] = pedra
        return tabuleiro

def remove_pedra(tabuleiro, posicao):
    if eh_tabuleiro(tabuleiro) and eh_posicao_valida(posicao, obtem_numero_orbitas(tabuleiro)):
        linha = obtem_pos_lin(posicao) - 1
        coluna = letras_possiveis.index(obtem_pos_col(posicao))
        tabuleiro[linha][coluna] = 0
        return tabuleiro

def eh_tabuleiro(arg):
    if isinstance(arg, list) and len(arg) > 0:
        for linha in arg:
            if not isinstance(linha, list) or len(linha) != len(arg):
                return False
            for pedra in linha:
                if not eh_pedra(pedra):
                    return False
        return True
    return False

def tabuleiros_iguais(tabuleiro1, tabuleiro2):
    if eh_tabuleiro(tabuleiro1) and eh_tabuleiro(tabuleiro2):
        return tabuleiro1 == tabuleiro2

def tabuleiro_para_str(tabuleiro):
    if eh_tabuleiro(tabuleiro):
        string = " "
        for i in range(obtem_numero_orbitas(tabuleiro)*2):
            string += "   " + letras_possiveis[i] 
        for i in range(len(tabuleiro)):
            if i+1 < 10:
                string += "\n" + "0" + str(i+1) + f" [{pedra_para_str(tabuleiro[i][0])}]"
            else:
                string += "\n" + str(i+1) + f" [{pedra_para_str(tabuleiro[i][0])}]"
            for j in range(len(tabuleiro)-1):
                string += f"-[{pedra_para_str(tabuleiro[i][j+1])}]"
            
            if i < len(tabuleiro) - 1:  
                string += "\n" + "    |" + "   |"*(len(tabuleiro)-1)
                
        return string

def move_pedra(tabuleiro, p1, p2):
    if eh_tabuleiro(tabuleiro) and eh_posicao_valida(p1, obtem_numero_orbitas(tabuleiro)) and eh_posicao_valida(p2, obtem_numero_orbitas(tabuleiro)):
        if obtem_pedra(tabuleiro, p1) == 0 or obtem_pedra(tabuleiro, p2) != 0 or p1 == p2:
            return False
        tabuleiro = coloca_pedra(tabuleiro, p2, obtem_pedra(tabuleiro, p1))
        tabuleiro = remove_pedra(tabuleiro, p1)
        return tabuleiro
    
    return False

def obtem_posicao_seguinte(tabuleiro, posicao, d):
    if eh_tabuleiro(tabuleiro) and eh_posicao_valida(posicao, obtem_numero_orbitas(tabuleiro)) and d in (True, False):
        linha = obtem_pos_lin(posicao) - 1
        coluna = letras_possiveis.index(obtem_pos_col(posicao))
        linha = obtem_pos_lin(posicao) - 1
        coluna = letras_possiveis.index(obtem_pos_col(posicao))
        orbita = min(linha, coluna, len(tabuleiro) - 1 - linha, len(tabuleiro) - 1 - coluna)
        
        if d:  # Sentido horário
            if linha == orbita and coluna < len(tabuleiro) - 1 - orbita:
                coluna += 1  # Movendo para a direita
            elif coluna == len(tabuleiro) - 1 - orbita and linha < len(tabuleiro) - 1 - orbita:
                linha += 1  # Movendo para baixo
            elif linha == len(tabuleiro) - 1 - orbita and coluna > orbita:
                coluna -= 1  # Movendo para a esquerda
            elif coluna == orbita and linha > orbita:
                linha -= 1  # Movendo para cima
        else:  # Sentido anti-horário
            if linha == orbita and coluna > orbita:
                coluna -= 1  # Movendo para a esquerda
            elif coluna == orbita and linha < len(tabuleiro) - 1 - orbita:
                linha += 1  # Movendo para baixo
            elif linha == len(tabuleiro) - 1 - orbita and coluna < len(tabuleiro) - 1 - orbita:
                coluna += 1  # Movendo para a direita
            elif coluna == len(tabuleiro) - 1 - orbita and linha > orbita:
                linha -= 1  # Movendo para cima
        return cria_posicao(letras_possiveis[coluna], linha + 1)

def roda_tabuleiro(tabuleiro):
    if eh_tabuleiro(tabuleiro):
        n_orbitas = obtem_numero_orbitas(tabuleiro)
        tabuleiro_novo = cria_tabuleiro_vazio(n_orbitas)
        
        for posicao in obtem_posicoes_pedra(tabuleiro, 1):
            posicao_seguinte = obtem_posicao_seguinte(tabuleiro, posicao, False)
            coloca_pedra(tabuleiro_novo, posicao_seguinte, 1)
            
        for posicao in obtem_posicoes_pedra(tabuleiro, -1):
            posicao_seguinte = obtem_posicao_seguinte(tabuleiro, posicao, False)
            coloca_pedra(tabuleiro_novo, posicao_seguinte, -1)
            
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro[i])):
                tabuleiro[i][j] = tabuleiro_novo[i][j]
                
        return tabuleiro
        

def verifica_linha_pedras(tabuleiro, posicao, pedra, k):
    if eh_tabuleiro(tabuleiro) and eh_posicao_valida(posicao, obtem_numero_orbitas(tabuleiro)) and eh_pedra(pedra) and 0 < k <= obtem_numero_orbitas(tabuleiro)*2:
        if obtem_pedra(tabuleiro, posicao) != pedra or obtem_pedra(tabuleiro, posicao) == 0:
            return False
        
        # Obtém a linha, coluna e diagonais correspondentes à posição
        linha = obtem_linha_horizontal(tabuleiro, posicao)
        coluna = obtem_linha_vertical(tabuleiro, posicao)
        diag = obtem_linhas_diagonais(tabuleiro, posicao)
        
        # Conta o número máximo de valores consecutivos na coluna, linha e diagonais
        colunas_cons = conta_consecutivos(coluna, pedra) # Usa a função auxiliar
        linhas_cons = conta_consecutivos(linha, pedra)
        diag_cons = conta_consecutivos(diag[0], pedra)      # Diagonal principal
        antidiag_cons = conta_consecutivos(diag[1], pedra)  # Antidiagonal
        
        # Verifica se há valores consecutivos suficientes em qualquer direção
        if colunas_cons >= k or linhas_cons >= k or diag_cons >= k or antidiag_cons >= k:
            return True
        
    return False

def conta_consecutivos(tuplo1, pedra):
    contador = 0
    cont_max = 0
    
    # Process the tuple of positions and their corresponding values
    for pos, valor in tuplo1:
        if valor == pedra:
            contador += 1
            cont_max = max(cont_max, contador)  # Keep track of the maximum consecutive stones
        else:
            contador = 0  # Reset the counter if the value doesn't match the player's stone
    
    return cont_max

def eh_vencedor(tabuleiro, pedra):
    if eh_tabuleiro(tabuleiro) and eh_pedra_jogador(pedra):
        n_orbitas = obtem_numero_orbitas(tabuleiro)
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)):
                posicao = cria_posicao(letras_possiveis[j], i + 1)
                if verifica_linha_pedras(tabuleiro, posicao, pedra, n_orbitas*2):
                    return True
    return False      

def eh_fim_jogo(tabuleiro):
    if eh_tabuleiro(tabuleiro):
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)):
                posicao = cria_posicao(letras_possiveis[j], i + 1)
                if verifica_linha_pedras(tabuleiro, posicao, 1, obtem_numero_orbitas(tabuleiro)*2) or verifica_linha_pedras(tabuleiro, posicao, -1, obtem_numero_orbitas(tabuleiro)*2):
                    return True
        if len(obtem_posicoes_pedra(tabuleiro, cria_pedra_neutra())) == 0:
            return True
    return False
    
def escolhe_movimento_manual(tabuleiro):
    if eh_tabuleiro(tabuleiro):
        posicao = input("Escolha uma posicao livre:")
        posicao_convertida = str_para_posicao(posicao)# Solicita ao jogador que escolha uma posição livre
        if isinstance(posicao, str) and posicao_convertida and eh_posicao_valida(posicao_convertida, obtem_numero_orbitas(tabuleiro)):
            if obtem_pedra(tabuleiro, str_para_posicao(posicao)) == 0:
                return f'{posicao}'
            
    return escolhe_movimento_manual(tabuleiro)   # Se a posição não for válida, solicita novamente

def escolhe_movimento_auto(tabuleiro, pedra, lvl):
    if eh_tabuleiro(tabuleiro) and eh_pedra_jogador(pedra) and isinstance(lvl, str):
        if lvl in ("facil", "normal"):
            if lvl == "facil":
                return estratégia_facil(tabuleiro, pedra)
            elif lvl == "normal":
                return estratégia_normal(tabuleiro, pedra, obtem_numero_orbitas(tabuleiro)*2)

def estratégia_facil(tabuleiro, pedra):
    tabuleiro_copia = cria_copia_tabuleiro(tabuleiro)
    roda_tabuleiro(tabuleiro_copia)
    posicoes_originais = ()
    pedras = obtem_posicoes_pedra(tabuleiro, pedra)
    posicoes_livres = obtem_posicoes_pedra(tabuleiro, cria_pedra_neutra())
    
    for i in pedras:
        posicao_seguinte = obtem_posicao_seguinte(tabuleiro, i, False)
        for adj in obtem_posicoes_adjacentes(posicao_seguinte, obtem_numero_orbitas(tabuleiro), True):
            if obtem_pedra(tabuleiro_copia, adj) == 0:
                posicoes_originais += (obtem_posicao_seguinte(tabuleiro, adj, True),)
                
    if len(posicoes_originais) != 0:
        return ordena_posicoes(posicoes_originais, obtem_numero_orbitas(tabuleiro))[0]
    if len(posicoes_livres) != 0:
        return ordena_posicoes(posicoes_livres, obtem_numero_orbitas(tabuleiro))[0]

def estratégia_normal(tabuleiro, pedra, k):
    posicoes_maq = ()
    posicoes_adv = ()

    for l in range(k, 0, -1):
        for posicao in obtem_posicoes_pedra(tabuleiro, 0):
            tabuleiro_copia = cria_copia_tabuleiro(tabuleiro)
            pedra_seguinte1 = obtem_posicao_seguinte(tabuleiro_copia, posicao, False)
            roda_tabuleiro(tabuleiro_copia)
            pedra_seguinte2 = obtem_posicao_seguinte(tabuleiro_copia, pedra_seguinte1, False)
            coloca_pedra(tabuleiro_copia, pedra_seguinte1, pedra)

            if verifica_linha_pedras(tabuleiro_copia, pedra_seguinte1, pedra, l):
                posicoes_maq += (posicao,)
                    
            roda_tabuleiro(tabuleiro_copia)
            coloca_pedra(tabuleiro_copia, pedra_seguinte2, -pedra)
            
            if verifica_linha_pedras(tabuleiro_copia, pedra_seguinte2, -pedra, l):
                posicoes_adv += (posicao,)
                  
        if len(posicoes_maq) != 0:
            return ordena_posicoes(posicoes_maq, obtem_numero_orbitas(tabuleiro))[0]  
        if len(posicoes_adv) != 0:
            return ordena_posicoes(posicoes_adv, obtem_numero_orbitas(tabuleiro))[0]
        
    return ordena_posicoes(obtem_posicoes_pedra(tabuleiro, 0), obtem_numero_orbitas(tabuleiro))[0]
        
def orbito(orb, lvl, pedra_str):
    if isinstance(orb, int) and isinstance(pedra_str, str) and isinstance(lvl, str):
        if 2<=orb<=5 and pedra_str in ("X", "O") and lvl in ("facil", "normal","2jogadores"):
            tabuleiro_vazio = cria_tabuleiro_vazio(orb)
            print(f"Bem-vindo ao ORBITO-{orb}.")
            if lvl in ("facil", "normal"):
                return singleplayer(tabuleiro_vazio, pedra_str, lvl)
            else:
                return multiplayer(tabuleiro_vazio, pedra_para_int(pedra_str))
    raise ValueError('orbito: argumentos invalidos')

def singleplayer(tabuleiro, pedra, lvl):
    print(f"Jogo contra o computador ({lvl}).\nO jogador joga com '{pedra}'.")
    print(tabuleiro_para_str(tabuleiro))
    
    if pedra == "X":
        valor = 1
    
    if pedra == "O":
        valor = -1

    return resto_singleplayer(tabuleiro, pedra_para_int(pedra), valor, lvl)

def resto_singleplayer(tabuleiro, pedra, valor, lvl):
    while not eh_fim_jogo(tabuleiro):
        if pedra == cria_pedra_preta():
            print("Turno do jogador.")
            jogada_humana = escolhe_movimento_manual(tabuleiro)
            coloca_pedra(tabuleiro, str_para_posicao(jogada_humana), valor)
            roda_tabuleiro(tabuleiro)
            print(tabuleiro_para_str(tabuleiro))
            
            if eh_fim_jogo(tabuleiro):   # Verifica se o jogo terminou
                break
            
        if pedra == cria_pedra_branca():
            jogada_maquina = escolhe_movimento_auto(tabuleiro, -valor, lvl)
            coloca_pedra(tabuleiro, jogada_maquina, -valor)
            print(f"Turno do computador ({lvl}):")
            roda_tabuleiro(tabuleiro) 
            print(tabuleiro_para_str(tabuleiro))
    
            if eh_fim_jogo(tabuleiro):   # Verifica se o jogo terminou
                break
        
        pedra = -pedra
    
    if eh_vencedor(tabuleiro, pedra):  # Verifica se a máquina ganhou/humano perdeu
        print("VITORIA")
        return pedra
    
    elif eh_vencedor(tabuleiro, -pedra):
        print("DERROTA")
        return -pedra
    
    print("EMPATE")
    return 0

def multiplayer(tabuleiro, pedra):
    print("Jogo para dois jogadores.")
    print(tabuleiro_para_str(tabuleiro))
    valor = pedra
    while not eh_fim_jogo(tabuleiro):
        print(f"Turno do jogador '{pedra_para_str(valor)}'.")
        jogada_humana = escolhe_movimento_manual(tabuleiro)
        coloca_pedra(tabuleiro, str_para_posicao(jogada_humana), valor)
        roda_tabuleiro(tabuleiro)
        print(tabuleiro_para_str(tabuleiro))
        
        if eh_fim_jogo(tabuleiro):   # Verifica se o jogo terminou
            break

        valor = -valor
        
    if eh_vencedor(tabuleiro, pedra):
        print(f"VITORIA DO JOGADOR '{pedra_para_str(pedra)}'")
        return pedra
    if eh_vencedor(tabuleiro, -pedra):
        print(F"VITORIA DO JOGADOR '{pedra_para_str(-pedra)}'")
        return -pedra
    
    print("EMPATE")
    return 0

#print(orbito(2, "normal", "X"))
