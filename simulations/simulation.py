from abc import ABC, abstractclassmethod

class Simulation(ABC):
    """A base simulation framework. Cannot be instantiated.
    """
    def __init__(self, runs, systems):
        self.runs = runs
        self.systems = systems

    @abstractclassmethod
    def entityGenerator(self):
        raise Exception("Simulation.entityGenerator needs to be overriden.")

    def runSimulation(self):
        [entity for entity in self.entityGenerator()]
        print('Simulation populated')
        for system in self.systems:
            system.run()