def maior_nome(funcionarios):
    maior = 0
    for funcionario in funcionarios:
        if len(funcionario[0]) > maior:
            maior = len(funcionario[0])
    return maior

def exibe_func(funcionarios):
    maior = maior_nome(funcionarios)

    print('\n' + '-' * 50)
    print(f'{"NOME":^{maior}}', end=' | ')
    print(f'{"SALARIO":^11}', end=' | ')
    print(f'{"TEMPO":^7}', end=' | ')
    print(f'{"META"}')
    print('-' * 50)


    for funcionario in funcionarios:
        print(f'{funcionario[0]:{maior}}', end=' | ')
        print(f'R$ {funcionario[1]:8.2f}', end=' | ')
        print(f'{funcionario[2]:2}', end=' | ')
        print(f'{funcionario[3]}')
        if funcionario[3]:
            print(f'{"😀":^4}')
        else:
            print(f'{"😔":^4}')
    
    print('-' * 50)

def exibe_bonus(bonus):
    maior = maior_nome(funcionarios)
    print('\n' + '-' * 30)
    print(f'{"NOME":^{maior}}', end=' | ')
    print(f'{"BÔNUS":^11}')
    print('-' * 30)
    for funcionario in bonus:
        print(f'{funcionario[0]:{maior}}', end=' | ')
        print(f'R$ {funcionario[1]:8.2f}')
    print('-' * 30)

funcionarios = []
entrada = input('Funcionário? ')

while entrada != '':
    funcionario = entrada.split(';')
    funcionario[1] = float(funcionario[1])
    funcionario[2] = int(funcionario[2])
    funcionario[3] = (funcionario[3] == 'sim')
    funcionario.append(funcionario)
    entrada = input('Funcionario? ')

exibe_func(funcionarios)

bonus = []

for funcionario in funcionarios:
    valor = funcionario[1] + (0.05 * funcionario[2] * funcionario[1])

    if funcionario[3]:
        valor += 0.10 * valor
    bonus.append([funcionario[0], valor])

exibe_bonus(bonus)
#Caique;1000;5;sim
#Caio;500;3;nao
#Tatiana;1800;20;sim
#Sergio;5000;20;sim