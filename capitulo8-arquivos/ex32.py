import os

caminho = os.path.join("/", "home", "alan", "Documentos", "arquivo.txt")

nome = str(input("Digite o nome: "))

with open(caminho, "w") as arquivo:
    arquivo.write(nome)

with open(caminho, "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
