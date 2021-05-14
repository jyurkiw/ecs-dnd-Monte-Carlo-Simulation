from ecs.lib.entity import Entity, EntityManager
from mcSim.components.dice import D20Roll, DieCode
from mcSim.components.rollBonus import RollBonus
from mcSim.components.targetNumber import TargetNumber
from mcSim.simulations.simulation import Simulation
from mcSim.systems.report import ReportSystem
from mcSim.systems.roll import RollSystem
from mcSim.systems.successFail import SuccessFailSystem
from mcSim.systems.summarize import SummarizeSystem
from random import choices

