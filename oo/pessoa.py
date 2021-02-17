class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=19):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    silva = Pessoa(nome='Silva')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(vitoria.olhos)
    print(silva.olhos)
