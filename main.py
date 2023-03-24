from Jogo import Jogo


def main() -> None:

    jogo = Jogo()
    sair = False

    while True:
        jogo.iniciar()

        if input("\n\tJogoar de novo? [s - sim, outra - nao]: ").lower() != 's':
            break

    jogo.imprimir_pontuacao()
    print("\n\t** FIM **")


if __name__ == "__main__":
    main()
