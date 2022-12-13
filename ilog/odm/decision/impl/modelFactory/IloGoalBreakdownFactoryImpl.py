COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def IloGoalBreakdownFactoryImpl():
    '''public IloGoalBreakdownFactoryImpl(final IloOplArgumentDescEvaluatorContext context, final IloMessageParameterFormatter messageFormater, final IloBreakdownVariableFactory factory, final IloObjectiveModel model, final String modelId)
    public IloGoalBreakdownFactoryImpl(final IloOplArgumentDescEvaluatorContext context, final IloMessageParameterFormatter messageFormater, final IloBreakdownVariableFactory factory, final IloObjectiveModel goalModel, final String modelId, final IloSolveAnywayCallback monitor)
    '''
def onSearchFeasibleSolution():
    '''public boolean onSearchFeasibleSolution(final String model, final IloPriority maxRelaxablePriorityLevel, final Collection<?> relaxblesRanges, final boolean isHighestRelaxablePriority)
    '''
def onSearchOptimalSolution():
    '''public boolean onSearchOptimalSolution(final String model, final IloPriority maxRelaxablePriorityLevel)
    '''
def onBuildModel():
    '''public boolean onBuildModel(final String modelingType, final String model, final String label)
    '''
def onPublishSolution():
    '''public boolean onPublishSolution(final String publicationType, final String model, final String label)
    '''
def getMonitor():
    '''public IloSolveAnywayCallback getMonitor()
    '''
def end():
    '''public void end()
    '''
def isEvalutingKey():
    '''public boolean isEvalutingKey()
    '''
def publishGoalsBreakdown():
    '''public void publishGoalsBreakdown()
    '''
def addLeafDecisionVariableValue():
    '''public void addLeafDecisionVariableValue(final IloBreakdownVariable rootVariable, final DexprDesc desc, final Parameter parameter, final double value)
    '''
def makeTopDecisionVariableValue():
    '''public IloBreakdownVariable makeTopDecisionVariableValue(final DexprDesc desc, final double value)
    '''
def getDexprDesc():
    '''public DexprDesc getDexprDesc(final String name)
    '''
def getEvaluatorContext():
    '''public IloOplArgumentDescEvaluatorContext getEvaluatorContext()
    '''
def setSubModelDesc():
    '''public void setSubModelDesc(final SubModelDesc subModelDesc)
    '''
