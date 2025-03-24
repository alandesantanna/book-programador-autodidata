def intdiv(x):
    """
    Realiza a divisão inteira de x por 2.

    Parâmetros:
    x (int): O número a ser dividido.

    Retorna:
    int: O resultado da divisão inteira de x por 2.
    """
    return x // 2

def intmult(x):
    """
    Multiplica x por 4.

    Parâmetros:
    x (int): O número a ser multiplicado.

    Retorna:
    int: O resultado da multiplicação de x por 4.
    """
    return x * 4

x = int(input("Digite um número: "))
y = intdiv(x)
z = intmult(y)
print(z)