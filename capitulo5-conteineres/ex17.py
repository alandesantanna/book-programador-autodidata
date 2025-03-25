musicas = {"orochi": "balão", "mc cabelinho": "x1", "filipe ret": "alem do dinheiro"}

pergunta = input("Qual cantor você quer acessar: ")
if pergunta in musicas:
    print(musicas[pergunta])
else:    
    print("Esse cantor não existe.")