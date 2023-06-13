#dado um numero inteiro positivo n de 4
#digitos, verificar se n é um numero cuja raiz
#quadrada é formada pela soma de suas dezenas.
#exibir 'sim' ou 'nao'. nao use o operador de
#potencia, nem funçôes (use apenas input, print e int).

#2025 e 1063 no input


#---------------------------
#n = int(input())
#n1 = n // 100
#n2 = n % 100
#soma = n1 + n2
#quad = soma * soma

#if quad == n:
#    print('sim')
#else:
#    print('nao')
#---------------------------

n = int(input())
quad = (n // 100) + (n % 100) * (n // 100) + (n % 100)

if quad == n:
    print('sim')
else:
    print('nao')


#---------------------------
#n = int(input())
#print('sim' if (n // 100) + (n % 100) * (n // 100) + (n % 100) == n else 'nao')
#---------------------------