from ecs.lib.component import Component
from ecs.components.valueComponent import ValueComponent

# Base Components
class Complete(Component): pass
class Success(Component): pass
class Fail(Component): pass
class MarginSuccess(Component): pass
class MarginFail(Component): pass

# Value Components
class DamageTotal(ValueComponent): pass
class PreRerollDamageTotal(ValueComponent): pass
