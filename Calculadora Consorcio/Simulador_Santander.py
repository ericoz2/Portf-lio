class CalculadoraCredito:
    def __init__(self, valor_credito, prazo, taxa_admin, fundo_reserva, lance_embutido, lance_recurso_proprio):
        self.valor_credito = valor_credito
        self.prazo = prazo
        self.taxa_admin = taxa_admin
        self.fundo_reserva = fundo_reserva
        self.lance_embutido = lance_embutido
        self.lance_recurso_proprio = lance_recurso_proprio

    def calcular_resultados(self):
        # Passo 1
        valor_categoria = self.valor_credito + (self.valor_credito * self.taxa_admin / 100) + (self.valor_credito * self.fundo_reserva / 100)

        # Passo 2
        credito_liquido = round(valor_categoria - (valor_categoria * self.lance_embutido / 100), 2)

        # Passo 3
        saldo_devedor = round(credito_liquido - self.lance_embutido - self.lance_recurso_proprio, 2)

        # Passo 4
        percentual_lance_recurso_proprio = round((self.lance_recurso_proprio / valor_categoria) * 100, 2)

        # Passo 5
        lance_total = round(self.lance_embutido + percentual_lance_recurso_proprio, 2)

        # Passo 6
        parcela_inicial = round(valor_categoria / self.prazo, 2)

        # Passo 7
        parcela_pos_contemplacao = round(saldo_devedor / self.prazo, 2)

        return {
            'valor_credito': round(self.valor_credito, 2),
            'parcela_inicial': parcela_inicial,
            'lance_total': lance_total,
            'credito_liquido': credito_liquido,
            'parcela_pos_contemplacao': parcela_pos_contemplacao
        }

def main():
    # Solicita dados de entrada ao usuário
    valor_credito = float(input("Digite o valor de crédito: R$ "))
    prazo = int(input("Digite o prazo em meses: "))
    taxa_admin = float(input("Digite a taxa administrativa (%): "))
    fundo_reserva = float(input("Digite o fundo de reserva (%): "))
    lance_embutido = float(input("Digite o lance embutido (%): "))
    lance_recurso_proprio = float(input("Digite o valor do lance com recurso próprio: R$ "))

    # Cria uma instância da calculadora
    calculadora = CalculadoraCredito(valor_credito, prazo, taxa_admin, fundo_reserva, lance_embutido, lance_recurso_proprio)

    # Calcula e exibe os resultados na tela
    resultados = calculadora.calcular_resultados()
    print("\nResultados:")
    print("Valor de Crédito: R$ {:.2f}".format(resultados['valor_credito']))
    print("Parcela Inicial: R$ {:.2f}".format(resultados['parcela_inicial']))
    print("Lance Total: {:.2f}%".format(resultados['lance_total']))
    print("Crédito Líquido: R$ {:.2f}".format(resultados['credito_liquido']))
    print("Parcela Pós Contemplacao: R$ {:.2f}".format(resultados['parcela_pos_contemplacao']))

if __name__ == "__main__":
    main()

