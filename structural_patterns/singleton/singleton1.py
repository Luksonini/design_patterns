class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
           instance = super().__new__(cls, *args, **kwargs)
           cls._instance = instance
        return cls._instance

if __name__ == '__main__':
    x = Singleton()
    y = Singleton()

    print(id(x))
    print(id(y))
    print(x is y)