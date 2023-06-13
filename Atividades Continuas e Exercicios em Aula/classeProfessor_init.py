class Professor:
    def __init__(self, nome, drt, contratacao, status, diciplina, carga_max):
        self.nome = nome
        self.drt = drt
        self.contratacao = contratacao
        self.status = status
        self.diciplina = diciplina
        self.cargaMax = carga_max

    def set_diciplina(self, diciplina):
        self.diciplina = diciplina

    def set_cargamaxima(self, carga_max):
        self.cargaMax = carga_max


def exibe(p):
    print('-' * 35)
    print(f'Nome..........: {p.nome}')
    print(f'DRT...........: {p.drt}')
    print(f'Contratacao...: {p.contratacao}')
    print(f'Status........: {p.status}')
    print(f'Diciplina.....: {p.diciplina}')
    print(f'Carga Máxima..: {p.cargaMax} horas/semana')
    print('-' * 35)


prof = Professor('Ana', '543', '20/03/2020', 'Titular', 'Inglês', 20)

exibe(prof)
# print(prof.nome)
# print(prof.drt)
# print(prof.contratacao)
# print(prof.status)
# print(prof.diciplina)
# print(prof.cargaMax)
