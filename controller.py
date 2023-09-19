import view
import models
import utils

conection = utils.create_conection("localhost", "root", "1234", "animals_app")


def main_menu_controller():
    while True:
        choise = view.main_menu()
        match choise:
            case "1": 
                name, age, animal_class, kind, commands = view.create_new_animal()
                if animal_class == "1":
                    animal = models.PackAnimals(name, age, kind)
                else: animal = models.DomesticAnimals(name, age, kind)
                for command in commands.split(","):
                    animal.add_command(command)
                print("Питомец успешно создан.")
                utils.add_animal(conection, animal)
            case "2": 
                option = view.show_animals()
                match option:
                    case "1": 
                        animals = utils.read_query(conection, "SELECT * FROM animals")
                        for animal in animals:
                            print(animal)
                    case "2":
                        kind = input("Выберите класс питомцев, которых хотите просмотреть:")
                        animals = utils.read_query(conection, f"SELECT * FROM animals WHERE kind = '{kind}'")
                        if animals == []:
                            print("Питомцев такого класса не найдено.")
                        else:
                            for animal in animals:
                                print(animal)
                    case "3":
                        name = input("Введите имя питомца, которого хотите найти:")
                        animals = utils.read_query(conection, f"SELECT * FROM animals WHERE name = '{name}'")
                        if animals == []:
                            print("Питомцев с таким именем не найдено.")
                        else:
                            for animal in animals:
                                print(animal)

            case "3": 
                name = input("Введите имя питомца, которого хотите обучить:")
                animal = utils.read_query(conection, f"SELECT * FROM animals WHERE name = '{name}'")
                if animal == []:
                    print("Питомцев с таким именем не найдено.")
                else:
                    new_commands = input("Введите команды, которые хотите добавить питомцу. Команды вводятся через запятую:")
                    commands = animal[0][4] + ", " + new_commands
                    utils.read_query(conection, f"UPDATE animals SET commands = '{commands}' WHERE name = '{name}'")
                    print("Команды успешно добавлены.")
            case "4": 
                name = input("Введите имя питомца, которого хотите удалить:")
                animal = utils.read_query(conection, f"SELECT * FROM animals WHERE name = '{name}'")
                if animal == []:
                    print("Питомцев с таким именем не найдено.")
                else:
                    utils.read_query(conection, f"DELETE FROM animals WHERE name = '{name}'")
                    print("Питомец успешно удален.")


            case "5":
                print("До свидания!")
                break

    

                    
                    




        


    