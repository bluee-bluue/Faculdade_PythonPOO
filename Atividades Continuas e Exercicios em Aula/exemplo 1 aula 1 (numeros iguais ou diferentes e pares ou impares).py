#Crie um programa que receba dois números inteiros e
# #exiba uma mensagem indicando se os números são iguais ou
#diferentes e, caso sejam iguais, se são pares ou ímpares.

n1 = int(input())
n2 = int(input())

if n1 == n2:
    print('numeros iguais,', end='')
    if n1%2 == 0:
        print('ambos pares')
    else:
        print('ambos impares')
else:
    print('numeros diferentes')