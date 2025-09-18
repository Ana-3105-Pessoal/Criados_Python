import random

def mostrar_tabuleiro(jogo):
    for linha in range(3):
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print(f'|   {jogo[linha][0]}   |   {jogo[linha][1]}   |   {jogo[linha][2]}   |')
        print('|       |       |       |')
    print('+-------+-------+-------+')
def jogada_usuario(jogo):
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
  campos_livres = []
  for linha in range(3):
      for coluna in range(3):
          if jogo[linha][coluna] not in ['X','O']:
              campos_livres.append((linha,coluna))
  return campos_livres
def verificar_vitoria(jogo,simbolo):
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
    campos_livres = lista_campos_livres(jogo)
    escolha_jogada = random.choice(campos_livres)
    linha = escolha_jogada[0]
    coluna = escolha_jogada[1]
    jogo[linha][coluna] = 'X'

if __name__ == '__main__':
    tabuleiro = [[3 * linha + coluna + 1 for coluna in range(3)] for linha in range(3)]
    tabuleiro[1][1] = 'X'
    turno_usuario = True
    vencedor = None
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
        turno_usuario = not turno_usuario

    mostrar_tabuleiro(tabuleiro)
    if vencedor == 'Computador':
        print('Eu ganhei!')
    elif vencedor == 'Usuário':
        print('Você ganhou!Parabéns!')
    else:
        print('Empate!')
