# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.


from random import shuffle


class Carta:
    naipes = ["espadas",
              "copas",
              "ouros",
              "paus"]

    valores = [None, None, "2", "3",
               "4", "5", "6", "7",
               "8", "9", "10",
               "Valete", "Rainha",
               "Rei", "Ás"]

    def __init__(self, valor, naipe):
        """naipe + valor são inteiros"""
        self.valor = valor
        self.naipe = naipe

    def __lt__(self, outra_carta):
        if self.valor < outra_carta.valor:
            return True
        if self.valor == outra_carta.valor:
            if self.naipe < outra_carta.naipe:
                return True
            else:
                return False
        return False

    def __gt__(self, outra_carta):
        if self.valor > outra_carta.valor:
            return True
        if self.valor == outra_carta.valor:
            if self.naipe > outra_carta.naipe:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.valores[self.valor] + \
            " de " + \
            self.naipes[self.naipe]
        return v


class Baralho:
    def __init__(self):
        self.cartas = []
        for i in range(2, 15):
            for j in range(4):
                self.cartas.append(Carta(i, j))
        shuffle(self.cartas)

    def remover_carta(self):
        if len(self.cartas) == 0:
            return
        return self.cartas.pop()


class Jogador:
    def __init__(self, nome):
        self.vitorias = 0
        self.carta = None
        self.nome = nome


class Jogo:
    def __init__(self):
        nome1 = input("Nome do jogador 1: ")
        nome2 = input("Nome do jogador 2: ")
        self.baralho = Baralho()
        self.jogador1 = Jogador(nome1)
        self.jogador2 = Jogador(nome2)

    def venceu(self, vencedor):
        mensagem = "{} venceu esta rodada"
        mensagem = mensagem.format(vencedor)
        print(mensagem)

    def empate(self, nome1, carta1, nome2, carta2):
        mensagem = "{} jogou {} e {} jogou {}"
        mensagem = mensagem.format(nome1, carta1, nome2, carta2)
        print(mensagem)

    def jogar(self):
        cartas = self.baralho.cartas
        print("Começando o jogo de Guerra!")
        while len(cartas) >= 2:
            mensagem = "Digite 'q' para sair ou qualquer outra tecla para jogar: "
            resposta = input(mensagem)
            if resposta == 'q':
                break
            carta1 = self.baralho.remover_carta()
            carta2 = self.baralho.remover_carta()
            nome1 = self.jogador1.nome
            nome2 = self.jogador2.nome
            self.empate(nome1, carta1, nome2, carta2)
            if carta1 > carta2:
                self.jogador1.vitorias += 1
                self.venceu(self.jogador1.nome)
            else:
                self.jogador2.vitorias += 1
                self.venceu(self.jogador2.nome)

        vencedor = self.definir_vencedor(self.jogador1, self.jogador2)
        print("O jogo acabou. {} venceu!".format(vencedor))

    def definir_vencedor(self, jogador1, jogador2):
        if jogador1.vitorias > jogador2.vitorias:
            return jogador1.nome
        if jogador1.vitorias < jogador2.vitorias:
            return jogador2.nome
        return "Foi um empate!"

jogo = Jogo()
jogo.jogar()