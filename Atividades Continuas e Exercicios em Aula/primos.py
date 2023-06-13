def primo(n):
    divisores = 0
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            divisores += 1
    return divisores == 2

inicio = int(input())
fim = int(input())
primos = 0

for n in range(inicio, fim + 1):
    if primo(n):
        print(n)
        primos += 1
print(f'primos: {primos}')