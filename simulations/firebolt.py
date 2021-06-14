from ecs.lib.entity import EntityManager
from mcSim.components.cover import NoCover, HalfCover, ThreeQuartersCover
from mcSim.data.statdata import ArmorClassData
from mcSim.simulations.simulation import AttackRollSimulation, RUNS
from mcSim.systems.crit import CritSystem
from mcSim.systems.apiReport import ApiReportSystem
from mcSim.systems.roll import RollSystem
from mcSim.systems.rollBonus import HalfCoverSystem, ThreeQuartersCoverSystem
from mcSim.systems.successFail import SuccessFailSystem
from mcSim.systems.summarize import SummarizeSystem
from random import choices

class FireboltSimulation(AttackRollSimulation):
    def __init__(self, reportSystem):
        self.coverValues = [NoCover(), HalfCover(), ThreeQuartersCover()]
        self.coverWeights = [5, 3, 2]

        super().__init__(RUNS, [
            SuccessFailSystem(),
            HalfCoverSystem(),
            ThreeQuartersCoverSystem(),
            CritSystem(),
            RollSystem(),
            SummarizeSystem()
        ])
        self.setReportSystem(reportSystem)
        self.setAdditionalSteps(self.additionalSteps)
    
    def addCoverToEntity(self, entity):
        entity.addComponent(choices(self.coverValues, self.coverWeights)[0])

class Firebolt_3rdLevel(FireboltSimulation):
    def __init__(self):
        super().__init__(ApiReportSystem())
        self.setRollBonus(5).setDieCode(1, 10)
        ArmorClassData.loadLevel3(self)

class Firebolt_5thLevel(FireboltSimulation):
    def __init__(self):
        super().__init__(ApiReportSystem())
        self.setRollBonus(7).setDieCode(2, 10)
        ArmorClassData.loadLevel5(self)

class Firebolt_11thLevel(FireboltSimulation):
    def __init__(self):
        super().__init__(ApiReportSystem())
        self.setRollBonus(10).setDieCode(3, 10)
        ArmorClassData.loadLevel11(self)

class Firebolt_17thLevel(FireboltSimulation):
    def __init__(self):
        super().__init__(ApiReportSystem())
        self.setRollBonus(13).setDieCode(4, 10)
        ArmorClassData.loadLevel17(self)

def main():
    for test, level in [
                (Firebolt_3rdLevel(), 3),
                (Firebolt_5thLevel(), 5),
                (Firebolt_11thLevel(), 11),
                (Firebolt_17thLevel(), 17)
                ]:
        test.runSimulation()
        test.reportSystem.addStandardFields('Firebolt', 'cantrip', level)
        test.reportSystem.genReport()
        EntityManager.clear()

if __name__ == '__main__':
    from mcSim.util.writer import writeReport
    writeReport(main())
    