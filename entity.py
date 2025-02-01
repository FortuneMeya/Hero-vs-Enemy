from abc import ABC, abstractmethod

class Entity(ABC):
    """
    A Class to represent an Entity
    -----
    Attributes:
    _name(str) - name of the user/enemy
    _max_hp(int) - max hp of the user/enemy
    hp(int) - current hp of the user/enemy
    """

    def __init__(self,name,max_hp):
        """initialize _name, _max_hp, and hp"""
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    @property
    def name(self):
        """Get the name"""
        return self._name

    @property
    def hp(self):
        """Get the hp"""
        return self._hp

    def take_damage(self, dmg):
        """Subtract damage from hp"""
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0
        return self._hp

    def heal(self):
        """Restores the entity’s hp to max_hp."""
        self._hp = self._max_hp
        return self._hp

    def __str__(self):
        """Print in format of Name\nHP: hp / max_hp"""
        return f'{self._name}\nHP: {self._hp}/{self._max_hp}'

    @abstractmethod
    def attack(self, entity):
        """Abstract method that passes attack"""
        pass


