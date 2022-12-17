COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloOplControllerFactory\n\n
    (final IloOptimDesc desc, final IloScenario scenario)\n
    (final IloCplex cplex)\n
    '''
def notifyChanged():
    '''returns None\n\n
    notifyChanged(final Object source)\n
    '''
def getModeler():
    '''returns IloModeler\n\n
    getModeler()\n
    '''
def generateRequirementsPreview():
    '''returns IloTable\n\n
    generateRequirementsPreview(final boolean solve)\n
    '''
def makeModelAndEngine():
    '''returns IloOplModel\n\n
    makeModelAndEngine(final IloOplFactory factory, final IloOplModelDefinition def)\n
    '''
def getMappingAccessor():
    '''returns IloOplMappingAccessor\n\n
    getMappingAccessor()\n
    '''
def getCplexController():
    '''returns IloOplCplexController\n\n
    getCplexController()\n
    '''
def runEngine():
    '''returns boolean\n\n
    runEngine()\n
    '''
def setupScenarioInfo():
    '''returns None\n\n
    setupScenarioInfo(final IloScenarioInfo info, final IloScenario scenario)\n
    '''
def freeMemory():
    '''returns None\n\n
    freeMemory()\n
    '''
def postProcessResult():
    '''returns None\n\n
    postProcessResult()\n
    '''
def getValueAccessor():
    '''returns IloValueAccessor\n\n
    getValueAccessor()\n
    '''
def getCplex():
    '''returns IloCplex\n\n
    getCplex()\n
    '''
def getObjectiveValue():
    '''returns double\n\n
    getObjectiveValue()\n
    '''
