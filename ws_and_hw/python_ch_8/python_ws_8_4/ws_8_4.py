class Pet(Dog, Cat):
    def __init__(self, sound):
        self.sound = sound

    def play(self):
        print('애완동물과 놀기')

    def make_sound(self):
        print(self.sound)

    @classmethod
    def access_num_of_animal(cls):
        return cls.num_of_animal
    pass

pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
print(Animal.num_of_animal)
