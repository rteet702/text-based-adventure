from ..generic_classes.generic_statted import GenericStatted
from random import randint

class Goblin(GenericStatted):
    def __init__(self, difficulty:int = 1) -> None:
        super().__init__(self.name)
        self.name = 'Goblin'
        self.stats = Goblin.generate_stat_block(difficulty)

    @staticmethod
    def generate_stat_block(volatility:int = 1) -> dict:
        stat_block = {
            # Current well-being stats
            "max_health" : randint(10,30),
            "cur_health" : stat_block["max_health"],
            # COMBAT
            "initiative" : 10,
            "armor_class" : 10,
            # Stat Block
            "str" : 10 + randint(0, volatility),
            "dex" : 10 + randint(0, volatility),
            "int" : 10 + randint(0, volatility),
            "wis" : 10 + randint(0, volatility),
            "con" : 10 + randint(0, volatility),
            "cha" : 10 + randint(0, volatility)
        }
        return stat_block