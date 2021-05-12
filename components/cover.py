from ecs.lib.component import Component
from ecs.components.valueComponent import ValueComponent

class NoCover(Component): pass

class HalfCover(ValueComponent):
    def __init__(self):
        super().__init__(2)

class ThreeQuartersCover(ValueComponent):
    def __init__(self):
        super().__init__(5)