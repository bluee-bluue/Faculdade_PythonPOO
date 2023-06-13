lista = []
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))

pares = 0

if lista[0] %2 == 0:
    pares += 1
if lista[1] %2 == 0:
    pares += 1
if lista[2] %2 == 0:
    pares += 1
if lista[3] %2 == 0:
    pares += 1
if lista[4] %2 == 0:
    pares += 1

print(pares, 'valores pares')
