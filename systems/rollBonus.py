from ecs.lib.system import System
from mcSim.components.rollBonus import RollBonus

class RollBonusSystem(System):
    def __init__(self, bonusComponentName):
        super().__init__(['RollBonus', bonusComponentName])
        self.bonusComponentName = bonusComponentName

    def logic(self, entity):
        bonus = entity[self.bonusComponentName].value
        entity['RollBonus'].value += bonus

class HalfCoverSystem(RollBonusSystem):
    def __init__(self):
        super().__init__('HalfCover')

class ThreeQuartersCoverSystem(RollBonusSystem):
    def __init__(self):
        super().__init__('ThreeQuartersCover')