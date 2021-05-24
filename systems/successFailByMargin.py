from ecs.lib.system import System
from mcSim.components.general import MarginFail, MarginSuccess
from mcSim.util.tuples import AggregatorValue

class SuccessFailByMarginSystem(System):
    """
    """
    def __init__(self, margin, reversed=False):
        super().__init__(['TargetNumber', 'D20Roll', 'RollBonus', 'Success'])
        self.margin = margin
        self.reversed = reversed
    
    def logic(self, entity):
        roll = entity['D20Roll'].value
        bonus = entity['RollBonus'].value
        target = entity['TargetNumber'].value

        if not self.reversed:
            if roll + bonus >= target + self.margin:
                entity.addComponent(MarginSuccess())
            else:
                entity.addComponent(MarginFail())
        else:
            if roll + bonus <= target - self.margin:
                entity.addComponent(MarginSuccess())
            else:
                entity.addComponent(MarginFail())

def aggregateSuccesFailByMargin(entity, operationDict):
    if 'MarginSuccess' in entity:
        operationDict['successByMargin'] = operationDict.get('successByMargin', 0) + 1

def reportSuccessFailByMargine(damageTotal, hits, runs, operationDict):
    return [
        AggregatorValue('successByMargin', operationDict.get('successByMargin', 0)),
        AggregatorValue('marginSuccessRate', operationDict.get('successByMargin', 0) / runs)
    ]