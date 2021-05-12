from ecs.lib.system import System
from mcSim.components.dice import D20Roll

class CritSystem(System):
    def __init__(self):
        super().__init__(['D20Roll', 'DieCode'])
    
    def logic(self, entity):
        roll = entity['D20Roll'].value

        if roll == 20:
            entity['DieCode'].numDice *= 2

            
