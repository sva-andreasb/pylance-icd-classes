COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloCPDecisionEngine\n\n
    (final IloOptimDesc desc, final IloScenario scenario)\n
    '''
def makeModelAndEngine():
    '''returns IloOplModel\n\n
    makeModelAndEngine(final IloOplFactory factory, final IloOplModelDefinition def)\n
    '''
def runEngine():
    '''returns boolean\n\n
    runEngine()\n
    '''
def getCP():
    '''returns IloCP\n\n
    getCP()\n
    '''
def getModeler():
    '''returns IloModeler\n\n
    getModeler()\n
    '''
def getValueAccessor():
    '''returns IloValueAccessor\n\n
    getValueAccessor()\n
    '''
def getObjectiveValue():
    '''returns double\n\n
    getObjectiveValue()\n
    '''
def generateRequirementsPreview():
    '''returns IloTable\n\n
    generateRequirementsPreview(final boolean solve)\n
    '''
def solveFinished():
    '''returns None\n\n
    solveFinished(final IloCP cp)\n
    '''
