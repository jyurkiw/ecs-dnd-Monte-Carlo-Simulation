from ecs.lib.entity import Entity
from ecs.lib.entity_manager import EntityManager
from mcSim.systems.roll import RollSystem
from mcSim.components.dice import DieCode
from random import randint
import unittest
import unittest.mock as mock

def nrand(a, b):
    return 3

class TestRoll(unittest.TestCase):
    def tearDown(self):
        EntityManager.clear()

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
            self.assertEqual(e['Roll'].value, [3,3,3])

    # TODO: Test RerollBelowThreshold component

if __name__ == "__main__":
    unittest.main()