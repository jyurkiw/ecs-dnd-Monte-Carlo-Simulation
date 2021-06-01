from ecs.lib.entity import EntityManager
from mcSim.components.cover import NoCover, HalfCover, ThreeQuartersCover
from mcSim.data.statdata import ArmorClassData
from mcSim.simulations.simulation import AttackRollSimulation, RUNS
from mcSim.systems.crit import CritSystem
from mcSim.systems.cassandraReport import ApiReportSystem
from mcSim.systems.roll import RollSystem
from mcSim.systems.rollBonus import HalfCoverSystem, ThreeQuartersCoverSystem
from mcSim.systems.successFail import SuccessFailSystem
from mcSim.systems.summarize import SummarizeSystem
from mcSim.systems.thresholdReroll import ThresholdRerollSystem, aggregatePreRerollDamage, reportPreRerollDamage
from random import choices

class MagneticSlingSimulation(AttackRollSimulation):
    def __init__(self, reportSystem):
        self.coverValues = [NoCover(), HalfCover(), ThreeQuartersCover()]
        self.coverWeights = [5, 3, 2]

        super().__init__(RUNS, [
            SuccessFailSystem(),
            HalfCoverSystem(),
            ThreeQuartersCoverSystem(),
            CritSystem(),
            RollSystem(),
            ThresholdRerollSystem(3),
            SummarizeSystem()
        ])
        self.setReportSystem(reportSystem)
        self.setAdditionalSteps(self.additionalSteps)
    
    def addCoverToEntity(self, entity):
        entity.addComponent(choices(self.coverValues, self.coverWeights)[0])

class MagneticSling_3rdLevel(MagneticSlingSimulation):
    def __init__(self):
        super().__init__(ApiReportSystem())
        self.setRollBonus(5).setDieCode(1, 6)
        ArmorClassData.loadLevel3(self)

class MagneticSling_5thLevel(MagneticSlingSimulation):
    def __init__(self):
        super().__init__(ApiReportSystem())
        self.setRollBonus(7).setDieCode(2, 6)
        ArmorClassData.loadLevel5(self)

class MagneticSling_11thLevel(MagneticSlingSimulation):
    def __init__(self):
        super().__init__(ApiReportSystem())
        self.setRollBonus(10).setDieCode(3, 6)
        ArmorClassData.loadLevel11(self)

class MagneticSling_17thLevel(MagneticSlingSimulation):
    def __init__(self):
        super().__init__(ApiReportSystem())
        self.setRollBonus(13).setDieCode(4, 6)
        ArmorClassData.loadLevel17(self)

def main():
    for test, level in [
                (MagneticSling_3rdLevel(), 3),
                (MagneticSling_5thLevel(), 5),
                (MagneticSling_11thLevel(), 11),
                (MagneticSling_17thLevel(), 17)
                ]:
        test.reportSystem.addDataAggregator(
            aggregatePreRerollDamage,
            reportPreRerollDamage
        )
        test.runSimulation()
        test.reportSystem.addStandardFields('Magnetic Sling', 'cantrip', level)
        test.reportSystem.genReport()

        EntityManager.clear()

if __name__ == '__main__':
    from mcSim.util.writer import writeReport
    main()