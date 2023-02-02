from src.adapters.repository.memory.list_adapter import ListAdapter
from src.use_case.process_create_person.dto_create_person import PersonDtoInput
from src.use_case.process_create_person.process_create_person import ProcessCreatePerson

def create_person(name: str, age: int, genre: str):
    repository = ListAdapter()
    use_case = ProcessCreatePerson(
        repository=repository
    )

    input = PersonDtoInput()
    input.name = name
    input.age = age
    input.genre = genre

    output = use_case.execute(input=input)
    print(output.status)