class Village:
    def __init__(self, name, location, population):
        self.max_population = 999
        self.name = name
        self.location = location
        self.population = population
        if population or self.population > self.max_population:
            raise ValueError(f"Population limit is {self.max_population}")

    def __str__(self):
        return f"Village name: {self.name} \nLocation: {self.location} \nPopulation: {self.population}"

    def add_population(self):
        self.population += 1


class Building:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"name: {self.name}, capacity: {self.capacity}"


class Workshop(Building):
    def __init__(self, name, capacity, workers, manufactured_toys):
        super().__init__(name, capacity,)
        self.manufactured_toys = manufactured_toys
        self.working_elves = workers

    def __str__(self):
        return f"name: {self.name}, capacity: {self.capacity}, working elves: {self.working_elves}" \
               f"toy production: {self.manufactured_toys} - {Workshop.produce_toys_per_day(self)}quantity per day"

    def produce_toys_per_day(self):
        hour_production = 30 * self.working_elves
        day_production = hour_production * 24
        return day_production


class House(Building):
    def __init__(self, name, capacity, residents):
        super().__init__(name, capacity)
        self.residents = residents


class Resident:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.add = Village.add_population(self)


class Santa(Resident):
    def __int__(self, name, age, height, weight, special_skills=[]):
        super().__init__(name, age, height, weight)
        self.special_skill = special_skills
        self.weight = weight * 1.5

    def distribution_of_presents(self):
        time = 8
        number_of_laps_of_the_earth = 4
        number_of_presents = 7700000000
        return f"Santa distributed {}"


class Elf(Resident):
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
