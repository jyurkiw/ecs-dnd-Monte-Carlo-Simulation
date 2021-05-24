from ecs.lib.system import System

class CritSystem(System):
    def __init__(self, margin=0, multiplier=2, extraDice=0):
        super().__init__(['D20Roll', 'DieCode'])
        self.margin = margin
        self.multiplier = multiplier
        self.extraDice = extraDice
    
    def logic(self, entity):
        roll = entity['D20Roll'].value

        if roll >= 20 - self.margin:
            entity['DieCode'].numDice *= self.multiplier
            entity['DieCode'].numDice += self.extraDice