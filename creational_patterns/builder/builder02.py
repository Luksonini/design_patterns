'''
Working with the Builder Pattern Exercise
In this exercise you will implement the Builder Design Pattern for constructing a customized 
computer system.

Task: Implement the Builder Design Pattern to create a custom computer system.

Instructions:

Define a class Computer with attributes: processor, memory, storage, graphics_card, 
operating_system, and extras.

Initialize these attributes in the __init__ method.

Create an abstract class ComputerBuilder with the following abstract methods:

add_processor, add_memory, add_storage, add_graphics_card, add_operating_system, and add_extras.

Implement a concrete class CustomComputerBuilder that inherits from ComputerBuilder.

This class should override the abstract methods and set the attributes of a Computer object.

Create a class ComputerDirector that takes a ComputerBuilder instance and has a method 
build_computer that calls the add_* methods of the ComputerBuilder in the desired order.

Instantiate a CustomComputerBuilder, pass it to the ComputerDirector, and create a 
computer using the build_computer method.

Test your code.
'''



from abc import ABC, abstractmethod

class Computer:
    def __init__(self):
        self.processor = None
        self.memory = None
        self.storage = None
        self.graphics_card = None
        self.operating_system = None
        self.extras = None

class ComputerBuilder(ABC):
    @abstractmethod
    def add_processor(self):
        pass

    @abstractmethod
    def add_memory(self):
        pass

    @abstractmethod
    def add_storage(self):
        pass

    @abstractmethod
    def add_graphics_card(self):
        pass

    @abstractmethod
    def add_operating_system(self):
        pass

    @abstractmethod
    def add_extras(self):
        pass

class CustomComputerBuilder(ComputerBuilder):
    def __init__(self):
       self.computer = Computer()

    def add_processor(self, processor):
        self.computer.processor = processor

    def add_memory(self, memory):
        self.computer.memory = memory

    def add_storage(self, storage):
        self.computer.storage = storage

    def add_graphics_card(self, graphics_card):
        self.computer.graphics_card = graphics_card

    def add_operating_system(self, operating_system):
        self.computer.operating_system = operating_system

    def add_extras(self, extras):
        self.computer.extras = extras

class ComputerDirector:
    def __init__(self, builder):
        # Initialize the builder instance
        self.builder = builder


    def build_computer(self, specs):
        if 'processor' in specs:
            self.builder.add_processor(specs['processor'])
        if 'memory' in specs:
            self.builder.add_memory(specs['memory'])
        if 'storage' in specs:
            self.builder.add_storage(specs['storage'])
        if 'graphics_card' in specs:
            self.builder.add_graphics_card(specs['graphics_card'])
        if 'operating_system' in specs:
            self.builder.add_operating_system(specs['operating_system'])
        if 'extras' in specs:
            self.builder.add_extras(specs['extras'])
        return self.builder.computer


# Helper function to test the computer building process
def test_computer_building(specs, expected_output):
    builder = CustomComputerBuilder()
    director = ComputerDirector(builder)
    director.build_computer(specs)
    computer = builder.computer
    assert computer.__dict__ == expected_output, f"Expected {expected_output}, but got {computer.__dict__}"

# Test cases
test_specs = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

expected_output = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

test_computer_building(test_specs, expected_output)

print("All tests passed!")
