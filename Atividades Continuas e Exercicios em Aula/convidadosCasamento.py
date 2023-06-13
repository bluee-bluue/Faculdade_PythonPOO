# meu codigo
convidados_noiva = []
convidados_noivo = []
convidados_ambos = []
convidados_apenas_noiva = []
convidados_apenas_noivo = []

while True:
    entrada = input().split(';')
    if entrada[0].upper() == 'ACABOU':
        break
    x = entrada[0]
    y = entrada[1]
    if y == 'noiva':
        if x not in convidados_noiva:
            convidados_noiva.append(x)
        else:
            continue
    elif y == 'noivo':
        if x not in convidados_noivo:
            convidados_noivo.append(x)
        else:
            continue


convidados_final = set(convidados_noiva + convidados_noivo)


for x in convidados_noiva:
    if x not in convidados_noivo:
        convidados_apenas_noiva.append(x)
for x in convidados_noivo:
    if x not in convidados_noiva:
        convidados_apenas_noivo.append(x)
for x in convidados_noiva:
    if x in convidados_noivo:
        convidados_ambos.append(x)


print('-' * 20)
print('LISTA DE CONVIDADOS')
print('-' * 20)
for x in convidados_final:
    print(x)
print()
print('-' * 20)
print('CONVIDADOS APENAS DA NOIVA')
print('-' * 20)
for x in convidados_apenas_noiva:
    print(x)
print()
print('-' * 20)
print('CONVIDADOS APENAS DO NOIVO')
print('-' * 20)
for x in convidados_apenas_noivo:
    print(x)
print()
print('-' * 20)
print('CONVIDADOS DE AMBOS')
print('-' * 20)
for x in convidados_ambos:
    print(x)
print()
print('-' * 20)
print('CONVIDADOS POR APENAS UM DELES')
print('-' * 20)
for x in set(convidados_noiva) ^ set(convidados_noivo):
    print(x)


# codigo certo
noiva = set()
noivo = set()
ambos = set()

while True:
    entrada = input().split(';')
    if entrada[0] == 'ACABOU':
        break
    nome = entrada[0]
    convidado_por = entrada[1]
    if nome in ambos or nome in (noiva if convidado_por == 'noiva' else noivo):
        continue
    if convidado_por == 'noiva':
        noiva.add(nome)
    else:
        noivo.add(nome)
    if nome in (noiva if convidado_por == 'noivo' else noivo):
        ambos.add(nome)

lista_final = sorted(noiva.union(noivo))
lista_noiva = sorted(noiva - ambos)
lista_noivo = sorted(noivo - ambos)
lista_ambos = sorted(ambos)
lista_apenas_um = sorted((noiva - noivo) | (noivo - noiva))

print('-' * 20)
print('LISTA FINAL')
print('-' * 20)
for nome in lista_final:
    print(nome)
print()

print('-' * 20)
print('APENAS NOIVA')
print('-' * 20)
for nome in lista_noiva:
    print(nome)
print()

print('-' * 20)
print('APENAS NOIVO')
print('-' * 20)
for nome in lista_noivo:
    print(nome)
print()

print('-' * 20)
print('POR AMBOS')
print('-' * 20)
for nome in lista_ambos:
    print(nome)
print()

print('-' * 20)
print('POR APENAS UM DELES')
print('-' * 20)
for nome in lista_apenas_um:
    print(nome)