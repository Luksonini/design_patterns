class Car:
    def __init__(self, brand, model, engine, gearbox, body_type, license_plate,
                 owner, **kwargs):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.gearbox = gearbox
        self.body_type = body_type
        self.license_plate = license_plate
        self.owner = owner
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        summary = []
        for key, val in vars(self).items():
            summary.append(f'{key}: {val}')
        return '\n'.join(summary)
    
from copy import deepcopy

class Prototype:

    def __init__(self):

        self.objs = dict()

    def add_prototype(self, id_, obj):
        self.objs[id_] = obj

    def del_prototype(self, id_):
        del self.objs[id_]

    def clone(self, id_, **kwargs): #opcjonalnie dodatkowe atrybuty
        if id_ in self.objs:
            instance = deepcopy(self.objs[id_])
            for key in kwargs:
                setattr(instance, key, kwargs[key])
            return instance
        else:
            raise ModuleNotFoundError



mycar = Car('BMW', 'A', 'diesel', 'manual', 'sedan', 
            'LBL4466', 'Lukson', color = 'white')

print(mycar)
# now new the same car with different id plate and owner
prototype = Prototype()
prototype.add_prototype('lukson_car', mycar)
new_car = prototype.clone('lukson_car', license_plate = 'KR233455', owner = 'Zosson')
print('*' * 30)
print(new_car)