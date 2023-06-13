class Moeda:
    def __init__(self, valor):
        self.valor = valor


class Cofre:
    def __init__(self):
        self.total = 0
        self.moedas = []

    def adicionar(self, moeda):
        self.moedas.append(moeda)

    def calcular_total(self):
        for moeda in self.moedas:
            self.total += moeda.valor
        return self.total


cofre = Cofre()
cofre.adicionar(Moeda(2.6))
cofre.adicionar(Moeda(5.7))
cofre.adicionar(Moeda(5.1))

print('O valor total do cofre é:', cofre.calcular_total())
