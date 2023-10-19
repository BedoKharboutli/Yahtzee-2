import random


class BoardGameMaterial:
    """Used to store all board game materials in one class"""


class Die(BoardGameMaterial):
    def __init__(self):
        self.value = random.randint(1, 6)

    def __str__(self):
        return "Dice shows " + str(self.value)

    @staticmethod
    def Roll():
        value = random.randint(1, 6)
        return value

    # @staticmethod     uneccesary function
    # def die_reroll():
    #     return Die.DieRoll()
