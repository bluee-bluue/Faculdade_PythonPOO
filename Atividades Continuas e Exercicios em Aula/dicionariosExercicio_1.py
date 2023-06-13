produtos = {}

for _ in range(5):
    nome = input('Nome: ')
    preco = float(input('Preço: '))
    produtos[nome] = preco
    print()

print('-' * 30)
print('Produtos acima de R$50,00')
print('-' * 30)

for x in produtos:
    if produtos[x] > 50.00:
        print(f'Produto: {x}')

print('-' * 30)

for produto in produtos.items():
    if produto[1] > 50.00:
        print(f'Produto: {produto[0]}')

print('-' * 30)

for nome, preco in produtos.items():
    if preco > 50.00:
        print(f'Produto: {nome}')

print('-' * 30)
