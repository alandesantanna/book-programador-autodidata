x = int(input("Digite um número inteiro: "))
y = int(input("Dgite outro número inteiro:"))

print("Escolha uma operação matematica: ")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("Digite o número da operação desejada: "))
if op == 1:
    print(f"{x} + {y} = {x + y}")
elif op == 2:
    print(f"{x} - {y} = {x - y}")
elif op == 3:
    print(f"{x} * {y} = {x * y}")
elif op == 4:
    if y == 0:
        print("Divisão por zero não é permitida.")
    else:
        print(f"{x} / {y} = {x / y}")
else:
    print("Operação inválida.")