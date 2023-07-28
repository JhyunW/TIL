class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1


class Dog(Animal):
    def bark(self):
        print('멍 멍 !')


class Cat(Animal):
    def meow(self):
        print('야 옹 !')
        
class Pet(Dog, Cat):
    def __init__(cls, sound):
        cls.sound = sound
    def access_num_of_animal(cls):
        cls.num_of_animal
    
    def make_sound(cls):
        print(cls.sound)

    def play(cls):
        print('애완동물과 놀기')


pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
