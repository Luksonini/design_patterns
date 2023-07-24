'''
Try to implement the exact factory from the 
file previous excercise but using the classic Factory Method Pattern.
- this entails thay you need to create a specyfic
factory for each of the concrete Spacesheep class types 
Whey you need to create for example USSEnterprise you will
in fact delegate to USSEnterpriseFactory
This means that the creation will need to be in
some sort of switch to sort out which factory to use.
'''

from enum import Enum, auto
from abc import ABC, abstractmethod


class SpaceSheepType(Enum):
    MilleniumFalcon = auto()
    UNSCInfinity = auto()
    USSEnterprise = auto()
    Serenity = auto()

class SpaseShip(ABC):

    def __init__(self, position, name, size, speed=10):
        self.position = position
        self.name = name
        self.size = size
        self.speed = speed

    @abstractmethod
    def display_info(self):
        pass

class MilleniumFalcon(SpaseShip):

    def display_info(self):
        return f'Type: {SpaceSheepType.MilleniumFalcon.name}, position: {self.position} \
              , size: {self.size}, pseed: {self.speed}' 
    
class UNSCInfinity(SpaseShip):

    def display_info(self):
        return f'Type: {SpaceSheepType.UNSCInfinity.name}, position: {self.position} \
              , size: {self.size}, pseed: {self.speed}' 
    
class USSEnterprise(SpaseShip):

    def display_info(self):
        return f'Type: {SpaceSheepType.USSEnterprise.name}, position: {self.position} \
              , size: {self.size}, pseed: {self.speed}' 
    
class Serenity(SpaseShip):

    def display_info(self):
        return f'Type: {SpaceSheepType.Serenity.name}, position: {self.position} \
              , size: {self.size}, pseed: {self.speed}' 

class SpaceSheepFactory(ABC):

    @abstractmethod
    def create_cpacesheep(position, size, name, speed=10):
        pass

class MilleniumFalconFactory(SpaceSheepFactory):
    def create_cpacesheep(position, size, name, speed=10):
        return MilleniumFalcon(position, size, name, speed)
    
class UNSCInfinityFactory(SpaceSheepFactory):
    def create_cpacesheep(position, size, name, speed=10):
        return UNSCInfinity(position, size, name, speed)
    
class USSEnterpriseFactory(SpaceSheepFactory):
    def create_cpacesheep(position, size, name, speed=10):
        return USSEnterprise(position, size, name, speed)
    
class SerenityFactory(SpaceSheepFactory):
    def create_cpacesheep(position, size, name, speed=10):
        return Serenity(position, size, name, speed)

class SpaceFactoryOfFactories():
    def create_cpacesheep(self, spacesheep_type, position, size, name):
        if spacesheep_type == SpaceSheepType.MilleniumFalcon:
            return MilleniumFalconFactory.create_cpacesheep(position, size, name)
        elif spacesheep_type == SpaceSheepType.UNSCInfinity:
            return UNSCInfinityFactory.create_cpacesheep(position, size, name)
        elif spacesheep_type == SpaceSheepType.USSEnterprise:
            return USSEnterpriseFactory.create_cpacesheep(position, size, name)
        elif spacesheep_type == SpaceSheepType.Serenity:
            return SerenityFactory.create_cpacesheep(position, size, name)
        else:
            raise ValueError('There is no such a type of the spacesheep.')
        
def main():
    uber_factory = SpaceFactoryOfFactories()
    # Test the AnimalFactory by creating different types of animals and passing context data
    sp1 = uber_factory.create_cpacesheep(SpaceSheepType.MilleniumFalcon, (50, 30), (5, 5), 'space1')
    print(sp1.display_info())
    sp2 = uber_factory.create_cpacesheep(SpaceSheepType.UNSCInfinity, (55, 33), (5, 5), 'space2')
    print(sp2.display_info())
    sp3 = uber_factory.create_cpacesheep(SpaceSheepType.USSEnterprise, (10, 20), (5, 5), 'space3')
    print(sp3.display_info())
    sp4 = uber_factory.create_cpacesheep(SpaceSheepType.Serenity, (100, 200), (5, 5), 'space3')
    print(sp4.display_info())

if __name__ == "__main__":
    main()