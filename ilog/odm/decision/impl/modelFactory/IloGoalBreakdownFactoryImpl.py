COPYRIGHT_NOTICE = "String  Copyright IBM Corporation 2005,2012""
def IloGoalBreakdownFactoryImpl():
'''public IloGoalBreakdownFactoryImpl(final IloOplArgumentDescEvaluatorContext context, final IloMessageParameterFormatter messageFormater, final IloBreakdownVariableFactory factory, final IloObjectiveModel model, final String modelId)
public IloGoalBreakdownFactoryImpl(final IloOplArgumentDescEvaluatorContext context, final IloMessageParameterFormatter messageFormater, final IloBreakdownVariableFactory factory, final IloObjectiveModel goalModel, final String modelId, final IloSolveAnywayCallback monitor)
'''
pass
def onSearchFeasibleSolution():
'''public boolean onSearchFeasibleSolution(final String model, final IloPriority maxRelaxablePriorityLevel, final Collection<?> relaxblesRanges, final boolean isHighestRelaxablePriority)
'''
pass
def onSearchOptimalSolution():
'''public boolean onSearchOptimalSolution(final String model, final IloPriority maxRelaxablePriorityLevel)
'''
pass
def onBuildModel():
'''public boolean onBuildModel(final String modelingType, final String model, final String label)
'''
pass
def onPublishSolution():
'''public boolean onPublishSolution(final String publicationType, final String model, final String label)
'''
pass
def getMonitor():
'''public IloSolveAnywayCallback getMonitor()
'''
pass
def end():
'''public void end()
'''
pass
def isEvalutingKey():
'''public boolean isEvalutingKey()
'''
pass
def publishGoalsBreakdown():
'''public void publishGoalsBreakdown()
'''
pass
def addLeafDecisionVariableValue():
'''public void addLeafDecisionVariableValue(final IloBreakdownVariable rootVariable, final DexprDesc desc, final Parameter parameter, final double value)
'''
pass
def makeTopDecisionVariableValue():
'''public IloBreakdownVariable makeTopDecisionVariableValue(final DexprDesc desc, final double value)
'''
pass
def getDexprDesc():
'''public DexprDesc getDexprDesc(final String name)
'''
pass
def getEvaluatorContext():
'''public IloOplArgumentDescEvaluatorContext getEvaluatorContext()
'''
pass
def setSubModelDesc():
'''public void setSubModelDesc(final SubModelDesc subModelDesc)
'''
pass
