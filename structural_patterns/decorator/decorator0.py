# from abc import ABC, abstractmethod

# class MainClass(ABC):

#     @abstractmethod
#     def some_method(self):
#         pass

# class Myclass(MainClass):

#     def some_method(self):
#         print(self, 'sth')

# class Dectorator(MainClass):

#     def __init__(self, obj):
#         self.obj = obj

#     @abstractmethod
#     def some_method(self):
#         pass

# class ConcretDecorator(Dectorator):
#     def some_method(self):
#         print('sth extra')
#         self.obj.some_method()
#         print('sth more extra')

# my_class = Myclass()
# my_class.some_method()
# concret_decorator = ConcretDecorator(my_class)
# concret_decorator.some_method()



class Myclass():

    def some_method(self):
        print(self, 'sth')

class Dectorator(Myclass):

    def __init__(self, obj):
        self.obj = obj

    def some_method(self):
        print('sth extra')
        self.obj.some_method()
        print('sth more extra')

my_class = Myclass()
decorator = Dectorator(my_class)
decorator.some_method()