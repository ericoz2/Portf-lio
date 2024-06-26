# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

def recomendar_plano(consumo):
  if consumo >= 20:
    return "Plano Premium Fibra - 300Mbps"

  elif consumo >= 11 and consumo <= 19:
    return "Plano Prata Fibra - 100Mbps"
  
  else:
    return "Plano Essencial Fibra - 50Mbps"

# Solicita ao usuário que insira o consumo médio mensal de dados:
# Infelizmente o testador da plataforam da DIO não consegue lidar com o input
# quando existe alguma mensagem ao usuário, por isso o input está em branco.

# "Digite o seu consumo médio mensal de dados em GB:", deveria estar dentro do
# input
consumo = float(input())

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))