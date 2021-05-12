from ecs.lib.entity import Entity, EntityManager
from mcSim.components.cover import NoCover, HalfCover, ThreeQuartersCover
from mcSim.components.dice import D20Roll, DieCode
from mcSim.components.rollBonus import RollBonus
from mcSim.components.targetNumber import TargetNumber
from mcSim.simulations.simulation import Simulation
from mcSim.systems.crit import CritSystem
from mcSim.systems.report import ReportSystem
from mcSim.systems.roll import RollSystem
from mcSim.systems.rollBonus import HalfCoverSystem, ThreeQuartersCoverSystem
from mcSim.systems.successFail import SuccessFailSystem
from mcSim.systems.summarize import SummarizeSystem
from random import choices

RUNS = 100000

class FireboltSimulation(Simulation):
    def __init__(self):
        self.reportSystem = ReportSystem()
        self.rollBonus = 0
        self.targetNumbers = []
        self.targetNumberWeights = []
        self.numDice = 0
        super().__init__(RUNS, [
            SuccessFailSystem(),
            HalfCoverSystem(),
            ThreeQuartersCoverSystem(),
            CritSystem(),
            RollSystem(),
            SummarizeSystem(),
            self.reportSystem
        ])
    
    def setRollBonus(self, bonus):
        self.rollBonus = bonus
        return self

    def setTargetNumbers(self, targetNumbers):
        self.targetNumbers = targetNumbers
        return self

    def setTargetNumberWeights(self, weights):
        self.targetNumberWeights = weights
        return self

    def setNumDice(self, num):
        self.numDice = num
        return self

    def entityGenerator(self):
        targetNumbers = [TargetNumber(x) for x in self.targetNumbers]
        coverValues = [NoCover(), HalfCover(), ThreeQuartersCover()]
        coverWeights = [5, 3, 2]

        for i in range(self.runs):
            e = Entity()
            e.addComponent(D20Roll())
            e.addComponent(RollBonus(self.rollBonus))
            e.addComponent(choices(targetNumbers, self.targetNumberWeights)[0])
            e.addComponent(choices(coverValues, coverWeights)[0])
            e.addComponent(DieCode(self.numDice, 10))
            yield e

class Firebolt_3rdLevel(FireboltSimulation):
    def __init__(self):
        super().__init__()
        (self.setRollBonus(5)
            .setTargetNumbers(range(9, 19))
            .setTargetNumberWeights([1, 1, 3, 5, 13, 12, 10, 9, 7, 5])
            .setNumDice(1))

class Firebolt_5thLevel(FireboltSimulation):
    def __init__(self):
        super().__init__()
        (self.setRollBonus(7)
            .setTargetNumbers(range(9, 21))
            .setTargetNumberWeights([1, 1, 1, 5, 7, 14, 46, 18, 13, 20, 2, 1])
            .setNumDice(2))

class Firebolt_11thLevel(FireboltSimulation):
    def __init__(self):
        super().__init__()
        (self.setRollBonus(10)
            .setTargetNumbers(range(8, 22))
            .setTargetNumberWeights([1, 1, 2, 6, 10, 18, 43, 25, 14, 14, 6, 5, 4, 1])
            .setNumDice(3))

class Firebolt_17thLevel(FireboltSimulation):
    def __init__(self):
        super().__init__()
        (self.setRollBonus(13)
            .setTargetNumbers(range(10, 24))
            .setTargetNumberWeights([1, 1, 1, 1, 2, 1, 3, 16, 14, 32, 16, 6, 6, 1])
            .setNumDice(4))

def main():
    sim3 = Firebolt_3rdLevel()
    sim5 = Firebolt_5thLevel()
    sim11 = Firebolt_11thLevel()
    sim17 = Firebolt_17thLevel()

    sim3.runSimulation()
    print(sim3.reportSystem.genReport('Firebolt', 3))
    EntityManager.clear()

    sim5.runSimulation()
    print(sim5.reportSystem.genReport('Firebolt', 5))
    EntityManager.clear()

    sim11.runSimulation()
    print(sim11.reportSystem.genReport('Firebolt', 11))
    EntityManager.clear()

    sim17.runSimulation()
    print(sim17.reportSystem.genReport('Firebolt', 17))
    EntityManager.clear()

if __name__ == '__main__':
    main()
    