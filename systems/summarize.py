from ecs.lib.system import System
from mcSim.components.general import Complete, DamageTotal

class SummarizeSystem(System):
    def __init__(self):
        super().__init__(['Success', 'Roll'])

    def logic(self, entity):
        roll = entity['Roll'].value
        entity.addComponent(DamageTotal(sum(roll)))
        entity.addComponent(Complete())