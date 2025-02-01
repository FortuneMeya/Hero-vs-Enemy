import random
from entity import Entity
from map import Map


class Hero(Entity):
    def __init__(self, name):
        super().__init__(name, max_hp = 50)
        self._loc = [0, 0]  #row, column


    def attack(self, entity):
        damage = random.randint(2, 5)
        entity.take_damage(damage)
        return print(f'{entity.name} attacks {self.name} for {damage} damage')
   
    @property
    def loc(self):
        return self._loc


    def go_north(self):
        dungeon = Map()
        range = (0, len(dungeon) - 1)
        if self._loc[0] > range[0]:
            self._loc[0] -=1
            dungeon.reveal(self._loc)
            return dungeon._map[self._loc[0]][self._loc[1]]
        else:
            return 'o'


    def go_south(self):
        dungeon = Map()
        range = (0, len(dungeon) - 1)
        if self._loc[0] < range[1]:
            self._loc[0] +=1
            dungeon.reveal(self._loc)
            return dungeon._map[self._loc[0]][self._loc[1]]
        else:
            return 'o'


    def go_east(self):
        dungeon = Map()
        range = (0, len(dungeon) - 1)
        if self._loc[1] < range[1]:
            self._loc[1] +=1
            dungeon.reveal(self._loc)
            return dungeon._map[self._loc[0]][self._loc[1]]
        else:
            return 'o'


    def go_west(self):
        dungeon = Map()
        range = (0, len(dungeon) - 1)
        if self._loc[1] > range[0]:
            self._loc[1] -=1
            dungeon.reveal(self._loc)
            return dungeon._map[self._loc[0]][self._loc[1]]
        else:
            return 'o'



