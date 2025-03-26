import os
import csv

caminho = os.path.join("/", "home", "alan", "Documentos", "arquivo.csv")

filmes = [
    ["Top gun", "Ponte para terabitia", "O rei leão"],
    ["A espera de um milagre", "O poderoso chefão", "O senhor dos anéis"],
    ["Star wars", "Matrix", "O iluminado"]
]
 # grave os filmes em um arquivo csv e separe cada lista por uma linha
with open(caminho, "w") as arquivo:
    escritor = csv.writer(arquivo)
    for filme in filmes:
        escritor.writerow(filme)    
