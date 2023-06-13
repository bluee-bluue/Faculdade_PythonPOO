class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumenta_salario(self, valor):
        self.salario += valor

    def reduz_salario(self, valor):
        if valor > self.salario:
            self.salario = 0
        else:
            self.salario -= valor


n = int(input())
funcionarios = []

for i in range(n):
    nome, salario = input().split()
    salario = float(salario)
    funcionarios.append(Funcionario(nome, salario))

while True:
    operacao = input().split()
    if operacao[0] == 'FIM':
        break
    nome = operacao[2]
    valor = float(operacao[1])
    for funcionario in funcionarios:
        if funcionario.nome == nome:
            if operacao[0] == 'aumenta':
                funcionario.aumenta_salario(valor)
            else:
                funcionario.reduz_salario(valor)

for funcionario in funcionarios:
    print(f'Nome: {funcionario.nome}')
    print(f'Salário: R$ {funcionario.salario:.2f}')
    print('-' * 20)
    