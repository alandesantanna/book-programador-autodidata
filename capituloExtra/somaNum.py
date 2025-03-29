x = int(input("Digite um numero inteiro:"))
soma = 0

for i in range(1, x, 1):
    soma += i
print("A soma dos números de 1 a", x, "é:", soma)