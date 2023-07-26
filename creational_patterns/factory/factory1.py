'''
Working with the Factory Method Pattern Exercise #1
In this exercise you will create a simplified, parameterized version of the Factory 
Method pattern for creating different types of vehicles.



The factory will receive a parameter to determine which vehicle type to create.

Your Task is to: Create a Vehicle Factory that can create different types of vehicles 
(e.g., Car, Motorcycle, Bicycle) based on the input parameter. Make sure that the input 
parameters are defined as an enumeration.

Create an abstract Vehicle class.

Create concrete vehicle classes, e.g., Car, Motorcycle, and Bicycle, that inherit from the 
Vehicle class.

Create a VehicleFactory class with a create_vehicle method that takes a parameter to 
determine which type of vehicle to create.

Test the VehicleFactory class to create different types of vehicles.

Ten temat jest omawian
'''

from abc import ABC, abstractmethod
from enum import Enum

# Step 0: Create an enumeration for vehicle types
class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"

# Step 1: Create an abstract Vehicle class
class Vehicle(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

# Step 2: Create concrete vehicle classes
class Car(Vehicle):
    def get_name(self):
        return VehicleType.CAR.value

class Motorcycle(Vehicle):
    def get_name(self):
        return VehicleType.MOTORCYCLE.value

class Bicycle(Vehicle):
    def get_name(self):
        return VehicleType.BICYCLE.value

# Step 3: Create a VehicleFactory class
class VehicleFactory:
    def create_vehicle(self, vehicle_type: VehicleType) -> Vehicle:
        if vehicle_type == VehicleType.CAR:
            return Car()
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle()
        elif vehicle_type == VehicleType.BICYCLE:
            return Bicycle()  # To było brakujące
        else:
            raise ValueError()

    
# Step 4: Test the VehicleFactory class
def main():
    vehicle_factory = VehicleFactory()
    bike = vehicle_factory.create_vehicle(VehicleType.CAR)  # Tutaj zmieniamy 'Car' na VehicleType.CAR
    print(bike.get_name())

if __name__ == "__main__":
    main()