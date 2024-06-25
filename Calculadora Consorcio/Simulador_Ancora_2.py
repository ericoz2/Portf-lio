def calcular_seguro(saldo_devedor):
    seguro = 0.0007 * saldo_devedor
    return seguro

def main():
    # Entrada de dados
    valor_credito = float(input("Digite o Valor de Crédito: "))
    prazo = int(input("Digite o Prazo em meses: "))
    taxa_administrativa = float(input("Digite a Taxa Administrativa (%): "))
    fundo_reserva = float(input("Digite o Fundo Reserva (%): "))
    lance_embutido = float(input("Digite o Lance Embutido (%): "))
    lance_recurso_proprio = float(input("Digite o Lance Recurso Próprio: "))

    # Passo 1
    saldo_devedor = valor_credito + taxa_administrativa + fundo_reserva

    # Passo 2
    parcela_inicial = saldo_devedor / prazo

    # Passo 3, 4, 5
    valor_credito_diluido = valor_credito / prazo
    taxa_administrativa_diluida = taxa_administrativa / prazo
    fundo_reserva_diluido = fundo_reserva / prazo

    # Passo 6
    lance_embutido_em_moeda = saldo_devedor * (lance_embutido / 100)

    # Passo 7
    credito_liquido = valor_credito - lance_embutido_em_moeda

    # Passo 8
    lance_total = lance_embutido + lance_recurso_proprio

    # Passo 9
    prazo_diluido = prazo - 1

    # Passo 9
    parcela_reduzida = lance_total / prazo_diluido

    # Passo 10
    parcela_pos_contemplacao = parcela_inicial - parcela_reduzida

    # Passo 11
    lance_total_porcentagem = (lance_total / valor_credito) * 100

    # Passo 12
    seguro = calcular_seguro(saldo_devedor)

    # Exibição dos resultados
    print("\nResultados:")
    print("Valor de Crédito: {:.2f}".format(valor_credito))
    print("Parcela Inicial: {:.2f}".format(parcela_inicial))
    print("Parcela com Seguro: {:.2f}".format(parcela_inicial + seguro))
    print("Lance Total: {:.2f} ({}%)".format(lance_total, lance_total_porcentagem))
    print("Crédito Liquido: {:.2f}".format(credito_liquido))
    print("Parcela Pós Contemplação: {:.2f}".format(parcela_pos_contemplacao))
    print("Parcela com Seguro: {:.2f}".format(parcela_pos_contemplacao + seguro))

if __name__ == "__main__":
    main()
