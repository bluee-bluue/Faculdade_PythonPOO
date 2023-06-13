alunos = dict()

for _ in range(5):
    ra = int(input('R.A.: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    alunos[ra] = [n1, n2, n3]
    print()

for ra in alunos:
    # media = (notas[ra][0] + notas[ra][1] + notas[ra][2]) / 3
    media = sum(alunos[ra]) / len(alunos[ra])
    print(f'R.A.: {ra}\nMédia: {media:.2f}\n')

print('-' * 10)

for nota in alunos.items():
    media = sum(nota[1]) / len(nota[1])
    print(f'R.A.: {nota[0]}\nMédia: {media:.2f}\n')

print('-' * 10)

for ra, nota in alunos.items():
    media = sum(nota) / len(nota)
    print(f'R.A.: {ra}\nMédia: {media:.2f}\n')