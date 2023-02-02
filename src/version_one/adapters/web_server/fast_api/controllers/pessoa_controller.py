

from src.version_one.adapters.repository.list_python import ListPython
from src.version_one.use_case.process_create_person.create_person_dto import PessoaDtoInput
from src.version_one.use_case.process_create_person.process_create_person import ProcessCreatePerson

def controller():
    repository = ListPython()
    use_case = ProcessCreatePerson(
        repository=repository
    )

    input = PessoaDtoInput()
    input.name = 'Vitor',
    input.idade = 23
    input.genero = 'Masculino'

    output = use_case.execute(input=input)

    print(output.status)