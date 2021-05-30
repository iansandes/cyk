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

def concatenar_variaveis(valor_a, valor_b):
    resultado = set()
    if valor_a == set() or valor_b == set():
        return set()
    for a in valor_a:
        for b in valor_b:
            resultado.add(a + b)
    return resultado

def cyk(variaveis, terminais, palavra):

    tamanho = len(palavra)
    variaveis_a = [var[0] for var in variaveis]
    variaveis_b = [var[1] for var in variaveis]

    # Montagem da tabela que o algoritmo será utilizada
    tabela = [[set() for _ in range(tamanho - i)] for i in range(tamanho)]

    for i in range(tamanho):
        for terminal in terminais:
            if palavra[i] == terminal[1]:
                tabela[0][i].add(terminal[0])

    for i in range(1, tamanho):
        for j in range(tamanho - i):
            for k in range(i):
                linha = concatenar_variaveis(tabela[k][j], tabela[i - k - 1][j + k + 1])
                for valor in linha:
                    if valor in variaveis_b:
                        tabela[i][j].add(variaveis_a[variaveis_b.index(valor)])

    if 'S' in tabela[len(palavra) - 1][0]:
        print(
            "A palavra '{palavra}' pertence a gramática proposta!".format(palavra= palavra))
    else:
        print("A palavra '{palavra}' NÃO pertence a gramática proposta!".format(
            palavra= palavra))

if __name__ == '__main__':
    variaveis, terminais = ler_gramatica()
    cyk(variaveis, terminais, "aabb")