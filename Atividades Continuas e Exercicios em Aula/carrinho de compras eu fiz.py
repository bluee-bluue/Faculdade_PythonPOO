carrinho = input().split()

comando = input().split()

while comando[0] != 'encerrar':
  if carrinho != []:
    for i in range(len(carrinho)):
      carrinho[i] = int(carrinho[i])

  if comando[0] == 'adicionar':
    carrinho.append(comando[1])

  elif comando[0] == 'exibir':
    carrinho.sort()

    for i in range(len(carrinho)):
      if (i < len(carrinho) - 1):
        print(carrinho[i], end=' ')
      else:
        print(carrinho[i])

  elif comando[0] == 'remover':
    codigo = int(comando[1])
    if codigo in carrinho:
      carrinho.remove(codigo)
    else:
      print(f'código {codigo} não encontrado')
  
  comando = input().split()

print(carrinho[i])