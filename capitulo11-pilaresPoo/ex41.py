class Forma():
    def quem_sou_eu(self):
        print("Eu sou uma forma.")


class Retangulo(Forma):
    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento

    def calcular_perimetro(self):
        return self.largura * 2 + self.comprimento * 2


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        return self.lado * 4

um_retangulo = Retangulo(20, 50)
um_quadrado = Quadrado(29)

um_retangulo.quem_sou_eu()
um_quadrado.quem_sou_eu()
