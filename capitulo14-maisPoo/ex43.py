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


um_quadrado = Quadrado(29)
print(Quadrado.lista_quadrados)
outro_quadrado = Quadrado(93)
print(Quadrado.lista_quadrados)