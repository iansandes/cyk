import os


def ler_gramatica(arquivo="./gramatica.txt"):
    arquivo = os.path.join(os.curdir, arquivo)
    with open(arquivo) as gramatica:
        regras = gramatica.readlines()
        variaveis_regras = []
        terminais_regras = []

        for regra in regras:
            variavel, terminal = regra.split(" => ")
            terminal = terminal[:-1].split(" | ")
            for simbolo in terminal:
                if str.islower(simbolo):
                    terminais_regras.append([variavel, simbolo])
                else:
                    variaveis_regras.append([variavel, simbolo])
        return variaveis_regras, terminais_regras


if __name__ == '__main__':
    variaveis, terminais = ler_gramatica()