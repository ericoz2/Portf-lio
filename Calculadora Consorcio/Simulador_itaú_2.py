class CalculadoraCredito:
    def __init__(self):
        # Inicializa os atributos da instância
        self.valor_credito = 0.0
        self.prazo = 0
        self.taxa_admin = 0.0
        self.fundo_reserva = 0.0
        self.lance_embutido = 0.0
        self.lance_recurso_proprio = 0.0

    def obter_valores(self):
        # Obtém os valores inseridos pelo usuário
        self.valor_credito = float(input("Valor de Crédito: "))
        self.prazo = int(input("Prazo (meses): "))
        self.taxa_admin = float(input("Taxa Administrativa (%): "))
        self.fundo_reserva = float(input("Fundo Reserva (%): "))
        self.lance_embutido = float(input("Lance Embutido (%): "))
        self.lance_recurso_proprio = float(input("Lance Recurso Próprio: "))

    def calcular_resultados(self):
        # Passo 1
        valor_categoria = self.valor_credito + (self.valor_credito * self.taxa_admin / 100) + (self.valor_credito * self.fundo_reserva / 100)

        # Passo 2
        valor_lance_embutido = round((self.lance_embutido / 100) * valor_categoria, 2)  # Convertendo para moeda e arredondando

        # Passo 3
        valor_lance_total = round(valor_lance_embutido + self.lance_recurso_proprio, 2)

        # Passo 4
        credito_liquido = round(self.valor_credito - valor_lance_embutido, 2)

        # Passo 6
        saldo_devedor = round(valor_categoria - (self.lance_embutido + self.lance_recurso_proprio), 2)

        # Passo 7
        percentual_lance_recurso_proprio = round((self.lance_recurso_proprio / self.valor_credito) * 100, 2)  # Convertendo para porcentagem e arredondando

        # Passo 8
        lance_total = round(self.lance_embutido + percentual_lance_recurso_proprio, 2)

        # Passo 9
        parcela_inicial = round(valor_categoria / self.prazo, 2)

        # Passo 10
        parcela_pos_contemplacao = round((valor_categoria - valor_lance_total) / self.prazo, 2)

        # Exibir resultados no terminal
        print(f"\nValor de Crédito: {self.valor_credito:.2f}")
        print(f"Parcela Inicial: {parcela_inicial:.2f}")
        print(f"Lance Total: {lance_total:.2f}%")
        print(f"Crédito Liquido: {credito_liquido:.2f}")
        print(f"Parcela Pós Contemplação: {parcela_pos_contemplacao:.2f}")

# Criar uma instância da classe
calculadora = CalculadoraCredito()

# Obter valores e calcular resultados
calculadora.obter_valores()
calculadora.calcular_resultados()
