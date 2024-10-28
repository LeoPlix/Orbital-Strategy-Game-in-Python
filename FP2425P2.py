letras_possiveis = ("a","b","c","d","e","f","g","h", "i", "j")    #Variável global com as letras possíveis

#TAD Posição
#Construtor
def cria_posicao(letra, num):
    """
    Função que cria a posição com um formato imutável e hashable.
    Recebe como input uma letra correspondente à coluna e um número correspondente à linha.
    Retorna um tuplo com a letra no indice 0 e o número no indice 1.
    cria posicao: str x int → posicao
    """
    if isinstance(letra, str) and isinstance(num, int):
        if len(letra) == 1 and letra in letras_possiveis and num in range(1,11):
            return (letra, num)
    raise ValueError('cria_posicao: argumentos invalidos')

#Seletores
def obtem_pos_col(posicao):
    """
    Função que retorna a coluna da posição.
    Recebe o tuplo da posição e retorna o elemento de indice 0 do mesmo.
    posicao → str   
    """
    return posicao[0]

def obtem_pos_lin(posicao):
    """
    Função que retorna a linha da posição.
    Recebe o tuplo da posição e retorna o elemento de indice 1 do mesmo.
    posicao → int
    """
    return posicao[1]

#Reconhecedor
def eh_posicao(arg):
    """
    Função que verifica se o argumento é uma posição.
    Recebe um argumento e verifica se é um tuplo com 2 elementos, sendo o primeiro uma letra e o segundo um número.
    Retorna True se for uma posição e False caso contrário.
    universal → bool
    """
    return isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], str) and isinstance(arg[1], int) and arg[0] in letras_possiveis and arg[1] in range(1,11)

#Teste
def posicoes_iguais(pos1, pos2):
    """
    Função que verifica se duas posições são iguais.
    Recebe duas posições e retorna um valor booleano True se forem iguais e False caso contrário.
    posicao x posicao → bool
    """
    return pos1 == pos2

#Transformador
def posicao_para_str(pos):
    """ 
    Função que converte uma posição para string.
    Recebe uma posição e retorna uma string com a letra e o número da posição.
    posicao → str
    """
    return pos[0] + str(pos[1])

def str_para_posicao(s):
    """
    Função que converte uma string para uma posição.
    Recebe uma string com a letra e o número e retorna uma posição.
    str → posicao   
    """
    if isinstance(s, str) and len(s) == 2 and s[0] in letras_possiveis and s[1].isdigit() in range(1,10):
        return cria_posicao(s[0], int(s[1]))
    if isinstance(s, str) and len(s) == 3 and s[0] in letras_possiveis and s[1:3] == "10":
        return cria_posicao(s[0], 10)   #Caso especial para linha igual a 10
    return False

def eh_posicao_valida(posicao, n):
    """ 
    Função que verifica se uma posição é válida dentro dos parametros do tabuleiro tendo em conta o número de orbitas.
    posição x int → bool
    """
    if eh_posicao(posicao):
        return obtem_pos_lin(posicao) <= n*2 and obtem_pos_col(posicao) in letras_possiveis[:n*2]

#Alto Nível
def obtem_posicoes_adjacentes(posicao, n, d):
    """ 
    Função que retorna as posições adjacentes a uma dada posição de um tabuleiro com determinado número de órbitas.
    Caso d seja True, retorna todas as adjacentes. Caso contrário, retorna apenas as ortogonais.
    posicao x int x bool → tuplo de posicoes
    """
    col = obtem_pos_col(posicao)  #obter coluna da posição
    lin = obtem_pos_lin(posicao)  #obter linha da posição
    letras_possiveis = [chr(i) for i in range(97, 97 + n * 2)]  # Gera as letras possíveis para as colunas
    
    if d:
        direcoes = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]   #Todas as direções
    else:
        direcoes = [(0, -1), (1, 0), (0, 1), (-1, 0)]   #Apenas as direções ortogonais

    adjacentes_validas = [
        cria_posicao(letras_possiveis[letras_possiveis.index(col) + direcao_col], lin + direcao_lin)  # Cria a posição adjacente
        for direcao_col, direcao_lin in direcoes
        if 0 <= letras_possiveis.index(col) + direcao_col < len(letras_possiveis) and 1 <= lin + direcao_lin <= n * 2]  # Verifica se a posição pertence ao tabuleiro
    
    return tuple(adjacentes_validas)

def ordena_posicoes(posicoes, n):
    """ 
    Função que ordena as posições de acordo com a ordem específica de leitura do tabuleiro de Orbito.
    Calcula a distância máxima entre a posição e o centro do tabuleiro, usando valores numéricos para as colunas e linhas.
    Utiliza o 0.5 para calcular a distância ao centro de uma forma mais especifica.
    posição x int → tuplo de posicoes
    """
    colunas = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
    return tuple(sorted(posicoes,key=lambda posicao: (max(abs(colunas[obtem_pos_col(posicao)] - (n + 0.5)), abs(obtem_pos_lin(posicao) - (n + 0.5))),
                obtem_pos_lin(posicao), colunas[obtem_pos_col(posicao)])))
  
#TAD Pedra
#Construtor
def cria_pedra_branca():
    """ 
    Função que cria uma pedra branca, representada por -1.
    {} → pedra
    """
    return -1  

def cria_pedra_preta():
    """
    Função que cria uma pedra preta, representada por 1.
    {} → pedra
    """
    return 1

def cria_pedra_neutra():
    """
    Função que cria uma pedra neutra, representada por 0.
    {} → pedra
    """
    return 0

#Reconhecedor
def eh_pedra(arg):
    """ 
    Função que verifica se o argumento é uma pedra.
    universal → bool
    """
    return arg in (cria_pedra_preta(), cria_pedra_branca(), cria_pedra_neutra())

def eh_pedra_branca(pedra):
    """ 
    Função que verifica se o argumento é uma pedra branca.
    pedra → bool
    """
    return pedra == cria_pedra_branca() or pedra == pedra_para_str(cria_pedra_branca())

def eh_pedra_preta(pedra):
    """ 
    Função que verifica se o argumento é uma pedra preta.
    pedra → bool
    """
    return pedra == cria_pedra_preta() or pedra == pedra_para_str(cria_pedra_preta())

#Teste 
def pedras_iguais(pedra1, pedra2):
    """  
    Verifica se duas pedras são iguais.
    universal x universal → bool
    """
    return pedra1 == pedra2

#Transformador
def pedra_para_str(pedra):
    """ 
    Função que converte uma pedra para string.
    pedra → str
    """
    if pedra == cria_pedra_branca():
        return 'O'
    elif pedra == cria_pedra_preta():
        return 'X'
    elif pedra == cria_pedra_neutra():
        return ' '
    
#Alto Nível
def eh_pedra_jogador(pedra):
    """ 
    Função que verifica se a pedra é de um jogador, ou seja, não neutra.
    pedra → bool
    """
    if eh_pedra(pedra):
        return pedra in (cria_pedra_preta(), cria_pedra_branca())

def pedra_para_int(pedra):
    """  
    Função que converte uma pedra para um inteiro corresponde aos valores que lhes são atribuídos.
    pedra → int
    """
    if eh_pedra_branca(pedra):
        return cria_pedra_branca()
    if eh_pedra_preta(pedra):
        return cria_pedra_preta()
    return cria_pedra_neutra()

#TAD Tabuleiro
#Construtor
def cria_tabuleiro_vazio(n):
    """ 
    Função que cria um tabuleiro vazio com um número de órbitas n.
    int → tabuleiro
    """
    if 2<=n<=5 and isinstance(n, int):
        return [[0 for i in range(n * 2)] for i in range(n * 2)]
    raise ValueError('cria_tabuleiro_vazio: argumento invalido')

def cria_tabuleiro(n, tuplo_pretas, tuplo_brancas):
    """ 
    Função que cria um tabuleiro com um número de órbitas n, com pedras pretas e brancas nas posições indicadas.
    Verifica e chama uma exceção caso as posições não sejam válidas.
    int x tuplo x tuplo → tabuleiro
    """
    if type(tuplo_pretas) == tuple and type(tuplo_brancas) == tuple and 2<=n<=5:
            tabuleiro = cria_tabuleiro_vazio(n)
            for posicao in tuplo_pretas:
                if not eh_posicao_valida(posicao, n) or posicao in tuplo_brancas:  # Verifica se a posição é válida e se não está ocupada por uma pedra branca
                    raise ValueError('cria_tabuleiro: argumentos invalidos')
                linha = obtem_pos_lin(posicao) - 1
                coluna = letras_possiveis.index(obtem_pos_col(posicao))
                tabuleiro[linha][coluna] = cria_pedra_preta()  # Coloca uma pedra preta na posição correta no tabuleiro
                
            for posicao in tuplo_brancas:
                if not eh_posicao_valida(posicao, n) or posicao in tuplo_pretas: # Verifica se a posição é válida e se não está ocupada por uma pedra preta
                    raise ValueError('cria_tabuleiro: argumentos invalidos')
                linha = obtem_pos_lin(posicao) - 1  
                coluna = letras_possiveis.index(obtem_pos_col(posicao))
                tabuleiro[linha][coluna] = cria_pedra_branca()  # Marca a pedra branca na posição correta
            
            return tabuleiro
    
    raise ValueError('cria_tabuleiro: argumentos invalidos')

def cria_copia_tabuleiro(tabuleiro):
    """
    Faz uma cópia do tabuleiro, de modo a não modificar o tabuleiro original.
    tabuleiro → tabuleiro
    """
    return [[tabuleiro[i][j] for j in range(len(tabuleiro[i]))] for i in range(len(tabuleiro))]

#Seletores
def obtem_numero_orbitas(tabuleiro):
    """
    Função que retorna o número de órbitas do tabuleiro.
    tabuleiro → int
    """
    return len(tabuleiro) // 2

def obtem_pedra(tabuleiro, posicao):
    """ 
    Função que retorna a pedra numa dada posição do tabuleiro.
    tabuleiro x posicao → pedra
    """
    linha = obtem_pos_lin(posicao) - 1   #Determina a linha
    coluna = letras_possiveis.index(obtem_pos_col(posicao))   #Determina a coluna
    return tabuleiro[linha][coluna]   #Mostra a pedra na posição

def obtem_linha_horizontal(tabuleiro, posicao):
    """ 
    Função que retorna a linha horizontal da posição.
    tabuleiro x posicao → tuplo de posicoes
    """
    linha = posicao[1]
    linha_index = linha - 1 
    linha_horizontal = []
        
    for i in range(len(tabuleiro[linha_index])):  #Percorre a linha
        pos = cria_posicao(letras_possiveis[i], linha)  #Cria as posiçãos da linha
        pedra = tabuleiro[linha_index][i]
        linha_horizontal.append((pos, pedra))  #Adiciona as pedras à linha horizontal
        
    return tuple(linha_horizontal)

def obtem_linha_vertical(tabuleiro, posicao):
    """ 
    Função que retorna a linha vertical da posição.
    tabuleiro x posicao → tuplo de posicoes
    """
    coluna = obtem_pos_col(posicao)
    coluna_index = letras_possiveis.index(coluna)  
    linha_vertical = []
        
    for i in range(len(tabuleiro)): #Percorre a coluna
        pos = cria_posicao(coluna, i + 1)  #Cria as posições da coluna
        pedra = tabuleiro[i][coluna_index]
        linha_vertical.append((pos, pedra))  #Adiciona as pedras à linha vertical
        
    return tuple(linha_vertical)

def ordenar_diagonais(diagonal, tipo):
    """ 
    Função auxiliar que ordena as diagonais de acordo com a ordem específica de leitura do tabuleiro de Orbito.
    diagonal x str → diagonal
    """
    if tipo == 'diagonal':
        return sorted(diagonal, key=lambda pos: (obtem_pos_lin(pos[0]), letras_possiveis.index(obtem_pos_col(pos[0]))))
    if tipo == 'antidiagonal':
        return sorted(diagonal, key=lambda pos: (-obtem_pos_lin(pos[0]), letras_possiveis.index(obtem_pos_col(pos[0]))))
    
def obtem_linhas_diagonais(tabuleiro, posicao):
        """ 
        Função que retorna as diagonais da posição.
        Retorna um tuplo com subtuplos correspondentes às diagonais principal e antidiagonal, que são previamente ordenadas com
        uma função auxiliar, a principal de frente para trás e a antidiagonal de trás para a frente.
        tabuleiro x posicao → tuplo de posicoes
        """

        diagonal = []
        antidiagonal = []
        
        def fazer_diagonais():
            col_index = letras_possiveis.index(obtem_pos_col(posicao))  # Índice da coluna
            lin_index = obtem_pos_lin(posicao) - 1
        
            i, j = lin_index, col_index  #Diagonal principal (descendente da esquerda para a direita)
            while i >= 0 and j >= 0:  #Percorre diagonal acima/esquerda
                diagonal.append((cria_posicao(letras_possiveis[j], i+1), tabuleiro[i][j]))
                i -= 1
                j -= 1
            i, j = lin_index + 1, col_index + 1
            while i < len(tabuleiro) and j < len(tabuleiro):  #Percorre diagonal abaixo/direita
                diagonal.append((cria_posicao(letras_possiveis[j], i+1), tabuleiro[i][j]))
                i += 1
                j += 1
            return diagonal
        
        def fazer_antidiagonais():
            col_index = letras_possiveis.index(obtem_pos_col(posicao))  #Índice da coluna
            lin_index = obtem_pos_lin(posicao) - 1

            i, j = lin_index, col_index  #Antidiagonal (ascendente da esquerda para a direita)
            while i >= 0 and j < len(tabuleiro):  #Percorre antidiagonal acima/direita
                antidiagonal.append((cria_posicao(letras_possiveis[j], i + 1), tabuleiro[i][j]))
                i -= 1
                j += 1
            i, j = lin_index + 1, col_index - 1
            while i < len(tabuleiro) and j >= 0:  #Percorre antidiagonal abaixo/esquerda
                antidiagonal.append((cria_posicao(letras_possiveis[j], i + 1), tabuleiro[i][j]))
                i += 1
                j -= 1
                
            return antidiagonal
        
        diagonal = fazer_diagonais()
        antidiagonal = fazer_antidiagonais()
        
        return tuple(ordenar_diagonais(diagonal, "diagonal")), tuple(ordenar_diagonais(antidiagonal, "antidiagonal")) # Ordenar e retornar as diagonais
    

def obtem_posicoes_pedra(tabuleiro, pedra):
    """ 
    Função que retorna as posições de uma dada pedra no tabuleiro.
    tabuleiro x pedra → tuplo de posicoes
    """
    posicoes = ()
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] == pedra:   #Percorre todos os elementos do tabuleiro e verifica se a pedra é igual à pedra dada
                posicoes += (cria_posicao(letras_possiveis[j], i + 1),)  #Adiciona a posição à lista de posições
    return tuple(ordena_posicoes(posicoes, obtem_numero_orbitas(tabuleiro)))  #Ordena as posições de acordo com a ordem específica de leitura do tabuleiro de Orbito
    
#Modificadores
def coloca_pedra(tabuleiro, posicao, pedra):
    """ 
    Função que coloca uma pedra numa dada posição do tabuleiro, modificando destrutivamente o tabuleiro original.
    tabuleiro x posicao x pedra → tabuleiro
    """
    linha = obtem_pos_lin(posicao) - 1
    coluna = letras_possiveis.index(obtem_pos_col(posicao))
    tabuleiro[linha][coluna] = pedra  #Coloca a pedra na posição dada
    return tabuleiro

def remove_pedra(tabuleiro, posicao):
    """ 
    Função que remove uma pedra de uma dada posição do tabuleiro, modificando destrutivamente o tabuleiro original.
    tabuleiro x posicao → tabuleiro
    """
    linha = obtem_pos_lin(posicao) - 1
    coluna = letras_possiveis.index(obtem_pos_col(posicao))
    tabuleiro[linha][coluna] = cria_pedra_neutra()  #Remove a pedra da posição dada, substituindo-a por uma pedra neutra
    return tabuleiro

#Reconhecedor
def eh_tabuleiro(arg):
    """ 
    Função que verifica se o argumento é um tabuleiro.
    universal → bool
    """
    if isinstance(arg, list):  #Verifica se é uma lista
        if len(arg) > 0:  #Verifica se a lista tem elementos
            for linha in arg:
                if not isinstance(linha, list):  #Verifica se os elementos da lista são listas
                    return False
                if len(linha) != len(arg):  #Verifica se as listas têm o mesmo tamanho
                    return False
                for pedra in linha:
                    if not eh_pedra(pedra):  #Verifica se os elementos das listas são pedras
                        return False
            return True
    return False

#Teste
def tabuleiros_iguais(tabuleiro1, tabuleiro2):
    """ 
    Função que verifica se dois tabuleiros são iguais.
    tabuleiro x tabuleiro → bool
    """
    return tabuleiro1 == tabuleiro2

#Transformador
def tabuleiro_para_str(tabuleiro):
    """ 
    Função que converte um tabuleiro para string para efeitos de aplicar mais tarde.
    tabuleiro → str
    """
    string = " " #String vazia porque o tabuleiro começa com um espaço
    for i in range(obtem_numero_orbitas(tabuleiro)*2):
        string += "   " + letras_possiveis[i]  #Adiciona as letras das colunas com o respectivo espaçamento
    for i in range(len(tabuleiro)):
        if i+1 < 10:
            string += "\n" + "0" + str(i+1) + f" [{pedra_para_str(tabuleiro[i][0])}]"  #Adiciona o número da linha e a pedra na posição na primeira coluna
        else:
            string += "\n" + str(i+1) + f" [{pedra_para_str(tabuleiro[i][0])}]"  #Para o caso especial de a linha ser 10 na primeira coluna
        for j in range(len(tabuleiro)-1):
            string += f"-[{pedra_para_str(tabuleiro[i][j+1])}]"  #Adiciona as pedras nas restantes posições
            
        if i < len(tabuleiro) - 1:  
            string += "\n" + "    |" + "   |"*(len(tabuleiro)-1)  #Adiciona as linhas verticais
                
    return string

#Alto Nível
def move_pedra(tabuleiro, p1, p2):
    """ 
    Função que move uma pedra de uma posição para outra, modificando destrutivamente o tabuleiro original.
    tabuleiro x posicao x posicao → tabuleiro
    """
    pedra = obtem_pedra(tabuleiro, p1)  #Obtém a pedra da posição inicial
    remove_pedra(tabuleiro, p1)  #Remove a pedra da posição inicial
    coloca_pedra(tabuleiro, p2, pedra)  #Coloca a pedra na posição final
    return tabuleiro

def obtem_posicao_seguinte(tabuleiro, posicao, d):
    """ 
    Função que retorna a posição seguinte de uma dada posição, num dado sentido, no tabuleiro.
    Caso d seja True, o sentido é horário. Caso contrário, é anti-horário.
    tabuleiro x posicao x bool → posicao
    """
    if eh_tabuleiro(tabuleiro) and eh_posicao_valida(posicao, obtem_numero_orbitas(tabuleiro)) and d in (True, False):
        linha = obtem_pos_lin(posicao) - 1
        coluna = letras_possiveis.index(obtem_pos_col(posicao))
        linha = obtem_pos_lin(posicao) - 1
        coluna = letras_possiveis.index(obtem_pos_col(posicao))
        orbita = min(linha, coluna, len(tabuleiro) - 1 - linha, len(tabuleiro) - 1 - coluna)
        
        if d:  # Sentido horário
            if linha == orbita and coluna < len(tabuleiro) - 1 - orbita:
                coluna += 1  # Move para a direita
            elif coluna == len(tabuleiro) - 1 - orbita and linha < len(tabuleiro) - 1 - orbita:
                linha += 1  # Move para baixo
            elif linha == len(tabuleiro) - 1 - orbita and coluna > orbita:
                coluna -= 1  # Move para a esquerda
            elif coluna == orbita and linha > orbita:
                linha -= 1  # Move para cima
        else:  # Sentido anti-horário
            if linha == orbita and coluna > orbita:
                coluna -= 1  # Move para a esquerda
            elif coluna == orbita and linha < len(tabuleiro) - 1 - orbita:
                linha += 1  # Move para baixo
            elif linha == len(tabuleiro) - 1 - orbita and coluna < len(tabuleiro) - 1 - orbita:
                coluna += 1  # Move para a direita
            elif coluna == len(tabuleiro) - 1 - orbita and linha > orbita:
                linha -= 1  # Move para cima
                
        return cria_posicao(letras_possiveis[coluna], linha + 1)

def roda_tabuleiro(tabuleiro):
    """
    Função que roda o tabuleiro no sentido anti-horário.
    tabuleiro → tabuleiro
    """
    if eh_tabuleiro(tabuleiro):
        n_orbitas = obtem_numero_orbitas(tabuleiro)
        tabuleiro_novo = cria_tabuleiro_vazio(n_orbitas) #Cria um tabuleiro vazio para adicionar as pedras
        
        for posicao in obtem_posicoes_pedra(tabuleiro, 1):
            posicao_seguinte = obtem_posicao_seguinte(tabuleiro, posicao, False) #Obtém a posição seguinte
            coloca_pedra(tabuleiro_novo, posicao_seguinte, 1) #Coloca a pedra na posição seguinte
            
        for posicao in obtem_posicoes_pedra(tabuleiro, -1):
            posicao_seguinte = obtem_posicao_seguinte(tabuleiro, posicao, False) #Obtém a posição seguinte
            coloca_pedra(tabuleiro_novo, posicao_seguinte, -1) #Coloca a pedra na posição seguinte
            
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro[i])):
                tabuleiro[i][j] = tabuleiro_novo[i][j]  #Substitui o tabuleiro original pelo novo
                
        return tabuleiro

def verifica_linha_pedras(tabuleiro, posicao, pedra, k):
    """ 
    Função que verifica se há k pedras consecutivas numa linha, coluna ou diagonal a partir de uma dada posição.
    A função auxiliar conta_consecutivos é utilizada para contar o número de pedras consecutivas.
    tabuleiro x posicao x pedra x int → bool
    """
    if eh_tabuleiro(tabuleiro) and eh_posicao_valida(posicao, obtem_numero_orbitas(tabuleiro)) and eh_pedra(pedra) and k>0:
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

def conta_consecutivos(tuplo, pedra):
    """ 
    Função auxiliar que conta o número de pedras consecutivas nas posicoes dadas, considerando a posição principal.
    tuplo x pedra → int
    """
    contador = 0
    cont_max = 0
    
    for pos, valor in tuplo:
        if valor == pedra:
            contador += 1
            cont_max = max(cont_max, contador)   #Atualiza o contador máximo
        else:
            contador = 0  #Reinicia o contador
    
    return cont_max

#Funções Adicionais
def eh_vencedor(tabuleiro, pedra):
    """ 
    Função que verifica se um jogador é vencedor, ou seja, se tem uma linha (orbitas*2) de pedras consecutivas.
    tabuleiro x pedra → bool
    """
    if eh_tabuleiro(tabuleiro) and eh_pedra_jogador(pedra):
        n_orbitas = obtem_numero_orbitas(tabuleiro)
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)):
                posicao = cria_posicao(letras_possiveis[j], i + 1) #Cria a posição 
                if verifica_linha_pedras(tabuleiro, posicao, pedra, n_orbitas*2):  #Verifica se há uma linha de pedras consecutivas
                    return True
    return False      

def eh_fim_jogo(tabuleiro):
    """ 
    Função que verifica se o jogo terminou, ou seja, se há um vencedor ou se o tabuleiro está cheio.
    tabuleiro → bool
    """
    if eh_tabuleiro(tabuleiro):
        if eh_vencedor(tabuleiro, cria_pedra_branca()) or eh_vencedor(tabuleiro, cria_pedra_preta()):  #Verifica se há um vencedor
            return True
        if len(obtem_posicoes_pedra(tabuleiro, cria_pedra_neutra())) == 0:  #Verifica se o tabuleiro está cheio
            return True
        
    return False
    
def escolhe_movimento_manual(tabuleiro):
    """ 
    Função que solicita ao jogador uma posição livre para colocar uma pedra e verifica se a mesma é possível.
    tabuleiro → str
    """
    posicao_valida = False
    while not posicao_valida:
        posicao = input("Escolha uma posicao livre:")  #Solicita ao jogador que escolha uma posição livre
        if str_para_posicao(posicao) in obtem_posicoes_pedra(tabuleiro, cria_pedra_neutra()):
            return posicao_para_str(posicao)
        
def escolhe_movimdnto_manual(tabuleiro):
    """ 
    Função que solicita ao jogador uma posição livre para colocar uma pedra e verifica se a mesma é possível.
    tabuleiro → str
    """
    if eh_tabuleiro(tabuleiro):
        posicao = input("Escolha uma posicao livre:")
        posicao_convertida = str_para_posicao(posicao)  #Solicita ao jogador que escolha uma posição livre
        if isinstance(posicao, str) and posicao_convertida and eh_posicao_valida(posicao_convertida, obtem_numero_orbitas(tabuleiro)):
            if obtem_pedra(tabuleiro, str_para_posicao(posicao)) == 0:
                return f'{posicao}'
            
    return escolhe_movimento_manual(tabuleiro)   #Se a posição não for válida, solicita novamente

def escolhe_movimento_auto(tabuleiro, pedra, lvl):
    """ 
    Função que escolhe um movimento automático para o computador, de acordo com o nível de dificuldade escolhido.
    tabuleiro x pedra x str → str
    """
    if eh_tabuleiro(tabuleiro) and eh_pedra_jogador(pedra) and isinstance(lvl, str):
        if lvl in ("facil", "normal"):  #Verifica se o nível é válido
            if lvl == "facil":
                return estratégia_facil(tabuleiro, pedra)
            elif lvl == "normal":
                return estratégia_normal(tabuleiro, pedra, obtem_numero_orbitas(tabuleiro)*2)

def estratégia_facil(tabuleiro, pedra):
    """ 
    Função que escolhe um movimento automático para o computador, de acordo com o nível de dificuldade fácil.
    Se existir no tabuleiro pelo menos uma posi¸c˜ao livre que no fim do turno (após rotação) fique adjacente a uma pedra própria, jogar numa dessas posições;
    Se não, jogar numa posição livre.
    tabuleiro x pedra → str
    """
    tabuleiro_copia = cria_copia_tabuleiro(tabuleiro) #Para não modificar o tabuleiro original
    roda_tabuleiro(tabuleiro_copia) #Roda o tabuleiro
    posicoes_originais = ()
    pedras = obtem_posicoes_pedra(tabuleiro, pedra)
    posicoes_livres = obtem_posicoes_pedra(tabuleiro, cria_pedra_neutra()) #Obtém as posições livres
    
    for i in pedras:
        posicao_seguinte = obtem_posicao_seguinte(tabuleiro, i, False)
        for adj in obtem_posicoes_adjacentes(posicao_seguinte, obtem_numero_orbitas(tabuleiro), True): #Obtém as posições adjacentes
            if obtem_pedra(tabuleiro_copia, adj) == 0:
                posicoes_originais += (obtem_posicao_seguinte(tabuleiro, adj, True),)  #Adiciona as posições adjacentes à lista de posições originais
                
    if len(posicoes_originais) != 0:  #Se houver posições adjacentes
        return ordena_posicoes(posicoes_originais, obtem_numero_orbitas(tabuleiro))[0]
    if len(posicoes_livres) != 0:  #Se não houver posições adjacentes
        return ordena_posicoes(posicoes_livres, obtem_numero_orbitas(tabuleiro))[0]

def estratégia_normal(tabuleiro, pedra, k):
    """ 
    Função que escolhe um movimento automático para o computador, de acordo com o nível de dificuldade normal.
    Jogar para vencer: Caso exista uma posição onde é possível formar uma linha com L pedras consecutivas do próprio jogador 
    ao final do turno, deve-se jogar nessa posição para garantir a vitória
    Bloquear o adversário: Se não houver nenhuma posição que permita vencer imediatamente, a estratégia deve ser jogar em uma 
    posição que impeça o adversário de completar uma linha com L pedras consecutivas no final do próximo turno.
    tabuleiro x pedra x int → str
    """
    posicoes_maq = ()
    posicoes_adv = ()

    for l in range(k, 0, -1):
        for posicao in obtem_posicoes_pedra(tabuleiro, 0):
            tabuleiro_copia = cria_copia_tabuleiro(tabuleiro) #Para não modificar o tabuleiro original
            pedra_seguinte1 = obtem_posicao_seguinte(tabuleiro_copia, posicao, False)  #Obtém a posição seguinte
            roda_tabuleiro(tabuleiro_copia) #Roda o tabuleiro
            pedra_seguinte2 = obtem_posicao_seguinte(tabuleiro_copia, pedra_seguinte1, False)  #Obtém a posição seguinte à posição seguinte
            coloca_pedra(tabuleiro_copia, pedra_seguinte1, pedra) #Coloca a pedra na posição seguinte

            if verifica_linha_pedras(tabuleiro_copia, pedra_seguinte1, pedra, l):
                return posicao  #Adiciona a posição à lista de posições da máquina
        
            roda_tabuleiro(tabuleiro_copia)  #Roda o tabuleiro de novo, para simular o tabuleiro da jogada do adversário
            coloca_pedra(tabuleiro_copia, pedra_seguinte2, -pedra)  #Coloca a pedra do adversário na posição seguinte à posição seguinte
            
            if verifica_linha_pedras(tabuleiro_copia, pedra_seguinte2, -pedra, l):
                posicoes_adv += (posicao,)  #Adiciona a posição à lista de posições do adversário
                
        if len(posicoes_adv) != 0:
            return ordena_posicoes(posicoes_adv, obtem_numero_orbitas(tabuleiro))[0]  #Ordena as posições do adversário
        
        
def orbito(orb, lvl, pedra_str):
    """ 
    Função principal que inicia o jogo Orbito, de acordo com os argumentos dados.
    A função chama as funções auxiliares singleplayer e multiplayer, de acordo com o nível de 
    dificuldade escolhido, executando assim o jogo.
    int x str x str → int
    """
    if isinstance(orb, int) and isinstance(pedra_str, str) and isinstance(lvl, str):
        if 2<=orb<=5 and pedra_str in ("X", "O") and lvl in ("facil", "normal","2jogadores"):
            tabuleiro_vazio = cria_tabuleiro_vazio(orb)
            print(f"Bem-vindo ao ORBITO-{orb}.")
            if lvl in ("facil", "normal"):
                return singleplayer(tabuleiro_vazio, pedra_str, lvl)  #Chama a função singleplayer
            else:
                return multiplayer(tabuleiro_vazio, pedra_para_int(pedra_str)) #Chama a função multiplayer
    raise ValueError('orbito: argumentos invalidos')

def singleplayer(tabuleiro, pedra, lvl):
    """ 
    Função auxiliar que inicia o jogo singleplayer, de acordo com o nível de dificuldade escolhido.
    tabuleiro x pedra x str → int
    """
    print(f"Jogo contra o computador ({lvl}).\nO jogador joga com '{pedra}'.")
    print(tabuleiro_para_str(tabuleiro))
    
    if pedra == "X":
        valor = cria_pedra_preta()
    
    if pedra == "O":
        valor = cria_pedra_branca()

    return resto_singleplayer(tabuleiro, pedra_para_int(pedra), valor, lvl)

def resto_singleplayer(tabuleiro, pedra, valor, lvl):
    """ 
    Função auxiliar que executa o jogo singleplayer até ao seu fim, de acordo com o nível de dificuldade escolhido.
    tabuleiro x pedra x int x str → int
    """
    while not eh_fim_jogo(tabuleiro):
        if pedra == cria_pedra_preta():
            print("Turno do jogador.")
            jogada_humana = escolhe_movimento_manual(tabuleiro)  #Jogada do jogador
            coloca_pedra(tabuleiro, str_para_posicao(jogada_humana), valor)
            roda_tabuleiro(tabuleiro)
            print(tabuleiro_para_str(tabuleiro))
            
            if eh_fim_jogo(tabuleiro):   # Verifica se o jogo terminou
                break
        
        if pedra == cria_pedra_branca():
            jogada_maquina = escolhe_movimento_auto(tabuleiro, -valor, lvl)  #Jogada da máquina
            coloca_pedra(tabuleiro, jogada_maquina, -valor)
            print(f"Turno do computador ({lvl}):")
            roda_tabuleiro(tabuleiro) 
            print(tabuleiro_para_str(tabuleiro))
    
            if eh_fim_jogo(tabuleiro):   # Verifica se o jogo terminou
                break
        
        pedra = -pedra   # Alterna entre o jogador e a máquina
    
    if eh_vencedor(tabuleiro, valor):  # Verifica se a máquina ganhou/humano perdeu
        print("VITORIA")
        return valor
    
    elif eh_vencedor(tabuleiro, -valor):
        print("DERROTA")
        return -valor
    
    print("EMPATE")
    return 0

def multiplayer(tabuleiro, pedra):
    """ 
    Função auxiliar que inicia e executa até ao fim o jogo multiplayer, para dois jogadores.
    tabuleiro x str → int
    """
    print("Jogo para dois jogadores.")
    print(tabuleiro_para_str(tabuleiro))
    valor = pedra
    while not eh_fim_jogo(tabuleiro):  #Enquanto o jogo não terminar, os jogadores vão alternando
        print(f"Turno do jogador '{pedra_para_str(valor)}'.")
        jogada_humana = escolhe_movimento_manual(tabuleiro)
        coloca_pedra(tabuleiro, str_para_posicao(jogada_humana), valor)
        roda_tabuleiro(tabuleiro)
        print(tabuleiro_para_str(tabuleiro))
        
        if eh_fim_jogo(tabuleiro):   #Verifica se o jogo terminou
            break

        valor = -valor   #Alterna entre os jogadores
        
    if eh_vencedor(tabuleiro, pedra):
        print(f"VITORIA DO JOGADOR '{pedra_para_str(pedra)}'")
        return pedra
    if eh_vencedor(tabuleiro, -pedra):
        print(F"VITORIA DO JOGADOR '{pedra_para_str(-pedra)}'")
        return -pedra
    
    print("EMPATE")
    return 0


