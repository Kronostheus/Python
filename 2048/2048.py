          #    PROJECTO II - FUNDAMENTOS DA PROGRAMACAO    #
          # ---------------------------------------------- #
          #              Joel Almeida   81609              #
          #              Nuno Amaro     81824              #
          # ---------------------------------------------- #

from random import random

#Funcao construtora do tipo coordenada
def cria_coordenada(l, c):
    """ Esta funcao recebe dois inteiros, respectivamente, o da linha e o da coluna
    e devolve uma coordenada valida para o nosoo jogo"""
    if not isinstance(l, int) or not isinstance(c, int) or l not in range(1,5) or c not in range(1,5):
        raise ValueError ('cria_coordenada: argumentos invalidos')
    else:
        return (l,c)

#Funcao seletora que retorna a linha de uma coordenada
def coordenada_linha(coord):
    return coord[0]

#Funcao seletora que retorna a coluna de uma coordenada
def coordenada_coluna(coord):
    return coord[1]

#Funcao reconhecedora que determina se uma variavel e do tipo coordenada
def e_coordenada(c):
    """ Para que uma dada coordenada seja valida para o nosso jogo ela devera ter
    ser um tuplo com dois inteiros compreendidos entre 1 e 4"""
    return isinstance(c, tuple) and len(c) == 2 and isinstance(c[0], int) and isinstance(c[1], int) and c[0] in range(1, 5) and c[1] in range(1, 5)

#Funcao de teste que determina se uma coordenada e igual a outra, sendo ambas validas
def coordenadas_iguais(C1, C2):
    return e_coordenada(C1) and e_coordenada(C2) and C1 == C2

#Funcao construtora que cria um elemento do tipo tabuleiro
def cria_tabuleiro():
    # Decidimos usar uma representacao interna em dicionarios no nosso jogo
    return {'tab': [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]],
            'pont': 0}

#Funcao reconhecedora que devolve o elemento do tabuleiro numa determinada corrdenada
def tabuleiro_posicao(t, c):
    if not e_coordenada(c) :
        raise ValueError ('tabuleiro_posicao: argumentos invalidos')
    else :
        return t['tab'][coordenada_linha(c)-1][coordenada_coluna(c)-1]

#Funcao reconhecedora que devolve a pontuacao de um tabuleiro
def tabuleiro_pontuacao(t):
    return t['pont']

#Funcao reconhecedora que retorna as posicoes vazias de um tabuleio
def tabuleiro_posicoes_vazias(t):
    """Percorre uma coordenada de cada vez, comecando na primeira linha, 
    verificando se o valor da coordenada e zero."""
    lst = []
    for l in range(1, 5) :
        for c in range(1, 5) :
            if tabuleiro_posicao(t, cria_coordenada(l, c)) == 0 :
                lst = lst + [cria_coordenada(l, c)]
    return lst

#Funcao modificadora que atualiza o valor existente numa posicao
def tabuleiro_preenche_posicao(t, c, v):
    if not e_coordenada(c) or not isinstance(v, int) :
        raise ValueError ('tabuleiro_preenche_posicao: argumentos invalidos')
    else:
        t['tab'][coordenada_linha(c)-1][coordenada_coluna(c)-1] = v
        return t

#Funcao modificadora que atualiza a pontuacao de um tabuleiro
def tabuleiro_actualiza_pontuacao(t, v):
    """De acordo com as regras do jogo 2048, qualquer valor sera positivo 
    e multiplo de 4"""
    if not isinstance(v, int) or v < 0 or v % 4 != 0 :
        raise ValueError ('tabuleiro_actualiza_pontuacao: argumentos invalidos')
    else :
        t['pont'] = t['pont'] + v
        return t

def tabuleiro_reduz(t, d):
    if d not in ('N', 'S', 'W', 'E'):
        raise ValueError ('tabuleiro_reduz: argumentos invalidos')
    else :
        """Consoante a direccao introduzida, esta funcao precorre todos os 
        tabuleiro pela ordem correspondente a ela, somando depois cada elemento
        a sua posicao seguinte. As posicoes que, para cada direccao, nao tem elementos seguintes
        (exemplo: primeira linha quando se reduz para Norte) sao ignoradas."""
        
        ranges = {'N': (range(2, 5), range(1, 5)), 'W': (range(1, 5), range(2, 5)), 'S': (range(3, 0, -1), range(4, 0, -1)), 'E': (range(4, 0, -1), range(3, 0, -1))}
        
        """Como a funcao auxiliar soma_posicoes verifica duas posicoes
        seguintes, movemos todas as posicoes ocupadas antes de proceder aos 
        calculos, para que nao existam posicoes vazias intermedias."""
        t = move_posicoes(t, d)        
        """A funcao verifica as posicoes, soma as que sao possiveis de somar e 
        so depois as junta na direccao escolhida"""
        for l in ranges[d][0] :
            for c in ranges[d][1] :
                t = soma_posicoes(t, cria_coordenada(l, c), d)        
        """Movemos uma ultima vez as posicoes, ja com os calculos feitos, para 
        dispor a jogada ao jogador."""
        t = move_posicoes(t, d)
        return t

def soma_posicoes(t, coord, direcao) :
    """Funcao auxiliar a tabuleiro_reduz que verifica duas posicoes durante 
    um movimento e soma-as se forem iguais."""
    posicoes = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    coord_seg = cria_coordenada(coordenada_linha(coord)+posicoes[direcao][0], coordenada_coluna(coord)+posicoes[direcao][1])
    if e_coordenada(coord_seg) :
        pos = tabuleiro_posicao(t, coord)
        pos_seg = tabuleiro_posicao(t, coord_seg)
        if pos == pos_seg :
            # Soma os valores das duas posicoes
            tabuleiro_preenche_posicao(t, coord_seg, pos + pos_seg)
            # Poe a coordenada anterior a zero
            tabuleiro_preenche_posicao(t, coord, 0)
            # Actualiza a pontuacao para a correcta, depois da soma
            tabuleiro_actualiza_pontuacao(t, pos*2)
    return t

def move_posicoes(t, direcao) :
    """Funcao auxiliar a tabuleiro_reduz que movimenta todas as posicoes 
    ocupadas para uma mesma direcao."""
    operacoes = {'N': (1, 0, range(3, 0, -1), range(1, 5)), 'S': (-1, 0, range(2, 5), range(1, 5)), 'W': (0, 1, range(1, 5), range(1, 4)), 'E': (0, -1, range(1, 5), range(4, 1, -1))}
    for i in range(3) :
        for l in operacoes[direcao][2] :
            for c in operacoes[direcao][3] :
                coord = cria_coordenada(l, c)
                if tabuleiro_posicao(t, coord) == 0 :
                    """ Move os valores caso haja posicoes nulas intermedias,
                    consoante a direccao escolhida""" 
                    tabuleiro_preenche_posicao(t, coord, tabuleiro_posicao(t, cria_coordenada(l+operacoes[direcao][0], c+operacoes[direcao][1])))
                    # Reinicia a posicao de onde o valor se moveu para zero
                    tabuleiro_preenche_posicao(t, cria_coordenada(l+operacoes[direcao][0], c+operacoes[direcao][1]), 0)
    return t

def e_tabuleiro (t) :
    """Esta funcao verifica se o seu argumento esta representado em 
        forma de dicionario, contem a pontuacao (numero inteiro) e tem o tabuleiro 
        em forma de lista de acordo com a especificacao da funcao cria_tabuleiro"""    
    tabuleiro = True   # Parte-se do principio que o tabuleiro inserido e valido, testando-o para confirmar 
    if isinstance(t, dict) and isinstance(t['pont'], int) and isinstance(t['tab'], list) and len(t['tab']) == 4 :
        for l in range(4) :   
            if len(t['tab'][l]) == 4 :  # Verifica se ha 4 colunas
                for c in range(4) :
                    # Verifica se todas as posicoes contem numeros inteiros maiores ou iguais a zero
                    if not isinstance(t['tab'][l][c], int) or t['tab'][l][c] < 0 :  
                        tabuleiro = False
            else :
                tabuleiro = False
    else :
        tabuleiro = False
    return tabuleiro

def tabuleiro_terminado (t) :
    """Funcao que verifica se nao existem mais posicoes vazias, no caso 
    afirmativo copia o tabuleiro e, na copia, efectua todos os movimentos
    possiveis. Caso a copia ser igual ao original, nao ha jogadas possiveis,
    estando assim o tabuleiro terminado."""
    if len(tabuleiro_posicoes_vazias(t)) == 0 :
        pos = ('W', 'E', 'N', 'S')
        t2 = copia_tabuleiro(t)
        for i in pos :
            tabuleiro_reduz(t2, i)
        return t2 == t
    else :
        return False

def tabuleiros_iguais(t1, t2) :
    # Verifica se os tabuleiros sao ambos validos e iguais
    return e_tabuleiro(t1) and e_tabuleiro(t2) and t1 == t2

def escreve_tabuleiro (t) :
    # Funcao que imprime o formato do tabuleiro de jogo 
    if not e_tabuleiro(t) :
        raise ValueError('escreve_tabuleiro: argumentos invalidos')
    else :
        escreve = ''
        for l in range(1, 5) :
            for c in range(1, 5) :
                # Junta linha do tabuleiro
                escreve = escreve + '[ ' + str(tabuleiro_posicao(t, cria_coordenada(l, c))) + ' ] '
            # Move linha seguinte para baixo 
            escreve = escreve + '\n'
        # Escreve tabuleiro e a pontuacao actual
        print(escreve + 'Pontuacao: ' + str(tabuleiro_pontuacao(t)))

def pede_jogada() :
    # Funcao que pede ao jogador que insira uma direccao para a jogada
    d = ''
    while d not in ('N', 'S', 'E', 'W') :
        d = input('Introduza uma jogada (N, S, E, W): ')
        if d not in ('N', 'S', 'E', 'W') :
            print('Jogada invalida.')
    return d

def preenche_posicao_aleatoria(t) :
    """Funcao que guarda numa variavel a lista de posicoes vazias e
    preenche uma delas com 2 (80% de probabilidade) ou 4 (20% probabilidade)"""
    posicoes_vazias = tabuleiro_posicoes_vazias(t)
    if random() < 0.8 :
        tabuleiro_preenche_posicao(t, posicoes_vazias[int(random()*len(posicoes_vazias)-1)], 2)
    else :
        tabuleiro_preenche_posicao(t, posicoes_vazias[int(random()*len(posicoes_vazias)-1)], 4)
    return t

def copia_tabuleiro(t) :
    """Funcao que ao receber um tabuleiro percorre todas as suas coordenadas
    e insere todas as suas posicoes num novo tabuleiro, fazendo assim uma copia 
    do original"""
    t_copia = cria_tabuleiro()
    for l in range(1, 5) :
        for c in range(1, 5) :
            tabuleiro_preenche_posicao(t_copia, cria_coordenada(l, c), tabuleiro_posicao(t, cria_coordenada(l, c)))
    tabuleiro_actualiza_pontuacao(t_copia, tabuleiro_pontuacao(t))
    return t_copia

def jogo_2048() :
    """Funcao principal do nosso jogo que utiliza as anteriormente definidas
    para construir o jogo 2048."""
    t = cria_tabuleiro()    # cria um tabuleiro com todas as posicoes a zero
    # Preenche tabuleiro recem criado com dois valores (2 ou 4) em posicoes aleatorias
    preenche_posicao_aleatoria(t)
    preenche_posicao_aleatoria(t)
    # Jogo corre enquanto o tabuleiro nao ser considerado como terminado
    while not tabuleiro_terminado(t) :
        t_copia = copia_tabuleiro(t)
        escreve_tabuleiro(t)
        tabuleiro_reduz(t, pede_jogada())
        """ Se o tabuleiro for igual ao que estava antes da reducao, nao gerar
            uma posicao aleatoria e continua a pedir uma nova jogada."""        
        if not tabuleiros_iguais(t, t_copia) :
            preenche_posicao_aleatoria(t)