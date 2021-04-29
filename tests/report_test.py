from ecs.lib.entity import Entity
from mcSim.components.general import Complete, DamageTotal
from mcSim.systems.report import ReportSystem
import unittest

class TestReport(unittest.TestCase):
    def test_report(self):
        expectedString = "{0} (level {1}):\n\tAverage Damage: {2:+.2f}\n\tData Points: {3}".format(
            "TestSpell",
            5,
            10,
            10
        )

        for idx in range(10):
            e = Entity()
            e.addComponent(DamageTotal(10))
            e.addComponent(Complete())
        system = ReportSystem()
        system.run()

        actualString = system.genReport("TestSpell", 5)
        self.assertEqual(actualString, expectedString)

if __name__ == "__main__":
    unittest.main()