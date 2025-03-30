class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)
        

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return 4 * self.lado
    
    def tamanho(self, tamanho):
        self.lado = tamanho
        return self.lado

    

x = int(input("Digite a largura do retangulo: "))
y = int(input("DIgite a altura do retangulo: "))
retangulo = Retangulo(x, y)

print(f"Perímetro do retângulo: {retangulo.perimetro()}")

t = int(input("Digite o lado do quadrado: "))

quadrado = Quadrado(t)
print(f"Perímetro do quadrado: {quadrado.perimetro()}")

z = int(input("digite um novo valor para alterar o tamanho do quadrado: "))
tamanho = quadrado.tamanho(z)

print(f"Perímetro do quadrado: {quadrado.perimetro()}")
