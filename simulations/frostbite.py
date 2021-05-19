from ecs.lib.entity import EntityManager
from mcSim.data.statdata import ConstitutionData
from mcSim.simulations.simulation import TargetNumberSimulation, RUNS
from mcSim.systems.report import CassandraReportSystem
from mcSim.systems.roll import RollSystem
from mcSim.systems.successFail import SuccessFailSystem
from mcSim.systems.summarize import SummarizeSystem

class FrostbiteSimulation(TargetNumberSimulation):
    def __init__(self, reportSystem):
        super().__init__(RUNS, [
            SuccessFailSystem(reversed=True),
            RollSystem(),
            SummarizeSystem()
        ])
        self.setReportSystem(reportSystem)

class Frostbite_3rdLevel(FrostbiteSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem('Frostbolt', 3, RUNS))
        self.setTargetNumber(13).setDieCode(1, 6)
        ConstitutionData.loadLevel3(self)

class Frostbite_5thLevel(FrostbiteSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem('Frostbolt', 5, RUNS))
        self.setTargetNumber(15).setDieCode(2, 6)
        ConstitutionData.loadLevel5(self)

class Frostbite_11thLevel(FrostbiteSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem('Frostbolt', 11, RUNS))
        self.setTargetNumber(18).setDieCode(3, 6)
        ConstitutionData.loadLevel11(self)

class Frostbite_17thLevel(FrostbiteSimulation):
    def __init__(self):
        super().__init__(CassandraReportSystem('Frostbolt', 17, RUNS))
        self.setTargetNumber(22).setDieCode(4, 6)
        ConstitutionData.loadLevel17(self)

def main():
    reports = []
    for test in [Frostbite_3rdLevel(),
                Frostbite_5thLevel(),
                Frostbite_11thLevel(),
                Frostbite_17thLevel()]:
        test.runSimulation()
        reports.append(test.reportSystem.makeReport())
        EntityManager.clear()
    return reports

if __name__ == '__main__':
    from mcSim.util.writer import writeReport
    writeReport(main())