class Endereco:
    def __init__(self, rua, endereco, bairro, complemento, cep):
        self.rua = rua
        self.endereco = endereco
        self.bairro = bairro
        self.complemento = complemento
        self.cep = cep

    def exibir_dados(self):
        print('Dados do endereço: ')
        print('Rua:', self.rua)
        print('Endereço:', self.endereco)
        print('Bairro:', self.bairro)
        print('Complemento:', self.complemento)
        print('CEP:', self.cep)


class Funcionario:
    def __init__(self, nome, data_nasc, sexo, salario, endereco):
        self.nome = nome
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.salario = salario
        self.endereco = endereco

    def exibir_dados(self):
        print('Dados do funcionário:')
        print('Nome:', self.nome)
        print('Data_nasc:', self.data_nasc)
        print('Sexo:', self.sexo)
        print(f'Salario: R$ {self.salario:.2f}\n')
        self.endereco.exibir_dados()


def main():
    e = Endereco('Rua Dr Arnaldo de Campos', 304, 'Vila Zatt', 'S/C', '02975-160')
    f = Funcionario('Caique', '14/09/2002', 'M', 1000, e)
    f.exibir_dados()


main()