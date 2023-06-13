def quociente(a, b):
    return a // b

while True:
    x = int(input())
    y = int(input())
    q = quociente(x, y)

    try:
        print(f'{x} // {y} = {q}')
    except:
        print('Erro! Divisão inválida')
    else:
        print('Divisão bem sucedida')
    finally:
        continuar = input('continuar (s/n)?')
        if continuar == 'n': break

print('Até mais!')