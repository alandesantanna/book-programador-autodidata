def cadastro_users(nome, sobrenome, email, idade=None, telefone=None):
    """
    Cadastra um usuário com as informações fornecidas.

    Parâmetros:
    nome (str): O nome do usuário.
    sobrenome (str): O sobrenome do usuário.
    email (str): O email do usuário.
    idade (int, opcional): A idade do usuário. Padrão é None.
    telefone (str, opcional): O telefone do usuário. Padrão é None.

    Retorna:
    dict: Um dicionário contendo as informações do usuário.
    """
    usuario = {
        "nome": nome,
        "sobrenome": sobrenome,
        "email": email,
        "idade": idade,
        "telefone": telefone
    }
    return usuario

# Exemplo de uso da função
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
email = input("Digite seu email: ")
idade = input("Digite sua idade: ")
telefone = input("Digite seu telefone: ")

print(cadastro_users(nome, sobrenome, email, idade, telefone))