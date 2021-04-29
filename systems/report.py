from ecs.lib.system import System
from ecs.lib.factory import Factory

class ReportSystem(System):
    def __init__(self):
        super().__init__(['DamageTotal', 'Complete'])
        self.damages = []

    def logic(self, entity):
        self.damages.append(entity['DamageTotal'].value)

    def genReport(self, spellName, casterLevel):
        total = sum(self.damages)
        average = total / len(self.damages)

        return "{0} (level {1}):\n\tAverage Damage: {2:+.2f}\n\tData Points: {3}".format(
            spellName,
            casterLevel,
            average,
            len(self.damages)
        )