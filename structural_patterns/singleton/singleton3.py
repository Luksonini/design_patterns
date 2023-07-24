from singleton1 import Singleton
from multiprocessing import Process


def f():
    instance = Singleton()
    print(id(instance))
    return instance

if __name__ == '__main__':
    p1 = Process(target=f)
    p2 = Process(target=f)
    p3 = Process(target=f)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    

