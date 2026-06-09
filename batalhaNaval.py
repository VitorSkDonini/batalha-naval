import random

def criarTab():
    tabReal= []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabReal.append(linha)
    return tabReal
    
tabuleiroReal = criarTab()
tabuleiroJogador = criarTab()
tabuleiroMaquina = criarTab()

# for i in range(10):
#     for j in range(10):
#         print(tabuleiroReal[i][j], end='  ')
#     print()

