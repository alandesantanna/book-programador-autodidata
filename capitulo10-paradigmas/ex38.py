class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
t1 = Triangulo(base, altura)
print(f"Área do triângulo: {t1.area():.2f}")