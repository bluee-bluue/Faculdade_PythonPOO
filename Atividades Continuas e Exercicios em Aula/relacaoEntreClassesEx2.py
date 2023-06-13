class Pedido:
    def __init__(self, valor, produto):
        self.valor = valor
        self.produto = []

    def adicionar_produto(self, produto):
        self.produto = produto

    def calcular_valor(self, valor):
        self.valor = valor


class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd


cafe = Produto('Café solúvel', 5.50, 1)
arroz = Produto('Arroz integral', 4.90, 2)
feijao = Produto('Feijão preto', 2.80, 2)

meu_pedido = Pedido()

meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)

print('O valor total é:', meu_pedido.calcular_valor(cafe.preco +
                                                    arroz.preco +
                                                    feijao.preco))