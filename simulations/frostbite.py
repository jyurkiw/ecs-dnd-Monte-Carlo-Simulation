from ecs.lib.entity import EntityManager
from mcSim.data.statdata import ConstitutionData
from mcSim.simulations.simulation import TargetNumberSimulation, RUNS
from mcSim.systems.cassanapiReportdraReport import ApiReportSystem
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
        super().__init__(ApiReportSystem())
        self.setTargetNumber(13).setDieCode(1, 6)
        ConstitutionData.loadLevel3(self)

class Frostbite_5thLevel(FrostbiteSimulation):
    def __init__(self):
        super().__init__(ApiReportSystem())
        self.setTargetNumber(15).setDieCode(2, 6)
        ConstitutionData.loadLevel5(self)

class Frostbite_11thLevel(FrostbiteSimulation):
    def __init__(self):
        super().__init__(ApiReportSystem())
        self.setTargetNumber(18).setDieCode(3, 6)
        ConstitutionData.loadLevel11(self)

class Frostbite_17thLevel(FrostbiteSimulation):
    def __init__(self):
        super().__init__(ApiReportSystem())
        self.setTargetNumber(22).setDieCode(4, 6)
        ConstitutionData.loadLevel17(self)

def main():
    for test, level in [
                (Frostbite_3rdLevel(), 3),
                (Frostbite_5thLevel(), 5),
                (Frostbite_11thLevel(), 11),
                (Frostbite_17thLevel(), 17)
                ]:
        test.runSimulation()
        test.reportSystem.addStandardFields('Frostbite', 'cantrip', level)
        test.reportSystem.genReport()
        EntityManager.clear()

if __name__ == '__main__':
    from mcSim.util.writer import writeReport
    writeReport(main())