class Singleton:

    _instances = []
    _actual = -1

    def __new__(cls, *args, **kwargs):
        if len(cls._instances) < 3:
            singleton = super().__new__(cls, *args, **kwargs)
            cls._instances.append(singleton)
        cls._actual += 1
        cls._actual = cls._actual % 3
        return cls._instances[cls._actual]
    

a = Singleton()
b = Singleton()
c = Singleton()
d = Singleton()

print(id(a))
print(id(b))
print(id(c))
print(id(d))

   