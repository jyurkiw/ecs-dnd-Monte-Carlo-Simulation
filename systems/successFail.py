from ecs.lib.system import System
from mcSim.components.general import Fail
from mcSim.components.general import Success

class SuccessFailSystem(System):
    def __init__(self, reversed=False):
        super().__init__(['TargetNumber', 'D20Roll', 'RollBonus'])
        self.reversed = reversed
    
    def logic(self, entity):
        roll = entity['D20Roll'].value
        bonus = entity['RollBonus'].value
        target = entity['TargetNumber'].value

        if not self.reversed:
            if roll + bonus >= target:
                entity.addComponent(Success())
            else:
                entity.addComponent(Fail())
        else:
            if roll + bonus < target:
                entity.addComponent(Success())
            else:
                entity.addComponent(Fail())