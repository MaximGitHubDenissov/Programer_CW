class Animals:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.command = []
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    def add_command(self, command):
        self.command.append(command)

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}, Commands: {self.command}"
    
class PackAnimals(Animals):
    default_kind = "Unknown Pack Animal"
    def __init__(self, name, age, kind):
        super().__init__(name, age)
        if kind:
            self.kind = kind
        else:
            self.kind = PackAnimals.default_kind
       
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Type: {self.kind}, Commands: {self.command}"
    
    
class DomesticAnimals(Animals):
    default_kind = "Unknown Domestic Animal"
    def __init__(self, name, age, kind):
        super().__init__(name, age)
        if kind:
            self.kind = kind
        else:
            self.kind = DomesticAnimals.default_kind
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Type: {self.kind}, Commands: {self.command}"
    
    
    


   