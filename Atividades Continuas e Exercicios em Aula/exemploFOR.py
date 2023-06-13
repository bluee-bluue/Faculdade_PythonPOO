# for <item> in <conjunto_de_itens>:
#    <bloco_de_codigo>

def vogais_consoantes():
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vogais = []
    consoantes = []

    for letra in 'AEIOU':
        print(letra)

    # pulei uma linha para separar vogal do alfabeto no print
    for letra in f'\n{alfabeto}':
        print(letra)

    for letra in alfabeto:
        if letra in 'AEIOU':
            vogais.append(letra)
        else:
            consoantes.append(letra)

    print(vogais)
    print(consoantes)


def cidade():
    contador = 0
    pessoas = [({'nome': 'João', 'cidade': 'Belo Horizonte'}),
               ({'nome': 'Maria', 'cidade': 'São Paulo'}),
               ({'nome': 'Pedro', 'cidade': 'Curitiba'}),
               ({'nome': 'Caique', 'cidade': 'Rio de Janeiro'})]
    for pessoa in pessoas:
        contador += 1
        print(f'\n{contador}')
        print(pessoa['nome'], 'mora em', pessoa['cidade'])


def ate_10():
    # ate 10
    print(f'\n')
    for numero in range(1, 10 + 1):
        if numero % 2 == 0:
            print('O número', numero, 'é par')
        else:
            print('O número', numero, 'é impar')


def tabuada():
    for numero_coluna1 in range(2, 5):
        print(f'\nTabuada do ', numero_coluna1)
        for numero_coluna2 in range(11):
            print(numero_coluna1, "x", numero_coluna2, " = ", numero_coluna1 * numero_coluna2)


def tabela():
    # a cada ano salário + 5%
    # cumpriu a meta salário + 10%
    funcionarios = [({'nome': 'Matheus Oliveira  ', 'salário': 1000.0, 'nada': '  ', 'anos': 2, 'meta': '  sim'}),
                    ({'nome': 'Aline dos Santos  ', 'salário': 4000.0, 'nada': '  ', 'anos': 3, 'meta': '  sim'}),
                    ({'nome': 'Carla Oliveira    ', 'salário': 1500.0, 'nada': '  ', 'anos': 1, 'meta': '  não'}),
                    ({'nome': 'Leon Kennedy      ', 'salário': 5000.0, 'nada': '  ', 'anos': 10, 'meta': ' sim'})]

    for pessoa in funcionarios:
        if pessoa['anos'] == 1:
            pessoa['salário'] = pessoa['salário'] + pessoa['salário'] * 0.05
        elif pessoa['anos'] == 2:
            pessoa['salário'] = pessoa['salário'] + pessoa['salário'] * 0.1
        elif pessoa['anos'] == 3:
            pessoa['salário'] = pessoa['salário'] + pessoa['salário'] * 0.15
        elif pessoa['anos'] == 10:
            pessoa['salário'] = pessoa['salário'] + pessoa['salário'] * 0.5

        contem = 'nao'
        if pessoa['meta'] not in contem:
            pessoa['salário'] = pessoa['salário'] + pessoa['salário'] * 0.1

        print(pessoa['nome'], pessoa['salário'], pessoa['nada'], pessoa['anos'], pessoa['meta'])


escolha = int(input(f'\n1 - vogais e consoantes\n2 - cidade\n3 - ate 10\n4 - tabuada\n5 - tabela\n'))

if escolha == 1:
    vogais_consoantes()
if escolha == 2:
    cidade()
if escolha == 3:
    ate_10()
if escolha == 4:
    tabuada()
if escolha == 5:
    tabela()