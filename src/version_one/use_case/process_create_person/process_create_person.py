from src.version_one.adapters.repository.repository_interface import RepositoryInterface
from src.version_one.entity.pessoa import Pessoa
from src.version_one.use_case.process_create_person.create_person_dto import PessoaDtoInput, PessoaDtoOutput


class ProcessCreatePerson():

    def __init__(self, repository: RepositoryInterface) -> None:
        self.repository = repository


    def execute(self, input: PessoaDtoInput) -> PessoaDtoOutput:
        output = PessoaDtoOutput()
        try:
            pessoa = Pessoa(
                nome= input.name,
                idade= input.idade,
                genero= input.genero
            )
            self.repository.person_create(pessoa= pessoa)
            self.repository.person_show()

            output.status = 'success'
        except Exception as e:
            output.status = 'error'
        finally:
            return output