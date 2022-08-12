from random import randint

class GenericStatted:
    def __init__(self, name:str) -> None:
        # User's display name
        self.name = name
        # User's Stats
        self.stats =  GenericStatted.generate_stat_block(3)

    def __repr__(self) -> str:
        return f'Entity Object: {self.name}'

    def unarmed_attack(self, target):
        if target.stats:
            if randint(1, 20) >= target.stats["armor_class"]:
                damage = randint(1, self.stats["str"])
                target.stats["cur_health"] -= damage
                print(f'{self.name} hit and did {damage} damage!')

            else:
                print('You missed!')

    @staticmethod
    def generate_stat_block(volatility:int = 1) -> dict:
        stat_block = {
            # XP and Level
            "xp" : 0,
            "xp_to_level" : 100,
            "level" : 1,
            # Current well-being stats
            "max_health" : 100,
            "cur_health" : 100,
            "max_mana" : 20,
            "cur_mana" : 20,
            # COMBAT
            "initiative" : 10,
            "armor_class" : 10,
            # Stat Block
            "str" : 10 + randint(-volatility, volatility),
            "dex" : 10 + randint(-volatility, volatility),
            "int" : 10 + randint(-volatility, volatility),
            "wis" : 10 + randint(-volatility, volatility),
            "con" : 10 + randint(-volatility, volatility),
            "cha" : 10 + randint(-volatility, volatility)
        }
        return stat_block