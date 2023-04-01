from typing import List, Tuple

"""
    Vou utilizaar numeros para representar 
    as posicoes do tabuleiro, para facilitar o utilizador, 
    que provavelmente nao percebe nada de matrizes

     1 | 2 | 3  
    ---+---+---
     4 | 5 | 6 
    ---+---+---
     7 | 8 | 9
"""


class Tabuleiro:
    __tab: List[List[str]]

    def iniciar_tabuleiro(self) -> None:
        self.__tab = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
        ]

    def marcar_jogada(self, pos: int, simbolo: str) -> None:
        """
        Marca a jogada de um jogador no tabuleiro

        Args:
            pos (int): A posicao escolhida pelo utilizador
            simbolo (str): Simbolo, pode ser 'X' ou 'O'
        """
        i, j = self.converter_posicao(pos)
        self.__tab[i][j] = simbolo

    def posicao_ocupada(self, pos: int) -> bool:
        """Verifica se a posicao escolhida se encontra ocupda

        Args:
            pos (int): A posicao escolhida pelo jogador

        Returns:
            bool: True se a posicao estiver ocupada, False caso contrario
        """

        i, j = self.converter_posicao(pos)
        return self.__tab[i][j] in ('X', 'O')

    def converter_posicao(self, pos: int) -> Tuple[int]:
        """
        Converte a posicao (1, 2, ... 9) para as coordendas (i, j) 
        da matriz 

        Args:
            pos (int): A posicao escolhida pelo jogador

        Returns:
            Tuple[int]: uma tupla com as coordenadas da matriz Ex: (0, 2), (1, 1) ...
        """
        for i in range(3):
            for j in range(3):
                if pos == 1:
                    return (i, j)
                pos -= 1

    def verificar_se_ganhou(self, simbolo: str) -> bool:
        """Verifica se o jogador ganhou o jogo

        Args:
            simbolo (str): o simbolo (X ou O)

        Returns:
            bool: True se existe uma sequencia de 3 simbolos, False caso contrario
        """
        # Horizontal
        for linha in self.__tab:
            if linha.count(simbolo) == 3:
                return True

        # Vertical
        for j in range(3):
            coluna = [x[j] for x in self.__tab]
            if coluna.count(simbolo) == 3:
                return True

        # Diagonal principal
        diagonal_principal = [self.__tab[i][i] for i in range(3)]
        if diagonal_principal.count(simbolo) == 3:
            return True

        # Diagonal secundaria
        diagonal_secundaria = [self.__tab[i][2 - i] for i in range(3)]
        if diagonal_secundaria.count(simbolo) == 3:
            return True

        return False

    def imprimir_tabuleiro(self) -> None:
        s = f"""
         {self.__tab[0][0]} | {self.__tab[0][1]} | {self.__tab[0][2]}  
        ---+---+---
         {self.__tab[1][0]} | {self.__tab[1][1]} | {self.__tab[1][2]} 
        ---+---+---
         {self.__tab[2][0]} | {self.__tab[2][1]} | {self.__tab[2][2]}
        """

        s = s.replace('X', '\033[91mX\033[0m')
        s = s.replace('O', '\033[94mO\033[0m')

        print(s)
