x = int(input("Digite um número inteiro positivo: "))

if x > 1:
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            print(f"O número {x} não é primo")
            break
    else:
        print(f"O número {x} é primo")
else:
    print(f"O número {x} não é primo")
    