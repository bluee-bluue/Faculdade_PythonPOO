class Pessoa:
    def __init__(self, nome, idade, carro):
        self.nome = nome
        self.idade = idade
        self.carro = carro

    def comprar_carro(self, carro):
        self.carro = carro


class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano


meucarro = Carro('Volkswagem', 'Golf', 'FGY-4589', 2017)
eu = Pessoa('Caique', 20, None)
eu.comprar_carro(meucarro)

print('Meu nome:', eu.nome)
print('Modelo do meu carro:', eu.carro.modelo)
print('Placa do meu carro:', eu.carro.placa)
