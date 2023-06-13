entrada = int(input())
cont = 1
n = 65

while entrada < 1 or entrada > 26:
    entrada = int(input())

while cont <= 26 and n <= 90:
    print(f'{cont * chr(n)}')
    cont += 1
    n += 1

    if cont == entrada + 1:
        break