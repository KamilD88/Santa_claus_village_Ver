class Vilage:
    def __init__(self, name, location, population, area_bulding):
        self.name = name
        self.location = location
        self.population = population
        self.area_building = area_bulding


class Building:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area


class Workshop(Building):
    def __init__(self, manufactured_toys, working_elves, name, population, area):
        super().__init__(name, population, area)
        self.manufactured_toys = manufactured_toys
        self.working_elves = working_elves


class House(Building):
    def __init__(self, bed_capacity, residents):
        self.bed_capacity = bed_capacity
        self.residents = residents


class Resident:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class Human(Resident):
    pass


class Elf(Resident):
    pass


class MagicElf(Elf):
    pass


class Reindeer(Resident):
    pass


class SantaReindeer(Reindeer):
    pass


class Item():
    pass


class Sledge(Item):
    pass


class SantaBag(Item):
    pass


class ChristmasTree(Item):
    pass


class Toy(Item):
    pass
