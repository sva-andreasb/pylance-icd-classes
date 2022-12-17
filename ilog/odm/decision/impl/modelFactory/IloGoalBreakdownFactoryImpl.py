COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloGoalBreakdownFactoryImpl\n\n
    (final IloOplArgumentDescEvaluatorContext context, final IloMessageParameterFormatter messageFormater, final IloBreakdownVariableFactory factory, final IloObjectiveModel model, final String modelId)\n
    (final IloOplArgumentDescEvaluatorContext context, final IloMessageParameterFormatter messageFormater, final IloBreakdownVariableFactory factory, final IloObjectiveModel goalModel, final String modelId, final IloSolveAnywayCallback monitor)\n
    '''
def onSearchFeasibleSolution():
    '''returns boolean\n\n
    onSearchFeasibleSolution(final String model, final IloPriority maxRelaxablePriorityLevel, final Collection<?> relaxblesRanges, final boolean isHighestRelaxablePriority)\n
    '''
def onSearchOptimalSolution():
    '''returns boolean\n\n
    onSearchOptimalSolution(final String model, final IloPriority maxRelaxablePriorityLevel)\n
    '''
def onBuildModel():
    '''returns boolean\n\n
    onBuildModel(final String modelingType, final String model, final String label)\n
    '''
def onPublishSolution():
    '''returns boolean\n\n
    onPublishSolution(final String publicationType, final String model, final String label)\n
    '''
def getMonitor():
    '''returns IloSolveAnywayCallback\n\n
    getMonitor()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def isEvalutingKey():
    '''returns boolean\n\n
    isEvalutingKey()\n
    '''
def publishGoalsBreakdown():
    '''returns None\n\n
    publishGoalsBreakdown()\n
    '''
def addLeafDecisionVariableValue():
    '''returns None\n\n
    addLeafDecisionVariableValue(final IloBreakdownVariable rootVariable, final DexprDesc desc, final Parameter parameter, final double value)\n
    '''
def makeTopDecisionVariableValue():
    '''returns IloBreakdownVariable\n\n
    makeTopDecisionVariableValue(final DexprDesc desc, final double value)\n
    '''
def getDexprDesc():
    '''returns DexprDesc\n\n
    getDexprDesc(final String name)\n
    '''
def getEvaluatorContext():
    '''returns IloOplArgumentDescEvaluatorContext\n\n
    getEvaluatorContext()\n
    '''
def setSubModelDesc():
    '''returns None\n\n
    setSubModelDesc(final SubModelDesc subModelDesc)\n
    '''
