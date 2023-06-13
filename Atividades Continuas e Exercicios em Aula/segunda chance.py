alunos = int(input())

def notas():
  notas = []

  for _ in range(alunos):
    notas.append(float(input()))

  return notas

def notas_finais(notas_originais, novas_notas):
  qnt_notas = 0

  for i in range(len(notas_originais)):
    if (novas_notas[i] == 10 and notas_originais[i] < 10):
      novas_notas[i] = min(notas_originais[i] + 2, 10)
      qnt_notas += 1
    else:
      novas_notas[i] = notas_originais[i]

  return qnt_notas

def notas_alteradas(notas_originais, notas_finais, qnt_notas):
  print(f'NOTAS ALTERADAS: {qnt_notas}')
  for i in range(alunos):
    nota_alterada = ('*' if notas_originais[i] != notas_finais[i] else '-')
    print(f'{nota_alterada}({i+1:03}) original: {notas_originais[i]:05.2f} | final: {notas_finais[i]:05.2f}')

if (1 <= alunos <= 999):
  notas_originais = notas()
  novas_notas = notas()
  qnt_notas = notas_finais(notas_originais, novas_notas)
  notas_alteradas(notas_originais, novas_notas, qnt_notas)