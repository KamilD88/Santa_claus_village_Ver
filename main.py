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
        Village.add_population()


class Santa(Resident):
    def __int__(self, name, age, height, weight, special_skill):
        super().__init__(name, age, height, weight)
        self.special_skill = special_skill
        self.weight = weight * 1.5

    def distribution_of_presents(self):
        time_in_hours = 24
        number_of_laps_of_the_earth = 4
        number_of_presents = 7700000000
        return f"Santa distributed {number_of_presents} presents in {time_in_hours} hours," \
               f"make {number_of_laps_of_the_earth} laps around the world"


class Elf(Resident):
     def __init__(self, manufactured, name, age, height, weight):
         super().__init__(name, age, height, weight)
         self.manufactured = manufactured



class Reindeer(Resident):
    def __init__(self, special_skill, run_speed, name, age, height, weight):
        super().__init__(name, age, height, weight)
        self.special_skill = special_skill
        self.run_speed = run_speed

    def fly(self):
        move_in_air = self.run_speed * 5
        return move_in_air

class Item:
    def __init__(self, size, weight):
        self.size = size
        self.weight = weight


class Sledge(Item):
    def __init__(self, amount_of_magic_dust, amount_of_reindeer, size, weight):
        super().__init__(size, weight)
        self.amount_of_magic_dust = amount_of_magic_dust
        self.amount_of_reindeer = amount_of_reindeer

    def fly(self):
        move_speed = self.amount_of_reindeer * Reindeer.fly()
        self.amount_of_magic_dust =- 1
        return move_speed
class SantaBag(Item):
    def __init__(self, amount_of_presents, size, weight):
        super().__init__(size, weight)
        self.amount_of_presents = amount_of_presents

class ChristmasTree(Item):
    def __init__(self, number_of_lights, number_of_ornaments, state_of_lights, size, weight):
        super().__init__(size, weight)
        self.number_of_lights = number_of_lights
        self.number_of_ornaments = number_of_ornaments
        self.state_of_lights = state_of_lights

    def turn_on_lights(self):
        self.state_of_lights = 1
        return self.state_of_lights

    def turn_off_lights(self):
        self.state_of_lights = 0
        return self.state_of_lights


class Toy(Item):
    def __init__(self, multimedia, destination, size, weight):
        super().__init__(size, weight)
        self.multimedia = multimedia
        self.destination = destination

santa = Village("Santa", "Nowhere", 9992)
print(Santa)
