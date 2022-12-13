COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def IloScenarioProcessor():
    '''public IloScenarioProcessor(final IloCplexController controller)
    '''
def getController():
    '''public IloCplexController getController()
    '''
def publishOptimResultStatus():
    '''public void publishOptimResultStatus(final IloOptimResultStatus report)
    '''
def updateOptimResultStatus():
    '''public void updateOptimResultStatus(final IloOptimResultStatus report)
    '''
def changeRequirementPriorities():
    '''public IloRequirementId[] changeRequirementPriorities(final IloTable requirementPropertyInput)
    '''
def executeEngine():
    '''public boolean executeEngine(final IloEngineRequest request)
    '''
def makeExplanationTable():
    '''public IloOrderedTableImpl makeExplanationTable()
    public IloOrderedTableImpl makeExplanationTable(final IloExplanation explanation, final IloSolutionReport solutionReport)
    '''
def getScenarioInput():
    '''public IloScenarioInput getScenarioInput()
    '''
def getErrorReport():
    '''public IloErrorReport getErrorReport()
    '''
def setErrorReporter():
    '''public void setErrorReporter(final IloErrorReporter reporter)
    '''
def setScenarioInput():
    '''public void setScenarioInput(final IloScenarioInput input)
    '''
def setEngineRequest():
    '''public void setEngineRequest(final IloEngineRequest request)
    '''
def getEngineRequest():
    '''public IloEngineRequest getEngineRequest()
    '''
def setScenarioInfo():
    '''public void setScenarioInfo(final IloScenarioInfo info)
    '''
def addDecisonVariablesConstraints():
    '''public IloCompositeId[] addDecisonVariablesConstraints(final IloDecisionVariableConstraints constraints)
    '''
def findGoalBound():
    '''public IloGoalBoundsReport findGoalBound(final IloGoalBoundsRequest request, final IloGoalBoundsReport goalReport, final IloSolvingInterrupter interrupter)
    '''
def publishGoalBoundResults():
    '''public void publishGoalBoundResults(final IloGoalBoundsReport goalReport, final IloCplexController controller, final String objName, final String sPriority, final boolean isBest)
    '''
def publishGoalReports():
    '''public boolean publishGoalReports()
    public boolean publishGoalReports(final IloPersistentGoalReport target, final boolean isMonitoring)
    '''
def makeGoalReportTable():
    '''public boolean makeGoalReportTable(final IloOrderedTableImpl result, final boolean isMonitoring)
    '''
def publishDecisionVariableReports():
    '''public void publishDecisionVariableReports()
    '''
def makeDecisionVariablesTable():
    '''public IloOrderedTableImpl makeDecisionVariablesTable(final IloSchemaImpl schema)
    '''
def publishExplanation():
    '''public void publishExplanation()
    '''
def getDefaultPriorityManager():
    '''public IloDefaultPriorityManager getDefaultPriorityManager()
    '''
def getScenarioInfo():
    '''public IloScenarioInfo getScenarioInfo()
    '''
def GapAndOptimalityInfo():
    '''public GapAndOptimalityInfo(final double gap, final boolean hasGap, final boolean isOptimal)
    '''
def getGap():
    '''public double getGap()
    '''
def hasGap():
    '''public boolean hasGap()
    '''
def isOptimal():
    '''public boolean isOptimal()
    '''
