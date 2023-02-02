from typing import List
from src.version_one.adapters.repository.repository_interface import RepositoryInterface
from src.version_one.entity.pessoa import Pessoa

class ListPython(RepositoryInterface):
    bd: List[Pessoa] = []
    
    
    def person_create(self, pessoa: Pessoa):
        self.bd.append(pessoa)

    def person_show(self):
        for person in self.bd:
            print(person.nome)
            print(person.idade)
            print(person.genero)

    

