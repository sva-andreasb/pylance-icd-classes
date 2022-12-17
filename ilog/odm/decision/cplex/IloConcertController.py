COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def getCplexSharedDefs():
    '''returns IloCplexSharedDefs\n\n
    getCplexSharedDefs()\n
    '''
def getSharedDefs():
    '''returns IloSharedDefs\n\n
    getSharedDefs()\n
    '''
def getCurrentExecMode():
    '''returns int\n\n
    getCurrentExecMode()\n
    '''
def getModelingFactory():
    '''returns IloCplexModelingFactory\n\n
    getModelingFactory()\n
    '''
def registerRequirement():
    '''returns None\n\n
    registerRequirement(final IloCplexRequirement req, final IloPriority prio, final boolean force)\n
    registerRequirement(final IloCplexRequirement req, final IloPriority prio)\n
    '''
def registerWeightedObjective():
    '''returns IloWeightedObjective\n\n
    registerWeightedObjective(final String name, final IloCplexDecisionVariable o, final IloObjectiveSense sense)\n
    registerWeightedObjective(final String name, final IloCplexDecisionVariable o, final IloObjectiveSense sense, final double weight, final boolean force, final boolean isPublished, final boolean isMonitored)\n
    '''
def unregisterWeightedObjective():
    '''returns None\n\n
    unregisterWeightedObjective(final IloWeightedObjective obj)\n
    unregisterWeightedObjective(final String id)\n
    '''
def unregisterRequirement():
    '''returns IloRequirement\n\n
    unregisterRequirement(final IloRequirement req)\n
    unregisterRequirement(final IloRequirementId reqId)\n
    '''
def solveAnyway():
    '''returns boolean\n\n
    solveAnyway(final int timeLimitSeconds, final boolean optimizeObjective)\n
    '''
def onChangeProperty():
    '''returns None\n\n
    onChangeProperty(final IloDecisionObjective o, final int propIndex, final Object oldValue)\n
    onChangeProperty(final IloDecisionVariable o, final int propIndex, final Object oldValue)\n
    '''
def getCurrentObjective():
    '''returns IloObjective\n\n
    getCurrentObjective()\n
    '''
def isAborted():
    '''returns boolean\n\n
    isAborted()\n
    '''
def resetAbort():
    '''returns None\n\n
    resetAbort()\n
    '''
def setRelaxationPref():
    '''returns None\n\n
    setRelaxationPref(final IloRange range, final double pref)\n
    setRelaxationPref(final IloRange range, final double lbPref, final double ubPref)\n
    '''
def buildRequirement():
    '''returns IloRangeRequirement\n\n
    buildRequirement(final IloRange rg)\n
    '''
def getRequirementProps():
    '''returns IloCplexReqPropsDef\n\n
    getRequirementProps()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def isEnded():
    '''returns boolean\n\n
    isEnded()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def findObjectiveBound():
    '''returns boolean\n\n
    findObjectiveBound(final String objectiveName, final IloPriority lowestPriority, final int timeLimitSeconds, final boolean isBest)\n
    '''
def getScenarioProcessor():
    '''returns IloScenarioProcessor\n\n
    getScenarioProcessor()\n
    '''
def getHighestIgnoredPriority():
    '''returns IloPriority\n\n
    getHighestIgnoredPriority()\n
    '''
def ignorePriorityLowerOrEqualsTo():
    '''returns None\n\n
    ignorePriorityLowerOrEqualsTo(final IloPriority priority)\n
    '''
def getIssuesReport():
    '''returns IloIssuesReport\n\n
    getIssuesReport()\n
    '''
def getValueAccessor():
    '''returns IloValueAccessor\n\n
    getValueAccessor()\n
    '''
def setValueAccessor():
    '''returns None\n\n
    setValueAccessor(final IloValueAccessor accessor)\n
    '''
def getMonitoringManager():
    '''returns IloMonitoringManager\n\n
    getMonitoringManager()\n
    '''
def getRootRequirementNode():
    '''returns IloRequirementNode\n\n
    getRootRequirementNode()\n
    '''
def getRequirement():
    '''returns IloRequirement\n\n
    getRequirement(final IloRequirementId id)\n
    '''
def getObjective():
    '''returns IloWeightedObjective\n\n
    getObjective(final String objectiveName)\n
    '''
def getRequirementConnector():
    '''returns IloRequirementConnector\n\n
    getRequirementConnector()\n
    '''
def getTreeBuilder():
    '''returns IloRequirementTreeBuilder\n\n
    getTreeBuilder()\n
    '''
def setTreeBuilder():
    '''returns None\n\n
    setTreeBuilder(final IloRequirementTreeBuilder treeBuilder)\n
    '''
def getIssueReporter():
    '''returns IloIssueReporter\n\n
    getIssueReporter()\n
    '''
def setIssueReporter():
    '''returns None\n\n
    setIssueReporter(final IloIssueReporter errorReporter)\n
    '''
def getModelName():
    '''returns String\n\n
    getModelName()\n
    '''
def setModelName():
    '''returns None\n\n
    setModelName(final String modelName)\n
    '''
def getAlgorithmHeuristic():
    '''returns int\n\n
    getAlgorithmHeuristic()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns IloCplexRequirement\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
