salarios = []
soma = 0

for _ in range(4):
    salario = float(input('salário R$: '))
    soma += salario
    salarios.append(salario)

media = soma / 4
print(f'Média R$: {media:.1f}')

for salario in salarios:
    if salario < media:
        print(f'abaixo da media: R$ {salario:.2f}')