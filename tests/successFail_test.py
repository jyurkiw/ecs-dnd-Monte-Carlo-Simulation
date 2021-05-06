from ecs.lib.entity import Entity
from mcSim.components.dice import D20Roll
from mcSim.components.rollBonus import RollBonus
from mcSim.systems.successFail import SuccessFail
from mcSim.components.targetNumber import TargetNumber
from unittest import TestCase
import unittest
import unittest.mock as mock

nextRoll = 1

def rollD20(a, b):
    global nextRoll
    return nextRoll

class TestSuccessFail(TestCase):
    def test_successFail_tnMinus1(self):
        global nextRoll
        nextRoll = 4
        e = Entity()
        e.addComponent(D20Roll())
        e.addComponent(RollBonus(0))
        e.addComponent(TargetNumber(5))

        sf = SuccessFail()
        sf.run()
        self.assertTrue('Fail' in e)

    def test_successFail_equalTn(self):
        global nextRoll
        nextRoll = 5
        e = Entity()
        e.addComponent(D20Roll())
        e.addComponent(RollBonus(0))
        e.addComponent(TargetNumber(5))

        sf = SuccessFail()
        sf.run()
        self.assertTrue('Success' in e)

    def test_successFail_tnPlus1(self):
        global nextRoll
        nextRoll = 6
        e = Entity()
        e.addComponent(D20Roll())
        e.addComponent(RollBonus(0))
        e.addComponent(TargetNumber(5))

        sf = SuccessFail()
        sf.run()
        self.assertTrue('Success' in e)

if __name__ == "__main__":
    unittest.main()