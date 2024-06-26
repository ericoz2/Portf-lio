ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.

# Ordenar a lista de ativos
ativos.sort()

# Exibir os ativos ordenados
for ativo in ativos:
    print(ativo)