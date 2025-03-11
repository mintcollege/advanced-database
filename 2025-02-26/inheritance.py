class Character:
    id: int
    alignment: str = 'hero'
    name: str
    gender: str
    age: int
    status: str = 'alive'
    nationality: str = 'Filipino'
    max_health: int = 100
    skin: str = ''


    def __init__(self, id: int, name: str, age: int, gender: str):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender


    def __str__(self):
        return f'<Character {self.id}: {self.name}>'


    def attack(self):
        print('USER IS ATTACKING!')


class Human(Character):
    type_of_attack: str
    attack_type: str = ''


    def __init__(self, id: int, name: str, age: int, gender: str, type_of_attack: str):    # noqa
        super().__init__(id, name, age, gender)
        self.type_of_attack = type_of_attack

    def attack(self):
        print('HUMAN DOES MELEE ATTACK')


    def melee_attack(self): # noqa
        if self.type_of_attack != 'melee':
            raise Exception(f'Can only do melee attack. Tried to input {self.attack_type}')
        print('Melee attack')


    def range_attack(self): # noqa
        if self.type_of_attack != 'range':
            raise Exception('Cannot do melee attack.')
        print('Range attack')

    def human_attack(self):
        print('ATTACK ONLY FOR HUMANS')


class Undead(Human):
    def attack(self):
        print('UNDEAD IS TRYING TO ATTACK')

    def human_attack(self):
        # raise Exception('Only humans can make this attack.')
        pass


class Void(Character):
    pass


# ranger = Character(1, 'Ranger', 20, 'male')
# ranger.attack()

sam = Human(2, 'Sam', 45, 'male', 'range')
# sam.type_of_attack = 'range'
# sam.melee_attack()
# sam.range_attack()

sally = Human(3, 'Sally', 23, 'female', 'melee')
# sally.type_of_attack = 'melee'
# sally.range_attack()
# sally.melee_attack()
# sally.human_attack()

nthnsda = Undead(4, 'Nthnsda', 1000, 'unknown', 'melee')
nthnsda.human_attack()




class Vehicle:
    wheels: int = 4


class DragRacer(Vehicle, Character):
    pass


class AllTerrain(Vehicle):
    pass




