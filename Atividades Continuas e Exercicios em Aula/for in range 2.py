nomes = []
for _ in range(5):
    nomes.append(input('nome: '))

qnt = 0

for nome in nomes:
    if (nome [0] == 'A' or nome [0] == 'E' or nome [0] == 'I' or nome [0] == 'O' or nome [0] == 'U'):
        qnt += 1
        print(f'{qnt} de nomes começa em vogal')