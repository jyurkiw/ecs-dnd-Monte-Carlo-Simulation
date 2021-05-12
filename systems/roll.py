from ecs.lib.system import System
from mcSim.components.dice import DieCode
from mcSim.components.dice import Roll
from mcSim.components.dice import RerollBelowThreshold
from random import randint

class RollSystem(System):
    def __init__(self):
        super().__init__(['DieCode', 'Success'])

    def logic(self, entity):
        # check for an existing roll component. Abort if found.
        if 'Roll' in entity: return

        # get diecode and optional components
        dieCode = entity['DieCode']
        
        rolls = [randint(1, dieCode.numSides) for x in  range(dieCode.numDice)]
        entity.addComponent(Roll(rolls))
