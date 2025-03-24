def converter_para_float(valor_str):
    """
    Converte uma string para float.

    Parâmetros:
    valor_str (str): A string a ser convertida.

    Retorna:
    float: O valor convertido, ou None se a conversão falhar.
    """
    try:
        resultado = float(valor_str)
        return resultado
    except ValueError:
        print("Erro: A string fornecida não pode ser convertida para float.")
        return None

# Exemplo de uso da função
valor = input("Digite um valor para converter para float: ")
resultado = converter_para_float(valor)
if resultado is not None:
    print(f"O valor convertido é: {resultado}")