from ecs.lib.entity import Entity
from mcSim.simulations.simulation import Simulation
#from mcSim.components.cover import HalfCover, ThreeQuartersCover
from mcSim.components.dice import D20Roll, DieCode
from mcSim.components.rollBonus import RollBonus
from mcSim.components.targetNumber import TargetNumber
from mcSim.systems.report import ReportSystem
from mcSim.systems.roll import RollSystem
from mcSim.systems.summarize import SummarizeSystem
from mcSim.systems.successFail import SuccessFailSystem
from random import choices

class Firebolt_3rdLevel(Simulation):
    def __init__(self, runs):
        self.reportSystem = ReportSystem()
        super().__init__(runs, [SuccessFailSystem(), RollSystem(), SummarizeSystem(), self.reportSystem])
    
    def entityGenerator(self):
        attackBonus = RollBonus(5)
        targetNumbers = [TargetNumber(x) for x in range(8, 17)]
        tnWeights = [1,1,2,3,10,10,8,6,5]
        dieCode = DieCode(1, 10)
        for i in range(self.runs):
            e = Entity()
            e.addComponent(D20Roll())
            e.addComponent(attackBonus)
            e.addComponent(choices(targetNumbers, tnWeights)[0])
            e.addComponent(dieCode)
            yield e

def main():
    sim = Firebolt_3rdLevel(100000)
    sim.runSimulation()
    print(sim.reportSystem.genReport('Firebolt', 3))

if __name__ == '__main__':
    main()