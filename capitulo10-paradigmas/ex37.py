import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

x = int(input("Digite o raio do círculo: "))
c1 = Circulo(x)
print(f"Área do círculo: {c1.area():.2f}")