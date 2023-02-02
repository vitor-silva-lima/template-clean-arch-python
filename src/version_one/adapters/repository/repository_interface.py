import abc
from typing import List


from src.version_one.entity.pessoa import Pessoa

class RepositoryInterface(metaclass = abc.ABCMeta):

    @abc.abstractclassmethod
    def person_create(self, pessoa: Pessoa):
        ...

    @abc.abstractclassmethod
    def person_show(self):
        ...
    
