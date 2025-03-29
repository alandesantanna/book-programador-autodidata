x = int(input("Digite um número inteiro positivo: "))

def fatorial(y):
    if y < 0:
        print("Número inválido")
    elif y == 0:
        return 1
    else:
        fatorial=1
        for i in range(1, y+1):
            fatorial *= i
        return fatorial

z = fatorial(x)
print(f"O fatorial de {x} é {z}")