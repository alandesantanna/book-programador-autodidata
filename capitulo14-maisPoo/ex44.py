class Forma():
    def quem_sou_eu(self):
        print("Eu sou uma forma.")


class Quadrado(Forma):
    lista_quadrados = []

    def __init__(self, lado):
        self.lado = lado
        self.lista_quadrados.append(self)

    def calcular_perimetro(self):
        return self.lado * 4

    def quem_sou_eu(self):
        super().quem_sou_eu()
        print("Eu sou um Quadrado.")

    def __repr__(self):
        return "{} por {} por {} por {}".format(self.lado, self.lado, self.lado, self.lado)

um_quadrado = Quadrado(29)
print(um_quadrado)