from src.version_one.controllers.person_controller import create_person

def cmd_create_person():
    print("\nPerson registration")
    print("Enter your name : ")
    name = input()

    print("Enter your age : ")
    age = input()

    print("Enter your genre : ")
    genre = input()

    create_person(
        name=name,
        age= int(age),
        genre= genre
    )