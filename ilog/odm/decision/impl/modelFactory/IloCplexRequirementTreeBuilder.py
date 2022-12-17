COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloCplexRequirementTreeBuilder\n\n
    (final IloCplexController controller, final IloOptimDesc desc)\n
    '''
def addConstraint():
    '''returns IloRequirement\n\n
    addConstraint(final String ctLabel, final IloConstraint ct, final String[] indexNames, final Object[] indexValues)\n
    '''
def getDynamicConstraintDesc():
    '''returns IloConstraintDesc\n\n
    getDynamicConstraintDesc(final String label)\n
    '''
def getDexprDesc():
    '''returns DexprDesc\n\n
    getDexprDesc(final String dexpr)\n
    '''
def registerTree():
    '''returns None\n\n
    registerTree()\n
    '''
def setConstants():
    '''returns None\n\n
    setConstants(final String[] constantNames, final Object[] constantValues)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def addLeafDecisionVariableValue():
    '''returns None\n\n
    addLeafDecisionVariableValue(final IloBreakdownVariable rootVariable, final DexprDesc desc, final Parameter parameter, final double value)\n
    '''
def makeTopDecisionVariableValue():
    '''returns IloBreakdownVariable\n\n
    makeTopDecisionVariableValue(final DexprDesc desc, final double value)\n
    '''
def getOptimFileName():
    '''returns String\n\n
    getOptimFileName()\n
    '''
def getModelDesc():
    '''returns SubModelDesc\n\n
    getModelDesc()\n
    '''
def setModelDesc():
    '''returns None\n\n
    setModelDesc(final SubModelDesc modelDesc)\n
    '''
def getOptimModelDescription():
    '''returns IloOptimDesc\n\n
    getOptimModelDescription()\n
    '''
def getCplexController():
    '''returns IloCplexController\n\n
    getCplexController()\n
    '''
def updateControllerModelName():
    '''returns None\n\n
    updateControllerModelName()\n
    '''
def getValueAccessor():
    '''returns IloValueAccessor\n\n
    getValueAccessor()\n
    '''
def getIssueReporter():
    '''returns IloIssueReporter\n\n
    getIssueReporter()\n
    '''
def getModelName():
    '''returns String\n\n
    getModelName()\n
    '''
def getCompiledOptimModelDescription():
    '''returns IloCompiledOptimDesc\n\n
    getCompiledOptimModelDescription()\n
    '''
