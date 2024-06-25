def calcular_resultados():
    # Obter os valores inseridos pelo usuário
    valor_credito = float(input("Valor de Crédito: "))
    prazo = int(input("Prazo (meses): "))
    taxa_admin = float(input("Taxa Administrativa (%): "))
    fundo_reserva = float(input("Fundo Reserva (%): "))
    lance_embutido = float(input("Lance Embutido (%): "))
    lance_recurso_proprio = float(input("Lance Recurso Próprio: "))

    # Passo 1
    valor_categoria = valor_credito + (valor_credito * taxa_admin / 100) + (valor_credito * fundo_reserva / 100)

    # Passo 2
    valor_lance_embutido = round((lance_embutido / 100) * valor_categoria, 2)  # Convertendo para moeda e arredondando

    # Passo 3
    valor_lance_total = round(valor_lance_embutido + lance_recurso_proprio, 2)

    # Passo 4
    credito_liquido = round(valor_credito - valor_lance_embutido, 2)

    # Passo 6
    saldo_devedor = round(valor_categoria - (lance_embutido + lance_recurso_proprio), 2)

    # Passo 7
    percentual_lance_recurso_proprio = round((lance_recurso_proprio / valor_credito) * 100, 2)  # Convertendo para porcentagem e arredondando

    # Passo 8
    lance_total = round(lance_embutido + percentual_lance_recurso_proprio, 2)

    # Passo 9
    parcela_inicial = round(valor_categoria / prazo, 2)

    # Passo 10
    parcela_pos_contemplacao = round((valor_categoria - valor_lance_total) / prazo, 2)

    # Exibir resultados no terminal
    print(f"\nValor de Crédito: {valor_credito:.2f}")
    print(f"Parcela Inicial: {parcela_inicial:.2f}")
    print(f"Lance Total: {lance_total:.2f}%")
    print(f"Crédito Liquido: {credito_liquido:.2f}")
    print(f"Parcela Pós Contemplação: {parcela_pos_contemplacao:.2f}")

# Calcular resultados
calcular_resultados()
