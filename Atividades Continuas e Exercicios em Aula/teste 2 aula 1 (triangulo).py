# Fornecidos os três segmentos de reta
# a, b e c (a > 0, b > 0 e c > 0), verificar se
# podem formar um triângulo. Exibir a mensagem
# 'formam' ou 'não formam', conforme o caso.
# Condição de existência de triângulo:
# "Todo lado deve ser menor do que a soma dos outros dois lados.

a = int(input())
b = int(input())
c = int(input())

if a < b + c and b < a + c and c < a + b:  #
    print('formam')  # CERTO
else:  #
    print('nao formam')  #

# ------------------------
# if a < b+c:                       #
#    print('formam')               #
# elif b < a+c:                     #
#    print('formam')               #  ERRADO
# elif c < a+b:                     #
#    print('formam')               #
# else:                             #
#    print('nao formam')           #
