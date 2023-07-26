

'''
Create an abstract class called SpaseShip 
which will simulate the spaceship for video game

you can assume such simple properties as:
- position (x, y), size(x, y), displayName - name str, speed = 10
Create a number of concrete classes such as:
MilleniumFalcon
UNSCInfinity
USSEnterprise
Serenity
uning the Simple Factory Method create a factory 
implementation that will create each of there instances

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

class SimpleSpaceSheepFactory():

    @staticmethod
    def create_cpacesheep(spacesheep_type, position, size, name, speed=10):
        if spacesheep_type == SpaceSheepType.MilleniumFalcon:
            return MilleniumFalcon(position, size, name, speed)
        elif spacesheep_type == SpaceSheepType.UNSCInfinity:
            return UNSCInfinity(position, size, name, speed)
        elif spacesheep_type == SpaceSheepType.USSEnterprise:
            return USSEnterprise(position, size, name, speed)
        elif spacesheep_type == SpaceSheepType.Serenity:
            return Serenity(position, size, name, speed)
        else:
            raise ValueError('There is no such a type of the spacesheep.')
        
def main():
    spacesheep_factory = SimpleSpaceSheepFactory()
    # Test the AnimalFactory by creating different types of animals and passing context data
    sp1 = spacesheep_factory.create_cpacesheep(SpaceSheepType.MilleniumFalcon, (50, 30), (5, 5), 'space1')
    print(sp1.display_info())
    sp2 = spacesheep_factory.create_cpacesheep(SpaceSheepType.UNSCInfinity, (55, 33), (5, 5), 'space2')
    print(sp2.display_info())
    sp3 = spacesheep_factory.create_cpacesheep(SpaceSheepType.USSEnterprise, (10, 20), (5, 5), 'space3')
    print(sp3.display_info())
    sp4 = spacesheep_factory.create_cpacesheep(SpaceSheepType.Serenity, (100, 200), (5, 5), 'space3')
    print(sp4.display_info())

if __name__ == "__main__":
    main()
