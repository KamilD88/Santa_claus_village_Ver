class Village:
    def __init__(self, name, location, population):
        self.max_population = 999
        self.name = name
        self.location = location
        self.population = population
        if population > self.max_population:
            raise ValueError(f"Population limit is {self.max_population}")

    def __str__(self):
        return f"Village name: {self.name} \nLocation: {self.location} \nPopulation: {self.population}"

    def add_population(self):
        if self.population < self.max_population:
            self.population += 1
        else:
            raise ValueError(f"Max population is {self.max_population}. "
                             f"You can not add more residents to village {self.name}")


class Building:
    def __init__(self, name, capacity, residents):
        self.name = name
        self.capacity = capacity
        self.residents = residents



class Workshop(Building):
    def __init__(self, name, capacity, residents,  manufactured_toys):
        super().__init__(name, capacity, residents)
        self.manufactured_toys = manufactured_toys
        self.working_elves = residents


class House(Building):
    def __init__(self, name, capacity, residents, b):
        super().__init__(name, capacity, residents)


class Resident:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        Village.add_population(self)


class Santa(Resident):
    pass


class Elf(Resident):
    pass


class MagicElf(Elf):
    pass


class Reindeer(Resident):
    pass


class SantaReindeer(Reindeer):
    pass


class Item:
    pass


class Sledge(Item):
    pass


class SantaBag(Item):
    pass


class ChristmasTree(Item):
    pass


class Toy(Item):
    pass


santa = Village("Santa", "Nowhere", 9992)
print(Santa)
