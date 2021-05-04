from ecs.lib.entity import Entity
from ecs.lib.entity_manager import EntityManager
from mcSim.systems.roll import RollSystem
from mcSim.components.dice import DieCode
from mcSim.components.dice import RerollBelowThreshold
from random import randint
import unittest
import unittest.mock as mock

def grand():
    for i in range(100):
        yield i

grandit = grand()

def nrand(a, b):
    return next(grandit)

class TestRoll(unittest.TestCase):
    def tearDown(self):
        EntityManager.clear()
        global grandit
        grandit = grand()

    def test_rollSystem_addsRollComponent(self):
        e = Entity()
        e.addComponent(DieCode(3, 6))
        rs = RollSystem()

        with mock.patch('mcSim.systems.roll.randint', nrand):
            rs.run()
            self.assertIn('Roll', e)

    def test_rollSystem_produces3rolls(self):
        e = Entity()
        e.addComponent(DieCode(3, 6))
        rs = RollSystem()

        with mock.patch('mcSim.systems.roll.randint', nrand):
            rs.run()
            self.assertEqual(len(e['Roll'].value), 3)

    def test_rollSystem_checkRollValues(self):
        e = Entity()
        e.addComponent(DieCode(3, 6))
        rs = RollSystem()

        with mock.patch('mcSim.systems.roll.randint', nrand):
            rs.run()
            self.assertEqual(e['Roll'].value, [0,1,2])

    def test_rollSystem_rerollBelowThreshold(self):
        e = Entity()
        e.addComponent(DieCode(5, 6))
        e.addComponent(RerollBelowThreshold(3, 5))
        rs = RollSystem()

        with mock.patch('mcSim.systems.roll.randint', nrand):
            rs.run()
            self.assertEqual(e['Roll'].value, [5,6,7,3,4])
    
if __name__ == "__main__":
    unittest.main()