class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura
    

x = float(input("Digite a largura do retângulo: "))
y = float(input("Digite a altura do retângulo: "))
r1 = Retangulo(x, y)
print(f"Área do retângulo: {r1.area():.2f}")