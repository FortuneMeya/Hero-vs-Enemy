import random
from entity import Entity


class Enemy(Entity):
    def __init__(self):
        name_list = ['Goblin','Vampire', 'Ghoul','Skeleton', 'Zombie']
        self._name = random.choice(name_list)
        self._max_hp = random.randint(4,8)
        super().__init__(self._name, self._max_hp)


    def attack(self,entity):
        damage = random.randint(1,4)
        entity.take_damage(damage)
        return print(f'{self.name} attacks {entity.name} for {damage} damage')


