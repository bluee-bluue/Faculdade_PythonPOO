class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas


def exibe(self):
    print('-' * 45)
    print(f'Título..............: {self.titulo}')
    print(f'Autor...............: {self.autor}')
    print(f'Número de Páginas...: {self.num_paginas}')


livro1 = Livro('A Culpa é das Estrelas', 'John Green', 286)
livro2 = Livro('Quem é Você, Alasca?', 'John Green', 335)

exibe(livro1)
exibe(livro2)