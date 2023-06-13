notas = input().split()
nota_1, nota_2, nota_3, nota_4 = notas

nota_1 = float(nota_1)
nota_2 = float(nota_2)
nota_3 = float(nota_3)
nota_4 = float(nota_4)

media = ((nota_1*2) + (nota_2*3) + (nota_3*4) + (nota_4*1))/10

print(f'Media: {media:.1f}')

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")

if media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')
    media = (media + nota_exame)/2

    if media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f'Media final: {media:.1f}')
