n = int(input())

if (0 <= n <= 10):
    cont = 1

    while cont <= 10:
        print(f'{n} x {cont} = {n * cont}')
        cont += 1