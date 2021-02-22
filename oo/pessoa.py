class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=19):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 10

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos  {cls.olhos}'


class Homem(Pessoa):
    pass


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    silva = Mutante(nome='Silva')
    vitoria = Pessoa(silva, nome='Vitória')
    print(Pessoa.cumprimentar(vitoria))
    print(id(vitoria))
    print(vitoria.cumprimentar())
    print(vitoria.nome)
    print(vitoria.idade)
    for filho in vitoria.filhos:
        print(filho.nome)
    vitoria.sobrenome = 'Santos'
    del vitoria.filhos
    vitoria.olhos = 4
    del vitoria.olhos
    print(vitoria.__dict__)
    print(silva.__dict__)
    print(Pessoa.olhos)
    print(vitoria.olhos)
    print(silva.olhos)
    print(Pessoa.metodo_estatico(), vitoria.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), vitoria.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(silva.olhos)
