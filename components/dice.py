from ecs.lib.component import Component
from ecs.components.valueComponent import ValueComponent
from random import randint

# Value Components
class D20Roll(ValueComponent):
    def __init__(self): self.value = randint(1, 20)

class Roll(ValueComponent):
    def __init__(self, diceRolls):
        if type(diceRolls) != list:
            raise Exception("diceRolls type must be a list of integers.")
        super().__init__(diceRolls)

# Complex Components
class DieCode(Component):
    def __init__(self, numDice, numSides, bonus=0):
        self.numDice = numDice
        self.numSides = numSides
        self.bonus = bonus

class RerollBelowThreshold(Component):
    def __init__(self, numRerolls, rerollThreshold):
        self.numRerolls = numRerolls
        self.rerollThreshold = rerollThreshold