class Cavaleiro():
    def __init__(self, nome):
        self.nome = nome


class Cavalo():
    def __init__(self, nome, cavaleiro):
        self.nome = nome
        self.cavaleiro = cavaleiro

o_cavaleiro = Cavaleiro("Sally")
harry_o_cavalo = Cavalo("Harry", o_cavaleiro)

print("O nome do Cavalo é {}".format(harry_o_cavalo.nome))
print("O nome do Cavaleiro é {}".format(harry_o_cavalo.cavaleiro.nome))