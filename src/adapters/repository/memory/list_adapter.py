from typing import List
from src.adapters.repository.repository_interface import RepositoryInterface
from src.entity.person import Person

class ListAdapter(RepositoryInterface):
    _people: List[Person] = []
    
    def person_create(self, person: Person):
        self._people.append(person)

    def person_show(self):
        for person in self._people:
            print('\n')
            print(f"Completed registration ( Name : {person.name} | Age : {person.age} | Genre : {person.genre} )")
            print('\n')

    

