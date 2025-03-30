class Maca:
    def __init__(self, tamanho, cor, data_colheita, validade):
        self.tamanho = tamanho
        self.cor = cor
        self.data_colheita = data_colheita
        self.validade = validade


m1 = Maca(10, "vermelha", "2023-10-01", "2023-10-15")

print(m1.tamanho, m1.cor, m1.data_colheita, m1.validade)