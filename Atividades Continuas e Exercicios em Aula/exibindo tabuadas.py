A = int(input())
B = int(input())

if (A > B):
  print('Nenhuma tabuada no intervalo!')
else:
  for intervalo in range(A, B + 1):
    for i in range(1, 11):
      print(f'{intervalo} x {i} = {intervalo * i}')
    print('----------')