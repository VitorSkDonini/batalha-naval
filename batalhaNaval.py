import random
# cria tabuleiro e troca para ser visivel
def criarTab():
    tabReal= []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabReal.append(linha)
    return tabReal
def tabuleiroVisivel(tabuleiro):
    for i in tabuleiro:
        for onda in i:
            if onda == 0:
                print('🌊', end= ' ')
            elif onda == 1:
                print('🚢', end= ' ')
            elif onda == 'X':
                print('💥', end= ' ')           
            elif onda == 'O':
                print('⭕', end= ' ')               
        print()


def colocarBarcosJogador():
    contadorBarcos = 0
    while contadorBarcos < 5:
        print('Barco', contadorBarcos + 1)
        X = int(input('digite a linha de 0 a 9:  '))
        Y = int(input('digite a coluna de 0 a 9:  '))
        if X >=0 and X <=9 and Y >=0 and Y <=9:
             if tabuleiroJogadorReal[X][Y] == 0:
                tabuleiroJogadorReal[X][Y] = 1
                contadorBarcos += 1
             else:
                print('Ja existe um barco nessa posicao')
        else:
            print('coordenada invalida')
def colocarBarcosRobo():
    contadorBarcos = 0
    while contadorBarcos < 5:
        X = random.randint(0,9)
        Y = random.randint(0,9)
        if tabuleiroMaquinaReal[X][Y] == 0:
            tabuleiroMaquinaReal[X][Y] = 1
            contadorBarcos += 1


# chama os ataques da maquina + jogador (os atque tem q ser pro tab oposto/ acertos retornam valor salvo)

def ataqueMaquina():
    while True:
        X = random.randint(0,9)
        Y = random.randint(0,9)
        if tabuleiroJogadorVisivel[X][Y] == 0:
            if tabuleiroJogadorReal[X][Y]== 1:
                tabuleiroJogadorVisivel[X][Y] = 'X'
                print('A maquina acertou um barco seu')
                return 1
            else:
                tabuleiroJogadorVisivel[X][Y] = 'O'
                print('A maquina errou')
                return 0

def ataqueJogador():
    while True:
        X = int(input('digite a linha de 0 a 9:  '))
        Y = int(input('digite a coluna de 0 a 9:  '))
        if X >=0 and X <=9 and Y >=0 and Y <=9:
            if tabuleiroMaquinaVisivel[X][Y] == 0:
                if tabuleiroMaquinaReal[X][Y] == 1:
                    print('Você acertou um barco')
                    tabuleiroMaquinaVisivel[X][Y] = 'X'
                    return 1
                else:
                    print('Você nao acertou nenhum barco')
                    tabuleiroMaquinaVisivel[X][Y] = 'O'     
                    return 0 
            else: 
                print('essa posicao ja foi atacada')
        else:
            print('coordenada invalida')
    

#chama o jogo(menu e logica do jogo + pontos)
def main():

    print('-----------------------------------------------------------------------------------------------------')
    print('\nBem vindo ao BATALHA NAVAL\n')
    print('Jogar| 1')
    print('fechar| 2\n')
    print('-----------------------------------------------------------------------------------------------------')

    escolha= int(input('escolha uma opcao:\n'))

    barcosJogador = 5
    barcosMaquina = 5
    if escolha == 1:
        colocarBarcosJogador()
        colocarBarcosRobo()
        while barcosJogador > 0 and barcosMaquina > 0:

            print('-----------------------------------------------------------------------------------------------------')
            print('Vez do jogador')
            print('tabuleiro da maquina:')
            tabuleiroVisivel(tabuleiroMaquinaVisivel)
            print('escolha onde atacar:')
            tiroJogador = ataqueJogador()
            tabuleiroVisivel(tabuleiroMaquinaVisivel)
            print('-----------------------------------------------------------------------------------------------------')

            if tiroJogador == 1:
                barcosMaquina -= 1
                print('faltam',barcosMaquina, ' barcos da maquina')
            if barcosMaquina == 0:
                print('PARABENS!!\n Voce venceu')
                break

            print('-----------------------------------------------------------------------------------------------------')
            tiroMaquina = ataqueMaquina() 
            if tiroMaquina == 1 :
                barcosJogador -= 1
                print('faltam',barcosJogador, 'barcos seus')
            if barcosJogador == 0:
                print('PERDEU!!\n A maquina venceu ')
                break
            print('Onde a maquina atacou')
            tabuleiroVisivel(tabuleiroJogadorVisivel)
            print('-----------------------------------------------------------------------------------------------------')

    elif escolha == 2:
         print('-----------------------------------------------------------------------------------------------------')
         print('jogo fechado')
         print('Obrigado por jogar')

    else:
        print('opcao invalida')

# gera matriz do tabuleiro+ carrega jogo
tabuleiroJogadorVisivel = criarTab()
tabuleiroJogadorReal = criarTab()
tabuleiroMaquinaVisivel = criarTab()
tabuleiroMaquinaReal = criarTab()
main()