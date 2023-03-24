from typing import List
from Tabuleiro import Tabuleiro
from Jogador import Jogador
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


class Jogo:
    pontuacao: dict[str, int]
    jogadores: List[Jogador]
    tab: Tabuleiro

    def __init__(self):
        self.jogadores = [Jogador(), Jogador()]
        self.tab = Tabuleiro()

        print("\n\tJogador 1 - Insira o seu nome: ", end="")
        self.jogadores[0].nome = f"\033[91m{input().upper()}\033[0m"
        self.jogadores[0].simbolo = 'X'

        print("\n\tJogador 2 - Insira o seu nome: ", end="")
        self.jogadores[1].nome = f"\033[94m{input().upper()}\033[0m"
        self.jogadores[1].simbolo = 'O'

        self.pontuacao = {
            self.jogadores[0].nome: 0,
            self.jogadores[1].nome: 0
        }

    def iniciar(self):
        self.tab.iniciar_tabuleiro()
        num_jogadas = 0

        while num_jogadas < 9:
            limpar_tela()
            self.imprimir_pontuacao()
            
            self.tab.imprimir_tabuleiro()

            jogador_actual = self.jogadores[num_jogadas % 2]

            pos = int(
                input(f"\n\t{jogador_actual.nome} Insira a posicao onde deseja jogar: "))

            while pos <= 0 or pos >= 10 or self.tab.posicao_ocupada(pos):
                print("\n\tPosicao invalida, tenta novamente")
                pos = int(
                    input(f"\n\t{jogador_actual.nome} Insira a posicao onde deseja jogar: "))

            self.tab.marcar_jogada(pos, jogador_actual.simbolo)
            num_jogadas += 1

            if num_jogadas >= 5:
                if self.tab.verificar_se_ganhou(jogador_actual.simbolo):
                    self.pontuacao[jogador_actual.nome] += 1
                    self.tab.imprimir_tabuleiro()
                    print(f"\n\t{jogador_actual} Ganhou!")
                    break

        if num_jogadas == 9:
            print("\n\tEmpate!")

    def imprimir_pontuacao(self):
        print("\n\tPontuacao:")
        for j, p in self.pontuacao.items():
            print(f"\t\t{j}: {p}")
