def calcular_resultados():
    # Obter os valores inseridos pelo usuário
    valor_credito = float(input("Valor de Crédito: "))
    prazo = int(input("Prazo (meses): "))
    taxa_admin = float(input("Taxa Administrativa (%): "))
    fundo_reserva = float(input("Fundo Reserva (%): "))
    lance_embutido = float(input("Lance Embutido (%): "))
    lance_recurso_proprio = float(input("Lance Recurso Próprio: "))

    # Passo 1
    saldo_devedor = valor_credito + (valor_credito * taxa_admin / 100) + (valor_credito * fundo_reserva / 100)

    # Passo 2
    parcela_inicial = saldo_devedor / prazo

    # Passo 3
    valor_credito_diluido = (valor_credito / prazo) * 100

    # Passo 4
    taxa_admin_diluida = taxa_admin / prazo

    # Passo 5
    fundo_reserva_diluido = fundo_reserva / prazo

    # Passo 6
    valor_lance_embutido = (lance_embutido / 100) * valor_credito

    # Passo 7
    credito_liquido = valor_credito - valor_lance_embutido

    # Passo 8
    lance_total = valor_lance_embutido + lance_recurso_proprio

    # Passo 9
    prazo_reduzido = prazo - 1
    parcela_reduzida = lance_total / prazo_reduzido

    # Passo 10
    parcela_pos_contemplacao = parcela_inicial - parcela_reduzida

    # Passo 11
    lance_total_porcentagem = (lance_total / saldo_devedor) * 100

    # Passo 12
    seguro = 0.0007 * saldo_devedor

    # Calcular parcelas com seguro
    parcela_com_seguro_inicial = parcela_inicial + seguro
    parcela_com_seguro_pos_contemplacao = parcela_pos_contemplacao + seguro

    # Exibir resultados no terminal
    print(f"\nValor de Crédito: R${valor_credito:.2f}")
    print(f"Parcela Inicial: R${parcela_inicial:.2f}")
    print(f"Parcela com Seguro: R${parcela_com_seguro_inicial:.2f}")
    print(f"Lance Total: {lance_total_porcentagem:.2f}%")
    print(f"Crédito Liquido: R${credito_liquido:.2f}")
    print(f"Parcela Pós Contemplacao: R${parcela_pos_contemplacao:.2f}")
    print(f"Parcela com Seguro: R${parcela_com_seguro_pos_contemplacao:.2f}")

# Calcular resultados
calcular_resultados()
