# Saldo inicial da conta (por padrão começando com 0)
saldo = 0.0

valor = float(input())

if valor > 0:
    saldo += valor
    print("Deposito realizado com sucesso!")
    print(f"Saldo atual: R$ {saldo:.2f}")
    
elif valor == 0:
    print("Encerrando o programa...")
else:
    print("Valor invalido! Digite um valor maior que zero.")
 
  
