from ecs.lib.system import System
from mcSim.components.general import Complete, DamageTotal

class SummarizeSystem(System):
    def __init__(self):
        super().__init__(['Success', 'Roll', 'DieCode'])

    def logic(self, entity):
        roll = entity['Roll'].value
        damageBonus = entity['DieCode'].bonus
        entity.addComponent(DamageTotal(sum(roll) + damageBonus))
        entity.addComponent(Complete())