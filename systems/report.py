from ecs.lib.entity_manager import EntityManager
from ecs.lib.system import System

class ReportSystem(System):
    def __init__(self):
        super().__init__(['DamageTotal', 'Complete'])
        self.damages = []

    def logic(self, entity):
        self.damages.append(entity['DamageTotal'].value)

    def genReport(self, spellName, casterLevel):
        total = sum(self.damages)
        average = total / len(self.damages)

        return "{0} (caster level {1}):\n\tAverage Damage: {2:.2f}\n\tData Points: {3}\n\t% Hits: {4:.2f}%".format(
            spellName,
            casterLevel,
            average,
            EntityManager.count(),
            (len(self.damages) / EntityManager.count()) * 100
        )