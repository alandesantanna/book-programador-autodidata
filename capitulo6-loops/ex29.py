numeros = [3, 7, 15, 23, 42]

print("Bem-vindo! Tente adivinhar um número da lista.")
print("Digite 'q' para sair.")

while True:

    entrada = input("Digite um número: ")

    if entrada.lower() == 'q':
        print("Saindo do programa. Até mais!")
        break

    try:
        numero = int(entrada)
        if numero in numeros:
            print("Parabéns! Você acertou, o número está na lista.")
        else:
            print("Que pena! O número não está na lista.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número ou 'q' para sair.")