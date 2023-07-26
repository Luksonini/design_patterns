'''
Working with the Factory Method Pattern Exercise #2
You task here will be to create a parameterized version of the Factory Method pattern for 
creating different types of animals with some context data.
The factory will receive a parameter to determine which animal type to create and a 
dictionary containing the context data for initializing the animal objects.

Task: Create an Animal Factory that can create different types of animals 
(e.g., Dog, Cat, Fish) based on the input parameter and context data.

Create an abstract Animal class.

Create concrete animal classes, e.g., Dog, Cat, and Fish, that inherit from the Animal class.

Create an AnimalFactory class with a create_animal method that takes a parameter to 
determine which type of animal to create and a dictionary containing context
 data for initializing the animal objects.

Add such context data such as name, age to initialize the Animal data with. 
NOTE that we are asking you to use Dictionary as the data bag for 
the initialization of each Animal.

Test the AnimalFactory class to create different types of animals.
'''


from abc import ABC, abstractmethod
from enum import Enum

# Step 0: Create an enumeration for animal types
class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    FISH = "Fish"

# Step 1: Create an abstract Animal class
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self) -> str:
        pass

# Step 2: Create concrete animal classes
class Dog(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def get_info(self):
        return f'Type: {AnimalType.DOG.value}, Name: {self.name}, Age: {self.age}'


class Cat(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def get_info(self):
        return f'Type: {AnimalType.CAT.value}, Name: {self.name}, Age: {self.age}'

class Fish(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def get_info(self):
        return f'Type: {AnimalType.FISH.value}, Name: {self.name}, Age: {self.age}'

# Step 3: Create an AnimalFactory class
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: AnimalType, context: dict) -> Animal:
        # Implement the logic to create an animal based on the animal_type parameter and context data
        if animal_type == AnimalType.DOG:
            return Dog(context['name'], context['age'])
        elif animal_type == AnimalType.CAT:
            return Cat(context['name'], context['age'])
        elif animal_type == AnimalType.FISH:
            return Fish(context['name'], context['age'])
        else:
            raise ValueError()

# Step 4: Test the AnimalFactory class
def main():
    animal_factory = AnimalFactory()
    # Test the AnimalFactory by creating different types of animals and passing context data
    dog = animal_factory.create_animal(AnimalType.DOG, context = {'name' : 'Max', 'age' : 5})
    print(dog.get_info())
    cat = animal_factory.create_animal(AnimalType.CAT, context = {'name' : 'Kitek', 'age' : 2})
    print(cat.get_info())
    fish = animal_factory.create_animal(AnimalType.FISH, context = {'name' : 'Fishman', 'age' : 100})
    print(fish.get_info())

if __name__ == "__main__":
    main()
