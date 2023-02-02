import abc
from src.entity.person import Person

class RepositoryInterface(metaclass = abc.ABCMeta):

    @abc.abstractclassmethod
    def person_create(self, person: Person):
        ...

    @abc.abstractclassmethod
    def person_show(self):
        ...
    
