from cassandra.cluster import Cluster
from ecs.lib.entity_manager import EntityManager
from ecs.lib.system import System
from uuid import uuid1

CREATE_KEYSPACE = "create keyspace if not exists simulations with replication = {'class': 'SimpleStrategy', 'replication_factor': 1};"
CREATE_SIMULATIONS_TABLE = "create table if not exists simulations.reports(id uuid, spellName text, casterLevel int, reportdata map<text, text>, primary key ((spellName, casterLevel), id));"
INSERT_REPORT = "insert into reports(id, spellName, casterLevel, reportdata) values (?, ?, ?, ?);"

class CassandraReportSystem(System):
    def __init__(self):
        super().__init__(['DamageTotal', 'Complete'])
        self.id = uuid1()
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

        # connect to cassandra cluster and insert report data
        cluster = Cluster()
        session = cluster.connect()
        
        # make sure we have a keyspace and connect to simulations
        session.execute(CREATE_KEYSPACE)
        session = cluster.connect('simulations')

        # make sure we have a table
        session.execute(CREATE_SIMULATIONS_TABLE)

        # prepare our insert statement
        insertStmt = session.prepare(INSERT_REPORT)

        # insert the report
        session.execute(insertStmt, (self.id, self.spellName, self.casterLevel, self.reportData))