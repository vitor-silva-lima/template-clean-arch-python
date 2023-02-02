class Pessoa:
    nome: str = None
    _idade: int = None
    genero: str = None

    def __init__(
        self,
        nome,
        idade,
        genero,
    ) -> None:
        self.nome = nome,
        self.idade = idade
        self.genero = genero

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, value: int):
        if value > 0:
            self._idade = value
        else:
            raise Exception("Idade Menor do que zero")


p = Pessoa(
    nome= "Vitor",
    idade= 5,
    genero="Masculino"
)


print(p.idade)
