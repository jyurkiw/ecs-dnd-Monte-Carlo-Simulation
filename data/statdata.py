from collections import namedtuple

ValueWeight = namedtuple('ValueWeight', ['value', 'weight'])

# ValueWeight loading functions by stat
# Armor Class
class ArmorClassData(object):
    @staticmethod
    def loadLevel3(simulation):
        (simulation.addTargetNumber(9, 1)
            .addTargetNumber(10, 1)
            .addTargetNumber(11, 3)
            .addTargetNumber(12, 5)
            .addTargetNumber(13, 13)
            .addTargetNumber(14, 12)
            .addTargetNumber(15, 10)
            .addTargetNumber(16, 9)
            .addTargetNumber(17, 7)
            .addTargetNumber(18, 5))

    @staticmethod
    def loadLevel5(simulation):
        (simulation.setDieCode(2, 10)
            .addTargetNumber(9, 1)
            .addTargetNumber(10, 1)
            .addTargetNumber(11, 1)
            .addTargetNumber(12, 5)
            .addTargetNumber(13, 7)
            .addTargetNumber(14, 14)
            .addTargetNumber(15, 46)
            .addTargetNumber(16, 18)
            .addTargetNumber(17, 13)
            .addTargetNumber(18, 20)
            .addTargetNumber(19, 2)
            .addTargetNumber(20, 1))

    @staticmethod
    def loadLevel11(simulation):
        (simulation.setDieCode(3, 10)
            .addTargetNumber(8, 1)
            .addTargetNumber(9, 1)
            .addTargetNumber(10, 2)
            .addTargetNumber(11, 6)
            .addTargetNumber(12, 10)
            .addTargetNumber(13, 18)
            .addTargetNumber(14, 43)
            .addTargetNumber(15, 25)
            .addTargetNumber(16, 14)
            .addTargetNumber(17, 14)
            .addTargetNumber(18, 6)
            .addTargetNumber(19, 5)
            .addTargetNumber(20, 4)
            .addTargetNumber(21, 1))

    @staticmethod
    def loadLevel17(simulation):
        (simulation.addTargetNumber(10, 1)
            .addTargetNumber(11, 1)
            .addTargetNumber(12, 1)
            .addTargetNumber(13, 1)
            .addTargetNumber(14, 2)
            .addTargetNumber(15, 1)
            .addTargetNumber(16, 3)
            .addTargetNumber(17, 16)
            .addTargetNumber(18, 14)
            .addTargetNumber(19, 32)
            .addTargetNumber(20, 16)
            .addTargetNumber(21, 6)
            .addTargetNumber(22, 6)
            .addTargetNumber(23, 1))

class StrengthData(object):
    pass

class DexterityData(object):
    @staticmethod
    def loadLevel3(simulation):
        (simulation.addRollBonus(-3, 2)
            .addRollBonus(-2, 1)
            .addRollBonus(-1, 16)
            .addRollBonus(0, 21)
            .addRollBonus(1, 30)
            .addRollBonus(2, 42)
            .addRollBonus(3, 21)
            .addRollBonus(4, 9)
            .addRollBonus(5, 8)
            .addRollBonus(6, 1)
            .addRollBonus(7, 3))
    
    @staticmethod
    def loadLevel5(simulation):
        (simulation.addRollBonus(-1, 14)
            .addRollBonus(0, 26)
            .addRollBonus(1, 21)
            .addRollBonus(2, 39)
            .addRollBonus(3, 21)
            .addRollBonus(4, 11)
            .addRollBonus(5, 9)
            .addRollBonus(6, 5)
            .addRollBonus(7, 5)
            .addRollBonus(8, 2))

    @staticmethod
    def loadLevel11(simulation):
        print('here')
        (simulation.addRollBonus(-3, 1)
            .addRollBonus(-2, 2)
            .addRollBonus(-1, 6)
            .addRollBonus(0, 6)
            .addRollBonus(1, 9)
            .addRollBonus(2, 15)
            .addRollBonus(3, 16)
            .addRollBonus(4, 5)
            .addRollBonus(5, 12)
            .addRollBonus(6, 18)
            .addRollBonus(7, 9)
            .addRollBonus(8, 7)
            .addRollBonus(9, 4)
            .addRollBonus(10, 1))

    @staticmethod
    def loadLevel17(simulation):
        (simulation.addRollBonus(-4, 1)
            .addRollBonus(-3, 1)
            .addRollBonus(-2, 1)
            .addRollBonus(-1, 1)
            .addRollBonus(0, 1)
            .addRollBonus(1, 1)
            .addRollBonus(2, 4)
            .addRollBonus(3, 4)
            .addRollBonus(4, 2)
            .addRollBonus(5, 6)
            .addRollBonus(6, 12)
            .addRollBonus(7, 3)
            .addRollBonus(8, 6)
            .addRollBonus(9, 3)
            .addRollBonus(10, 2)
            .addRollBonus(11, 3))

class ConstitutionData(object):
    @staticmethod
    def loadLevel3(simulation):
        (simulation.addRollBonus(-1, 1)
            .addRollBonus(0, 21)
            .addRollBonus(1, 53)
            .addRollBonus(2, 28)
            .addRollBonus(3, 17)
            .addRollBonus(4, 1))

    @staticmethod
    def loadLevel5(simulation):
        (simulation.addRollBonus(0, 12)
            .addRollBonus(1, 25)
            .addRollBonus(2, 48)
            .addRollBonus(3, 74)
            .addRollBonus(4, 20)
            .addRollBonus(5, 15)
            .addRollBonus(6, 1))

    @staticmethod
    def loadLevel11(simulation):
        (simulation.addRollBonus(-1, 1)
            .addRollBonus(0, 2)
            .addRollBonus(1, 13)
            .addRollBonus(2, 24)
            .addRollBonus(3, 27)
            .addRollBonus(4, 32)
            .addRollBonus(5, 31)
            .addRollBonus(6, 10)
            .addRollBonus(7, 3)
            .addRollBonus(8, 1))

    @staticmethod
    def loadLevel17(simulation):
        (simulation.addRollBonus(0, 1)
            .addRollBonus(1, 1)
            .addRollBonus(2, 1)
            .addRollBonus(3, 6)
            .addRollBonus(4, 2)
            .addRollBonus(5, 7)
            .addRollBonus(6, 8)
            .addRollBonus(7, 17)
            .addRollBonus(8, 3)
            .addRollBonus(9, 1)
            .addRollBonus(10, 2))

class IntelligenceData(object):
    pass

class WisdomData(object):
    pass

class CharismaData(object):
    pass

