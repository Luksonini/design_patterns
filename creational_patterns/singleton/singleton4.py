class Singleton(type):
    _instance = None
    
    def __call__(cls, *args, **kwargs):
        if not cls._instance:
           instance = super().__call__(*args, **kwargs)
           cls._instance = instance
        return cls._instance
    

class B(metaclass = Singleton):
    important = 'sth important'

cl_1 = B()
cl_2 = B()
print(id(cl_1), id(cl_2))
print(cl_1.important, cl_2.important)


class B():

    important = 'sth important'

class A(B, metaclass=Singleton):
    pass

a = B()
print(id(a))
print(a.important)