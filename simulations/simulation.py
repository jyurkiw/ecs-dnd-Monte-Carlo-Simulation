from abc import ABC, abstractclassmethod
from collections import namedtuple
from ecs.lib.entity import Entity
from mcSim.components.dice import D20Roll, DieCode
from mcSim.components.rollBonus import RollBonus
from mcSim.components.targetNumber import TargetNumber
from random import choices

ValueWeight = namedtuple('ValueWeight', ['value', 'weight'])
RUNS = 100000

class Simulation(ABC):
    """A base simulation framework. Cannot be instantiated.
    """
    def __init__(self, runs, systems):
        self.runs = runs
        self.systems = systems

    @abstractclassmethod
    def entityGenerator(self):
        raise Exception("Simulation.entityGenerator needs to be overriden.")

    def runSimulation(self):
        [entity for entity in self.entityGenerator()]
        print('Simulation populated')
        for system in self.systems:
            system.run()
        print('Simulation complete')

class TargetNumberSimulation(Simulation):
    def __init__(self, runs, systems):
        super().__init__(runs, systems)
        self.reportSystem = None
        self.rollBonuses = []
        self.targetNumber = 0
        self.numSides = 0
        self.numDice = 0

    def setReportSystem(self, reportSystem):
        self.reportSystem = reportSystem
        return self
    
    def addRollBonus(self, rollBonus, weight):
        self.rollBonuses.append(ValueWeight(rollBonus, weight))
        return self
    
    def setTargetNumber(self, targetNumber):
        self.targetNumber = targetNumber
        return self

    def setDieCode(self, numDice, numSides):
        self.numDice = numDice
        self.numSides = numSides
        return self
    
    def entityGenerator(self, additionalSteps=None):
        """Generate a standard entity for a target number simulation.
        additionalSteps is optional and has the following definition:
            additionalSteps(Simulation, Entity)
            Entity is altered directly by additionalSteps.
            Return value is ignored.
        """
        bonuses = [r.value for r in self.rollBonuses]
        weights = [ b.weight for b in self.rollBonuses]

        for i in range(self.runs):
            e = Entity()
            e.addComponent(D20Roll())
            e.addComponent(RollBonus(choices(bonuses, weights)[0]))
            e.addComponent(TargetNumber(self.targetNumber))
            e.addComponent(DieCode(self.numDice, self.numSides))

            if additionalSteps:
                additionalSteps(self, e)
            
            yield e
    
    def runSimulation(self):
        super().runSimulation()
        self.reportSystem.run()

class AttackRollSimulation(Simulation):
    def __init__(self, runs, systems):
        super().__init__(runs, systems)
        self.reportSystem = None
        self.rollBonus = 0
        self.targetNumbers = []
        self.numSides = 0
        self.numDice = 0
        self.additionalSteps = None

    def setReportSystem(self, reportSystem):
        self.reportSystem = reportSystem
        return self
    
    def setRollBonus(self, rollBonus):
        self.rollBonus = rollBonus
        return self
    
    def addTargetNumber(self, targetNumber, weight):
        self.targetNumbers.append(ValueWeight(targetNumber, weight))
        return self

    def setDieCode(self, numDice, numSides):
        self.numDice = numDice
        self.numSides = numSides
        return self

    def setAdditionalSteps(self, additionalSteps):
        self.additionalSteps = additionalSteps
        return self
    
    def entityGenerator(self):
        """Generate a standard entity for an attack roll simulation.
        additionalSteps is optional and has the following definition:
            additionalSteps(Entity)
            Entity is altered directly by additionalSteps.
            Return value is ignored.
        """
        targets = [t.value for t in self.targetNumbers]
        weights = [b.weight for b in self.targetNumbers]

        for i in range(self.runs):
            e = Entity()
            e.addComponent(D20Roll())
            e.addComponent(RollBonus(self.rollBonus))
            e.addComponent(TargetNumber(choices(targets, weights)[0]))
            e.addComponent(DieCode(self.numDice, self.numSides))

            if self.additionalSteps:
                self.additionalSteps(e)
            
            yield e
    
    def runSimulation(self):
        print('running sim')
        super().runSimulation()
        print('Running report system...')
        self.reportSystem.run()