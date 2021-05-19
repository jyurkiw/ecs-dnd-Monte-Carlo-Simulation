from ecs.lib.entity import EntityManager
from mcSim.data.statdata import DexterityData
from mcSim.simulations.simulation import TargetNumberSimulation, RUNS
from mcSim.systems.report import CassandraReportSystem, ReportSystem
from mcSim.systems.roll import RollSystem
from mcSim.systems.successFail import SuccessFailSystem
from mcSim.systems.summarize import SummarizeSystem

class RadiantFlashSimulation(TargetNumberSimulation):
    def __init__(self, reportSystem):
        super().__init__(RUNS, [
            SuccessFailSystem(reversed=True),
            RollSystem(),
            SummarizeSystem()
        ])
        self.setReportSystem(reportSystem)

class RadiantFlash_3rdLevel(RadiantFlashSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem('Radiant Flash', 3, RUNS))
        self.setTargetNumber(13).setDieCode(1, 6)
        DexterityData.loadLevel3(self)

class RadiantFlash_5thLevel(RadiantFlashSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem('Radiant Flash', 5, RUNS))
        self.setTargetNumber(13).setDieCode(2, 6)
        DexterityData.loadLevel5(self)

class RadiantFlash_11thLevel(RadiantFlashSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem('Radiant Flash', 11, RUNS))
        self.setTargetNumber(13).setDieCode(3, 6)
        DexterityData.loadLevel11(self)

class RadiantFlash_17thLevel(RadiantFlashSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem('Radiant Flash', 17, RUNS))
        self.setTargetNumber(13).setDieCode(4, 6)
        DexterityData.loadLevel17(self)

def main():
    reports = []
    for test in [RadiantFlash_3rdLevel(),
                RadiantFlash_5thLevel(),
                RadiantFlash_11thLevel(),
                RadiantFlash_17thLevel()]:
        test.runSimulation()
        reports.append(test.reportSystem.makeReport())
        EntityManager.clear()
    return reports

if __name__ == '__main__':
    from mcSim.util.writer import writeReport
    writeReport(main())