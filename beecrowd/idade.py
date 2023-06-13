soma = 0
media_de = 0

while True:
    idade = int(input())
    if(idade >= 0):
        soma += idade
        media_de += 1
    else:
        break

print("%.2f" %(soma/float(media_de)))
