def numquad(x):
    return x ** 2


x = int(input("Digite um número: "))
print(numquad(x))

def exibir_mensagem(mensagem):
    """
    Exibe a mensagem fornecida.

    Parâmetros:
    mensagem (str): A mensagem a ser exibida.
    """
    print(mensagem)

# Exemplo de uso da função
exibir_mensagem("Olá, esta é a mensagem a ser exibida!")
