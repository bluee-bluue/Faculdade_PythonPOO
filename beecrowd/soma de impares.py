x = int(input())
y = int(input())
lista = []

if x > y:
    a = x
    x = y
    y = a
    
    for numero in range(x+1, y):    
        if numero % 2 != 0:
            lista.append(numero)
elif y > x:
    x = x
    y = y
    
    for numero in range(x, y):    
        if numero % 2 != 0:
            lista.append(numero)

print(sum(lista))
