infos = {"nome": "lucas", "idade": 17, "cidade": "são paulo", "estado": None}
print(infos["nome"], infos["idade"], infos["cidade"])

pergunta = input("Qual chave você quer acessar: ")
if pergunta in infos:
    print(infos[pergunta])
else:
    print("Essa chave não existe.")