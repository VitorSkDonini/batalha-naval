import random

def criarTab():
    tabReal= []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabReal.append(linha)
    return tabReal

def tabuleiroVisivel(tabuleiroReal):
    for i in tabuleiroReal:
        for onda in i:
            if onda == 0:
                print('🌊', end= ' ')
            elif onda == 1:
                print('🚢', end= ' ')
        print()
    

def colocarBarcosJogador():
    for barcos in range(5):
        tabuleiroReal.insert(1)

tabuleiroReal = criarTab()
tabuleiroJogador = criarTab()
tabuleiroMaquina = criarTab()

tabuleiroVisivel(tabuleiroReal)