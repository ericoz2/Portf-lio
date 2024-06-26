def atualizar_saldo(saldo_atual, valor_deposito, valor_retirada):
    # Atualizando o saldo com o valor do depósito
    saldo_atual += valor_deposito
    # Atualizando o saldo com o valor da retirada (subtração)
    saldo_atual -= valor_retirada
    # Retornando o saldo atualizado formatado com uma casa decimal
    return round(saldo_atual, 1)

saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

# Exibindo o saldo atualizado
print(f"Saldo atualizado na conta: {atualizar_saldo(saldo_atual, valor_deposito, valor_retirada)}")