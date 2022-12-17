COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns GapAndOptimalityInfo\n\n
    (final IloCplexController controller)\n
    (final double gap, final boolean hasGap, final boolean isOptimal)\n
    '''
def getController():
    '''returns IloCplexController\n\n
    getController()\n
    '''
def publishOptimResultStatus():
    '''returns None\n\n
    publishOptimResultStatus(final IloOptimResultStatus report)\n
    '''
def updateOptimResultStatus():
    '''returns None\n\n
    updateOptimResultStatus(final IloOptimResultStatus report)\n
    '''
def changeRequirementPriorities():
    '''returns IloRequirementId[]\n\n
    changeRequirementPriorities(final IloTable requirementPropertyInput)\n
    '''
def executeEngine():
    '''returns boolean\n\n
    executeEngine(final IloEngineRequest request)\n
    '''
def makeExplanationTable():
    '''returns IloOrderedTableImpl\n\n
    makeExplanationTable()\n
    makeExplanationTable(final IloExplanation explanation, final IloSolutionReport solutionReport)\n
    '''
def getScenarioInput():
    '''returns IloScenarioInput\n\n
    getScenarioInput()\n
    '''
def getErrorReport():
    '''returns IloErrorReport\n\n
    getErrorReport()\n
    '''
def setErrorReporter():
    '''returns None\n\n
    setErrorReporter(final IloErrorReporter reporter)\n
    '''
def setScenarioInput():
    '''returns None\n\n
    setScenarioInput(final IloScenarioInput input)\n
    '''
def setEngineRequest():
    '''returns None\n\n
    setEngineRequest(final IloEngineRequest request)\n
    '''
def getEngineRequest():
    '''returns IloEngineRequest\n\n
    getEngineRequest()\n
    '''
def setScenarioInfo():
    '''returns None\n\n
    setScenarioInfo(final IloScenarioInfo info)\n
    '''
def addDecisonVariablesConstraints():
    '''returns IloCompositeId[]\n\n
    addDecisonVariablesConstraints(final IloDecisionVariableConstraints constraints)\n
    '''
def findGoalBound():
    '''returns IloGoalBoundsReport\n\n
    findGoalBound(final IloGoalBoundsRequest request, final IloGoalBoundsReport goalReport, final IloSolvingInterrupter interrupter)\n
    '''
def publishGoalBoundResults():
    '''returns None\n\n
    publishGoalBoundResults(final IloGoalBoundsReport goalReport, final IloCplexController controller, final String objName, final String sPriority, final boolean isBest)\n
    '''
def publishGoalReports():
    '''returns boolean\n\n
    publishGoalReports()\n
    publishGoalReports(final IloPersistentGoalReport target, final boolean isMonitoring)\n
    '''
def makeGoalReportTable():
    '''returns boolean\n\n
    makeGoalReportTable(final IloOrderedTableImpl result, final boolean isMonitoring)\n
    '''
def publishDecisionVariableReports():
    '''returns None\n\n
    publishDecisionVariableReports()\n
    '''
def makeDecisionVariablesTable():
    '''returns IloOrderedTableImpl\n\n
    makeDecisionVariablesTable(final IloSchemaImpl schema)\n
    '''
def publishExplanation():
    '''returns None\n\n
    publishExplanation()\n
    '''
def getDefaultPriorityManager():
    '''returns IloDefaultPriorityManager\n\n
    getDefaultPriorityManager()\n
    '''
def getScenarioInfo():
    '''returns IloScenarioInfo\n\n
    getScenarioInfo()\n
    '''
def getGap():
    '''returns double\n\n
    getGap()\n
    '''
def hasGap():
    '''returns boolean\n\n
    hasGap()\n
    '''
def isOptimal():
    '''returns boolean\n\n
    isOptimal()\n
    '''
