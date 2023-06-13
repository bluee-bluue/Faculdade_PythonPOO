#a cada ano salário + 5%
#cumpriu a meta salário + 10%
funcionarios = [({'nome': 'Matheus Oliveira  ', 'salário': 1000.0, 'nada': '  ', 'anos': 2, 'meta': '  sim'}),
                ({'nome': 'Aline dos Santos  ', 'salário': 4000.0, 'nada': '  ', 'anos': 3, 'meta': '  sim'}),
                ({'nome': 'Carla Oliveira    ', 'salário': 1500.0, 'nada': '  ', 'anos': 1, 'meta': '  não'}),
                ({'nome': 'Leon Kennedy      ', 'salário': 5000.0, 'nada': '  ', 'anos': 10, 'meta': ' sim'})]

for pessoa in funcionarios:
    if pessoa['anos'] == 1:
        pessoa['salário'] = pessoa['salário'] + pessoa['salário']*0.05
    elif pessoa['anos'] == 2:
        pessoa['salário'] = pessoa['salário'] + pessoa['salário']*0.1
    elif pessoa['anos'] == 3:
        pessoa['salário'] = pessoa['salário'] + pessoa['salário']*0.15
    elif pessoa['anos'] == 10:
        pessoa['salário'] = pessoa['salário'] + pessoa['salário']*0.5

    contem = 'nao'
    if pessoa['meta'] not in contem:
        pessoa['salário'] = pessoa['salário'] + pessoa['salário']*0.1

    print(pessoa['nome'], pessoa['salário'], pessoa['nada'], pessoa['anos'], pessoa['meta'])
