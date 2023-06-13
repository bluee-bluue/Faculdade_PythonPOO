vicC = 2.5
doacao = 0
somaD = 0
soma_vicC = 0

while doacao != -1:
    doacao = float(input())
    
    if doacao != -1:
        somaD += doacao
        soma_vicC = somaD * vicC
        
print(f'VC$ {somaD:.2f}')
print(f'R$ {soma_vicC:.2f}')