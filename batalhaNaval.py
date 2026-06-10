import random

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


# os atque tem q ser pro tab oposto

def ataqueMaquina():
    contadorAcertosMaquina = 5
    X = random.randint(0,9)
    Y = random.randint(0,9)
    if tabuleiroJogadorVisivel[X][Y] == 0:
        if tabuleiroJogadorReal[X][Y]== 1:
            tabuleiroJogadorVisivel[X][Y] = 'X'
            contadorAcertosMaquina -= 1
        else:
            tabuleiroJogadorVisivel[X][Y] = 'O'

def ataqueJogador():
    contadorAcertosJogador = 5
    X = int(input('digite a linha de 0 a 9:  '))
    Y = int(input('digite a coluna de 0 a 9:  '))
    if X >=0 and X <=9 and Y >=0 and Y <=9:
        if tabuleiroMaquinaVisivel[X][Y] == 0:
            if tabuleiroMaquinaReal[X][Y] == 1:
                print('Você acertou um barco')
                tabuleiroMaquinaVisivel[X][Y] = 'X'
                contadorAcertosJogador -= 1
            else:
                print('Você nao acertou nenhum barco')
                tabuleiroMaquinaVisivel[X][Y] = 'O'      
        else: 
            print('essa posicao ja foi atacada')
    else:
        print('coordenada invalida')
    
            



















        
#chama criacao de tab + barcos + ataques/ chama o que e mostrado mostrarTabuleiro(tabuleiroJogadorVisivel), mostrarTabuleiro(tabuleiroMaquinaVisivel) (sem barcos)
tabuleiroJogadorVisivel = criarTab()
tabuleiroJogadorReal = criarTab()

tabuleiroMaquinaVisivel = criarTab()
tabuleiroMaquinaReal = criarTab()

colocarBarcosJogador()
colocarBarcosRobo()
 
ataqueJogador()
ataqueMaquina()
