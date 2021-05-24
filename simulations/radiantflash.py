from ecs.lib.entity import EntityManager
from mcSim.data.statdata import DexterityData
from mcSim.simulations.simulation import TargetNumberSimulation, RUNS
from mcSim.systems.cassandraReport import CassandraReportSystem
from mcSim.systems.roll import RollSystem
from mcSim.systems.successFail import SuccessFailSystem
from mcSim.systems.successFailByMargin import SuccessFailByMarginSystem, aggregateSuccesFailByMargin, reportSuccessFailByMargine
from mcSim.systems.summarize import SummarizeSystem

class RadiantFlashSimulation(TargetNumberSimulation):
    def __init__(self, reportSystem):
        super().__init__(RUNS, [
            SuccessFailSystem(reversed=True),
            SuccessFailByMarginSystem(5, reversed=True),
            RollSystem(),
            SummarizeSystem()
        ])
        self.setReportSystem(reportSystem)

class RadiantFlash_3rdLevel(RadiantFlashSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem())
        self.setTargetNumber(13).setDieCode(1, 6)
        DexterityData.loadLevel3(self)

class RadiantFlash_5thLevel(RadiantFlashSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem())
        self.setTargetNumber(13).setDieCode(2, 6)
        DexterityData.loadLevel5(self)

class RadiantFlash_11thLevel(RadiantFlashSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem())
        self.setTargetNumber(13).setDieCode(3, 6)
        DexterityData.loadLevel11(self)

class RadiantFlash_17thLevel(RadiantFlashSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem())
        self.setTargetNumber(13).setDieCode(4, 6)
        DexterityData.loadLevel17(self)

def main():
    for test, level in [
                (RadiantFlash_3rdLevel(), 3),
                (RadiantFlash_5thLevel(), 5),
                (RadiantFlash_11thLevel(), 11),
                (RadiantFlash_17thLevel(), 17)
                ]:
        test.reportSystem.addDataAggregator(
            aggregateSuccesFailByMargin,
            reportSuccessFailByMargine
        )
        test.runSimulation()
        test.reportSystem.addStandardFields('Radiant Flash', 'cantrip', level)
        test.reportSystem.genReport()

        EntityManager.clear()

if __name__ == '__main__':
    from mcSim.util.writer import writeReport
    main()