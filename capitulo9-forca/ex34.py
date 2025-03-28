palavra = str(input("Digite uma palavra: ")).lower()
qtd_letras = len(palavra)
maxTentativas = qtd_letras

letrasDescobertas = ["_"] * qtd_letras
letrasErradas = []

print("Bem-vindo ao jogo da forca!")

while maxTentativas > 0 and "_" in letrasDescobertas:
    print("\nPalavra:", " ".join(letrasDescobertas))
    print(f"Tentativas restantes: {maxTentativas}")
    print(f"Letras erradas: {', '.join(letrasErradas)}")

    letra = input("Digite uma letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite apenas uma letra.")
        continue

    if letra in letrasDescobertas or letra in letrasErradas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    if letra in palavra:
        print("Boa! Você acertou uma letra.")
        for i, l in enumerate(palavra):
            if l == letra:
                letrasDescobertas[i] = letra
    else:
        print("Ops! Essa letra não está na palavra.")
        letrasErradas.append(letra)
        maxTentativas -= 1

if "_" not in letrasDescobertas:
    print("\nParabéns! Você acertou a palavra:", palavra)
else:
    print("\nVocê perdeu! A palavra era:", palavra)



