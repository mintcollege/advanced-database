# Python 3.12
# from typing import List
import math

class Game:
    name: str
    genre: list
    publisher: str
    id: int
    age_rating: str = 'PG-13'
    developer: list = []
    is_online: bool = None
    legal_data: dict = {}


    def __init__(self, id: int, name: str, publisher: str, genre: list):
        self.id = id  # From the db
        self.name = name
        self.publisher = publisher
        self.genre = genre
        self.legal_data = {
            'copyright': 2025,
            "tos": 'https://tos'
        }


    def launch_now(self):
        print('GAME IS NOW LIVE!')


# mario_kart = Game()
valo = Game(123, 'Volarant', 'Riot Games', ['shooter', 'strategy', 'first-person'])
valo.legal_data = {
    'copyright': 2026,
    'tos': 'https://facebook.com/tos'
}
print(valo.legal_data)
valo.launch_now()


# lol = Game()
# lol.name = 'League of Legends'
# lol.publisher = 'Riot Games'
# lol.genre = ['moba', 'strategy', 'rpg', 'isometric']
# print(lol.name, lol.publisher, lol.genre)

# def add(a: int, b: int) -> int:
#     return a + b
#
#
# add('111111', 2)


class Gun:
    id: int
    name: str
    weight: int
    damage: int
    range: int
    recoil: int
    # skin: Skin
    attachmets: dict

    def __init__(self, weight):
        self.weight = weight

    @classmethod
    def create_jackal(cls):
        gun = cls(20)
        gun.damage = 99
        gun.range = 15
        gun.name = 'Jackal'
        return gun


class Skin:
    id: int


# mp5 = Gun()
# mp5.id = 1
# mp5.weight = 50
# mp5.skin = Skin()
jackal_gun = Gun.create_jackal()
print(jackal_gun.name)
print(math.pi)