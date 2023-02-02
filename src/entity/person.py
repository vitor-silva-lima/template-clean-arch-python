class Person:
    _name: str = None
    _age: int = None
    _genre: str = None

    def __init__(
        self,
        name,
        age,
        genre,
    ) -> None:
        self.name = name
        self.age = age
        self.genre = genre

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value
    
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 0:
            raise Exception("Age cannot be less than zero")
        
        self._age = value

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    def genre(self, value: str):
        self._genre = value
