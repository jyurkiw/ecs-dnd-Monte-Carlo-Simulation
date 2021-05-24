from ecs.lib.entity import Entity
from ecs.lib.system import System
from mcSim.components.general import PreRerollDamageTotal
from mcSim.util.tuples import AggregatorValue
from random import randint

class ThresholdRerollSystem(System):
    def __init__(self, threshold, numDice=-1):
        super().__init__(['Roll', 'DieCode'])
        self.threshold = threshold
        self.numDice = numDice
    
    def logic(self, entity):
        roll = entity['Roll'].value
        entity.addComponent(PreRerollDamageTotal(sum(roll)))
        roll.sort()
        dieCode = entity['DieCode']
        numDice = self.numDice

        for i in range(len(roll)):
            if roll[i] >= self.threshold:
                return
            if numDice == 0:
                return
            if roll[i] <= self.threshold:
                roll[i] = randint(1, dieCode.numSides)
                numDice -= 1

def aggregatePreRerollDamage(entity, operationDict):
    if 'PreRerollDamageTotal' in entity:
        operationDict['preRerollDamageTotal'] = operationDict.get('preRerollDamageTotal', 0) + entity['PreRerollDamageTotal'].value

def reportPreRerollDamage(damageTotal, hits, runs, operationDict):
    preRerollDamageTotal = operationDict.get('preRerollDamageTotal', 0)
    return [
        AggregatorValue('preRerollDamageTotal', preRerollDamageTotal),
        AggregatorValue('preRerollDamageAveragePerHit', preRerollDamageTotal / hits),
        AggregatorValue('preRerollDamageAveragePerAttempt', preRerollDamageTotal / runs),
        AggregatorValue('preRerollDamageImprovementPerAttempt', (damageTotal - preRerollDamageTotal) / hits),
        AggregatorValue('preRerollDamageImprovementPerHit', (damageTotal - preRerollDamageTotal) / hits)
    ]