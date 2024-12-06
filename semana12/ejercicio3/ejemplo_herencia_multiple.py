class Mammals:
    def mammal_description(self):
        print("Mammals can give direct birth")


class FourLeggedAnimal:
    def four_legged_animal_description(self):
        print("This animal can walk with its four legs")


class Elephant (Mammals,FourLeggedAnimal):
    pass


animal = Elephant()
animal.mammal_description()
animal.four_legged_animal_description()