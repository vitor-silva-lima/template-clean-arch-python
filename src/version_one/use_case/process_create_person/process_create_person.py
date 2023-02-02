from src.version_one.adapters.repository.repository_interface import RepositoryInterface
from src.version_one.entity.person import Person
from src.version_one.use_case.process_create_person.dto_create_person import PersonDtoInput, PersonDtoOutput


class ProcessCreatePerson():

    def __init__(self,
        repository: RepositoryInterface
    ) -> None:
        self.repository = repository


    def execute(self, input: PersonDtoInput) -> PersonDtoOutput:
        output = PersonDtoOutput()
        try:
            person = Person(
                name= input.name,
                age= input.age,
                genre= input.genre
            )
            self.repository.person_create(person= person)
            self.repository.person_show()

            output.status = 'success'
        except Exception as e:
            output.status = f'error : {str(e)}'
        finally:
            return output