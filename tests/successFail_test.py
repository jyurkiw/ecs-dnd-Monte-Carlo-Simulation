from ecs.lib.entity import Entity
from ecs.lib.entity_manager import EntityManager
from mcSim.components.dice import D20Roll
from mcSim.components.rollBonus import RollBonus
from mcSim.systems.successFail import SuccessFailSystem
from mcSim.components.targetNumber import TargetNumber
from unittest import TestCase
import unittest
import unittest.mock as mock

nextRoll = 1

def rollD20(a, b):
    global nextRoll
    return nextRoll

class TestSuccessFail(TestCase):
    def setUp(self):
        EntityManager.clear()

    def test_successFailSystem_tnMinus1(self):
        global nextRoll
        nextRoll = 4
        e = Entity()
        with mock.patch('mcSim.components.dice.randint', rollD20):
            e.addComponent(D20Roll())
        e.addComponent(RollBonus(0))
        e.addComponent(TargetNumber(5))

        sf = SuccessFailSystem()
        sf.run()
        self.assertTrue('Fail' in e)

    def test_successFailSystem_equalTn(self):
        global nextRoll
        nextRoll = 5
        e = Entity()
        with mock.patch('mcSim.components.dice.randint', rollD20):
            e.addComponent(D20Roll())
        e.addComponent(RollBonus(0))
        e.addComponent(TargetNumber(5))

        sf = SuccessFailSystem()
        sf.run()
        self.assertTrue('Success' in e)

    def test_successFailSystem_tnPlus1(self):
        global nextRoll
        nextRoll = 6
        e = Entity()
        with mock.patch('mcSim.components.dice.randint', rollD20):
            e.addComponent(D20Roll())
        e.addComponent(RollBonus(0))
        e.addComponent(TargetNumber(5))

        sf = SuccessFailSystem()
        sf.run()
        self.assertTrue('Success' in e)

if __name__ == "__main__":
    unittest.main()