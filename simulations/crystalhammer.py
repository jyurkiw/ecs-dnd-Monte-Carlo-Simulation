from ecs.lib.entity import EntityManager
from mcSim.components.cover import NoCover, HalfCover, ThreeQuartersCover
from mcSim.data.statdata import ArmorClassData
from mcSim.simulations.simulation import AttackRollSimulation, RUNS
from mcSim.systems.crit import CritSystem
from mcSim.systems.cassandraReport import CassandraReportSystem
from mcSim.systems.roll import RollSystem
from mcSim.systems.rollBonus import HalfCoverSystem, ThreeQuartersCoverSystem
from mcSim.systems.successFail import SuccessFailSystem
from mcSim.systems.summarize import SummarizeSystem
from random import choices

class CrystalHammerSimulation(AttackRollSimulation):
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

class CrystalHammer_3rdLevel(CrystalHammerSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem())
        self.setRollBonus(5).setDieCode(0, 4, 3)
        ArmorClassData.loadLevel3(self)

class CrystalHammer_5thLevel(CrystalHammerSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem())
        self.setRollBonus(7).setDieCode(1, 4, 4)
        ArmorClassData.loadLevel5(self)

class CrystalHammer_11thLevel(CrystalHammerSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem())
        self.setRollBonus(10).setDieCode(2, 4, 5)
        ArmorClassData.loadLevel11(self)

class CrystalHammer_17thLevel(CrystalHammerSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem())
        self.setRollBonus(13).setDieCode(3, 4, 5)
        ArmorClassData.loadLevel17(self)

def main():
    for test, level in [
                (CrystalHammer_3rdLevel(), 3),
                (CrystalHammer_5thLevel(), 5),
                (CrystalHammer_11thLevel(), 11),
                (CrystalHammer_17thLevel(), 17)
                ]:
        test.runSimulation()
        test.reportSystem.addStandardFields('Crystal Hammer', 'cantrip', level)
        test.reportSystem.genReport()
        EntityManager.clear()

if __name__ == '__main__':
    from mcSim.util.writer import writeReport
    writeReport(main())
    