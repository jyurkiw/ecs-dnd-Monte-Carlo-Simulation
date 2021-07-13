from ecs.lib.entity_manager import EntityManager
from ecs.lib.system import System
import requests

class ApiReportSystem(System):
    def __init__(self):
        super().__init__(['DamageTotal', 'Complete'])
        self.damageTotal = 0
        self.hits = 0
        self.spellName = None
        self.casterLevel = None

        self.dataAggregators = []
        self.reportFieldFunctions = []
        self.reportData = {}
        self.aggregateOpData = {}

    def addStandardFields(self, spellName, spellLevel, casterLevel):
        self.addReportField('spellLevel', spellLevel)
        self.addReportField('entityCount', EntityManager.count())

        self.spellName = spellName
        self.casterLevel = casterLevel

    def addReportField(self, name, data):
        self.reportData[name] = str(data)

    def addDataAggregator(self, aggregatorFunction, reportFunction):
        """Aggregator functions need to satisfy the following function signature:
            def aggregatorName(entity, operationDict)
            The operationDict is a dictionary provided by the report system for the
                aggregation functions to store data between entities.
           Report functions need to satisfy the following function signature:
            def reportFunctionName(damageTotal, hits, runs, operationDict) -> [AggregatorValue]
        """
        self.dataAggregators.append(aggregatorFunction)
        self.reportFieldFunctions.append(reportFunction)

    def logic(self, entity):
        self.damageTotal += entity['DamageTotal'].value
        self.hits += 1

        for aggregator in self.dataAggregators:
            aggregator(entity, self.aggregateOpData)
    
    def genReport(self):
        self.addReportField('damageTotal', self.damageTotal)
        self.addReportField('attempts', EntityManager.count())
        self.addReportField('successes', self.hits)
        self.addReportField('successRate', str((self.hits / EntityManager.count()) * 100))
        self.addReportField('averageDamagePerHit', str(self.damageTotal / self.hits))
        self.addReportField('averageDamagePerCast', str(self.damageTotal / EntityManager.count()))

        for reporter in self.reportFieldFunctions:
            fields = reporter(self.damageTotal, self.hits, EntityManager.count(), self.aggregateOpData)
            for field in fields:
                self.addReportField(field.name, field.value)
        
        requests.post('http://mcsim-cluster_api_1:5000/report', json = {
            'spellName': self.spellName,
            'casterLevel': self.casterLevel,
            'reportData': self.reportData
        }, headers={'Content-type': 'application/json'})