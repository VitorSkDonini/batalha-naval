Batalha Naval
Projeto simples de Batalha Naval em Python, feito para praticar matrizes, funções, estruturas de repetição, condicionais e uso da biblioteca random.
Sobre o jogo
O jogo é uma versão simplificada de Batalha Naval no modo jogador contra máquina.
Cada jogador possui um tabuleiro 10x10. O jogador escolhe manualmente onde posicionar seus barcos, enquanto a máquina posiciona os barcos de forma aleatória.
O objetivo é acertar todos os barcos do adversário antes que ele acerte os seus.
Funcionalidades
Criação de tabuleiros usando matriz.
Posicionamento manual dos barcos do jogador.
Posicionamento aleatório dos barcos da máquina.
Ataques alternados entre jogador e máquina.
Marcação de acertos e erros no tabuleiro.
Contagem de barcos restantes.
Mensagem de vitória ou derrota.
Menu simples para jogar ou fechar o jogo.
Símbolos usados
🌊 = posição ainda não atacada
🚢 = barco
💥 = acerto
⭕ = erro
Como executar
Para executar o jogo, é necessário ter o Python instalado.

estrutura do código:
O código está organizado em funções:
criarTab()
Cria um tabuleiro 10x10 preenchido com zeros.
tabuleiroVisivel()
Mostra o tabuleiro no console usando emojis.
colocarBarcosJogador()
Permite que o jogador escolha as posições dos seus barcos.
colocarBarcosRobo()
Posiciona os barcos da máquina de forma aleatória usando random.
ataqueJogador()
Controla o ataque do jogador contra o tabuleiro da máquina.
ataqueMaquina()
Controla o ataque aleatório da máquina contra o tabuleiro do jogador.
main()
Controla o menu inicial, o funcionamento principal do jogo, os turnos e as condições de vitória ou derrota