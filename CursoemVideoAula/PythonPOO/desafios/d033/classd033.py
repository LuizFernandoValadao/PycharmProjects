from abc import ABC, abstractmethod
from datetime import date

ano = date.today().year

class Pessoa(ABC):

    def __init__(self, nome: str, nascimento: int):
        self._nome = nome
        self._nascimento = nascimento
        self.idade = idade

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        if nascimento >= ano:
            raise ValueError(f'Ano {ano} é inválido')
        else:
            self._nascimento = nascimento

    @property
    def idade(self):
        return self.idade

    @idade.setter
    def idade(self, idade):
        self.idade = ano - self._nascimento
        raise PermissionError('Não pode alterar a idade')




class Aluno(Pessoa):

    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']

    def __init__(self, nome: str, nascimento: int, curso: str):
        super().__init__(nome, nascimento)
        self._curso = curso


    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if Aluno.curso not in self.cursos_oficiais:
            print('Curso não existe')
        else:
            print('Curso ok')
            self._curso = Aluno.curso

