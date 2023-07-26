
#Zacznijmy od zdefiniowania "Product", czyli naszego obiektu domu:
class House:
    def __init__(self):
        self.rooms = None
        self.floors = None
        self.garage = None
        self.garden = None
        self.swimming_pool = None

#Następnie zdefiniujemy interfejs "Builder":
from abc import ABC, abstractmethod

class HouseBuilder(ABC):
    @abstractmethod
    def set_rooms(self, rooms):
        pass

    @abstractmethod
    def set_floors(self, floors):
        pass

    @abstractmethod
    def set_garage(self, garage):
        pass

    @abstractmethod
    def set_garden(self, garden):
        pass

    @abstractmethod
    def set_swimming_pool(self, swimming_pool):
        pass

#Teraz utworzymy "Concrete Builder":
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def set_rooms(self, rooms):
        self.house.rooms = rooms
        return self

    def set_floors(self, floors):
        self.house.floors = floors
        return self

    def set_garage(self, garage):
        self.house.garage = garage
        return self

    def set_garden(self, garden):
        self.house.garden = garden
        return self

    def set_swimming_pool(self, swimming_pool):
        self.house.swimming_pool = swimming_pool
        return self

    def build(self):
        return self.house
#Na końcu tworzymy "Director". W tym przypadku zastosujemy metodę łańcuchową, więc nie będzie potrzeby tworzyć klasy Director. 
# Metoda łańcuchowa pozwala nam łączyć wywołania metod, co ułatwia budowę skomplikowanego obiektu.
def main():
    builder = ConcreteHouseBuilder()
    house = (builder.set_rooms(5)
                   .set_floors(2)
                   .set_garage(True)
                   .set_garden(True)
                   .set_swimming_pool(False)
                   .build())
    print(house.rooms)  # 5
    print(house.floors)  # 2
    print(house.garage)  # True
    print(house.garden)  # True
    print(house.swimming_pool)  # False


if __name__ == "__main__":
    main()