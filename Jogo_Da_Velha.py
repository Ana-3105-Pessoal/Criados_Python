import random

def mostrar_tabuleiro(jogo):
    """
    Exibe o tabuleiro do Jogo da Velha formatado no terminal.

    Args:
        jogo (list): Uma lista de listas 3x3 representando o tabuleiro.
    """
    for linha in range(3):
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print(f'|   {jogo[linha][0]}   |   {jogo[linha][1]}   |   {jogo[linha][2]}   |')
        print('|       |       |       |')
    print('+-------+-------+-------+')
    
def jogada_usuario(jogo):
    """
    Solicita a jogada do usuário, valida a entrada e atualiza o tabuleiro.

    A função continuará pedindo uma jogada até que o usuário insira um
    número válido (1-9) correspondente a um campo livre no tabuleiro.

    Args:
        jogo (list): A lista de listas 3x3 representando o tabuleiro.
                     Esta lista é modificada diretamente pela função.
    """
    while True:
        try:
            jogada = int(input('Digite sua jogada (1-9): '))
        except ValueError:
            print('Entrada invalida! Digite um número.')
            continue
        if jogada < 1 or jogada > 9:
            print('Entrada invalida! Escolha um número entre 1 e 9.')
            continue
        linha = (jogada - 1) // 3
        coluna = (jogada - 1) % 3
        if jogo[linha][coluna] in ['X','O']:
            print('Este campo está ocupado. Tente outro.')
            continue
        jogo[linha][coluna] = 'O'
        break
        
def lista_campos_livres(jogo):
  """
  Verifica o tabuleiro e retorna uma lista com as coordenadas dos campos vazios.

  Args:
      jogo (list): A lista de listas 3x3 representando o tabuleiro.

  Returns:
      list: Uma lista de tuplas, onde cada tupla é uma coordenada (linha, coluna)
            de um campo livre.
  """
  campos_livres = []
  for linha in range(3):
      for coluna in range(3):
          if jogo[linha][coluna] not in ['X','O']:
              campos_livres.append((linha,coluna))
  return campos_livres
    
def verificar_vitoria(jogo,simbolo):
    """
    Verifica se um jogador venceu o jogo.

    Analisa todas as 8 possíveis condições de vitória (3 linhas, 3 colunas e 2 diagonais)
    para o símbolo fornecido.

    Args:
        jogo (list): A lista de listas 3x3 representando o tabuleiro.
        simbolo (str): O símbolo do jogador a ser verificado ('X' ou 'O').

    Returns:
        bool: True se o jogador com o símbolo venceu, False caso contrário.
    """
    for i in range(3):
        if jogo[i][0] == simbolo and jogo[i][1] == simbolo and jogo[i][2] == simbolo:
            return True
    for i in range(3):
        if jogo[0][i] == simbolo and jogo[1][i] == simbolo and jogo[2][i] == simbolo:
            return True
    if jogo[0][2] == simbolo and jogo[1][1] == simbolo and jogo[2][0] == simbolo:
        return True
    if jogo[0][0] == simbolo and jogo[1][1] == simbolo and jogo[2][2] == simbolo:
        return True
    return False
    
def jogada_computador(jogo):
    """
    Realiza a jogada do computador escolhendo um campo livre aleatoriamente.

    Args:
        jogo (list): A lista de listas 3x3 representando o tabuleiro.
                     Esta lista é modificada diretamente pela função.
    """
    campos_livres = lista_campos_livres(jogo)
    escolha_jogada = random.choice(campos_livres)
    linha = escolha_jogada[0]
    coluna = escolha_jogada[1]
    jogo[linha][coluna] = 'X'

# --- Bloco Principal do Jogo ---
# Este bloco é executado quando o script é iniciado diretamente.
if __name__ == '__main__':
    # Cria o tabuleiro inicial com números de 1 a 9
    tabuleiro = [[3 * linha + coluna + 1 for coluna in range(3)] for linha in range(3)]
    
    # O computador sempre começa no meio para ter um jogo mais interessante
    tabuleiro[1][1] = 'X'
    
    turno_usuario = True
    vencedor = None
    
    # O loop principal do jogo continua enquanto houver campos livres
    while len(lista_campos_livres(tabuleiro)) > 0:
        mostrar_tabuleiro(tabuleiro)
        if turno_usuario:
            print('É sua vez!')
            jogada_usuario(tabuleiro)
            if verificar_vitoria(tabuleiro,'O'):
                vencedor = 'Usuário'
                break
        else:
            print('É a vez do computador!')
            jogada_computador(tabuleiro)
            if verificar_vitoria(tabuleiro,'X'):
                vencedor = 'Computador'
                break
        # Alterna o turno
        turno_usuario = not turno_usuario

    # Exibe o tabuleiro final e o resultado
    mostrar_tabuleiro(tabuleiro)
    if vencedor == 'Computador':
        print('Eu ganhei!')
    elif vencedor == 'Usuário':
        print('Você ganhou!Parabéns!')
    else:
        print('Empate!')

