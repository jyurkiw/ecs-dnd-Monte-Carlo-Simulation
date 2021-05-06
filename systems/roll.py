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
        rerollBelowThreshold = None
        if 'RerollBelowThreshold' in entity:
            rerollBelowThreshold = entity['RerollBelowThreshold']
            rolls = self.handleRerolls(rolls, dieCode.numSides, rerollBelowThreshold)
        
        entity.addComponent(Roll(rolls))

    def handleRerolls(self, rolls, numSides, rerollBelowThreshold):
        rolls.sort()
        rerolls = [randint(1, numSides) for x in rolls[:rerollBelowThreshold.numRerolls] if x <= rerollBelowThreshold.rerollThreshold]
        return rerolls + rolls[len(rerolls):]
