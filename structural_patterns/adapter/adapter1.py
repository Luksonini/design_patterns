class Dog():
    def __init__(self, age, sex, breed, marking):
        self.age = age
        self.sex = sex
        self.breed = breed
        self.marking = marking

    def run(self):
        print('I run')

    def bark(self):
        print('How how')


class Child():
    def __init__(self, age, sex, race):
        self.age = age
        self.sex = sex
        self.race = race

    def walk(self):
        pass

    def speak(self, sth):
        print(sth)

dog1 = Dog(8, 'm', 'kundel', '')
child1 = Child(8, 'm', 'white')

#adapter child in the dog costume 
#musi przyjąć dziecko i chcemy żeby wydawało sie że posiada te same metody
class DogAdapter():
    def __init__(self, child):
        self.child = child

    def bark(self):
        print('How how')

    def say_something(self, sth):
        self.child.speak(sth)

# dog1.bark()
# child1.say_something('How how')
dog2 = DogAdapter(child1)
dog2.bark()
dog2.say_something('something')
