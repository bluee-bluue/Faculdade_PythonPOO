class PosGraduacao():
    def __init__(self, instituicao, curso):
        self.instituicao = instituicao
        self.curso = curso

    def get_curso(self):
        return 'Doutorado em ' + self.curso


class Doutorado(PosGraduacao):
    def __init__(self, instituicao, curso, tese=None):
        super().__init__(instituicao, curso)
        self.__tese = tese

    def get_tese(self):
        return self.__tese

    def set_tese(self, titulo):
        self.__tese = titulo


nomeCurso = 'Ciência da Computação'
universidade = 'Universidade Federal de São Paulo'
teseTitulo = 'Tecnologias Digitais na Educação: Potencialidades e Desafios para a Formação de Professores'

dr = Doutorado(universidade, nomeCurso)
dr.set_tese(teseTitulo)
print(dr.get_tese())
