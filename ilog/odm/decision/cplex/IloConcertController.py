COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def getCplexSharedDefs():
    '''    public IloCplexSharedDefs getCplexSharedDefs()
    '''
def getSharedDefs():
    '''    public IloSharedDefs getSharedDefs()
    '''
def getCurrentExecMode():
    '''    public int getCurrentExecMode()
    '''
def getModelingFactory():
    '''    public IloCplexModelingFactory getModelingFactory()
    '''
def registerRequirement():
    '''    public void registerRequirement(final IloCplexRequirement req, final IloPriority prio, final boolean force)
    public void registerRequirement(final IloCplexRequirement req, final IloPriority prio)
    '''
def registerWeightedObjective():
    '''    public IloWeightedObjective registerWeightedObjective(final String name, final IloCplexDecisionVariable o, final IloObjectiveSense sense)
    public IloWeightedObjective registerWeightedObjective(final String name, final IloCplexDecisionVariable o, final IloObjectiveSense sense, final double weight, final boolean force, final boolean isPublished, final boolean isMonitored)
    '''
def unregisterWeightedObjective():
    '''    public void unregisterWeightedObjective(final IloWeightedObjective obj)
    public void unregisterWeightedObjective(final String id)
    '''
def unregisterRequirement():
    '''    public void unregisterRequirement(final IloRequirement req)
    public IloRequirement unregisterRequirement(final IloRequirementId reqId)
    '''
def solveAnyway():
    '''    public boolean solveAnyway(final int timeLimitSeconds, final boolean optimizeObjective)
    '''
def onChangeProperty():
    '''    public void onChangeProperty(final IloDecisionObjective o, final int propIndex, final Object oldValue)
    public void onChangeProperty(final IloDecisionVariable o, final int propIndex, final Object oldValue)
    '''
def getCurrentObjective():
    '''    public IloObjective getCurrentObjective()
    '''
def isAborted():
    '''    public boolean isAborted()
    '''
def resetAbort():
    '''    public void resetAbort()
    '''
def setRelaxationPref():
    '''    public void setRelaxationPref(final IloRange range, final double pref)
    public void setRelaxationPref(final IloRange range, final double lbPref, final double ubPref)
    '''
def buildRequirement():
    '''    public IloRangeRequirement buildRequirement(final IloRange rg)
    '''
def getRequirementProps():
    '''    public IloCplexReqPropsDef getRequirementProps()
    '''
def end():
    '''    public void end()
    '''
def isEnded():
    '''    public boolean isEnded()
    '''
def abort():
    '''    public void abort()
    '''
def findObjectiveBound():
    '''    public boolean findObjectiveBound(final String objectiveName, final IloPriority lowestPriority, final int timeLimitSeconds, final boolean isBest)
    '''
def getScenarioProcessor():
    '''    public IloScenarioProcessor getScenarioProcessor()
    '''
def getHighestIgnoredPriority():
    '''    public IloPriority getHighestIgnoredPriority()
    '''
def ignorePriorityLowerOrEqualsTo():
    '''    public void ignorePriorityLowerOrEqualsTo(final IloPriority priority)
    '''
def getIssuesReport():
    '''    public IloIssuesReport getIssuesReport()
    '''
def getValueAccessor():
    '''    public IloValueAccessor getValueAccessor()
    '''
def setValueAccessor():
    '''    public void setValueAccessor(final IloValueAccessor accessor)
    '''
def getMonitoringManager():
    '''    public IloMonitoringManager getMonitoringManager()
    '''
def getRootRequirementNode():
    '''    public IloRequirementNode getRootRequirementNode()
    '''
def getRequirement():
    '''    public IloRequirement getRequirement(final IloRequirementId id)
    '''
def getObjective():
    '''    public IloWeightedObjective getObjective(final String objectiveName)
    '''
def getRequirementConnector():
    '''    public IloRequirementConnector getRequirementConnector()
    '''
def getTreeBuilder():
    '''    public IloRequirementTreeBuilder getTreeBuilder()
    '''
def setTreeBuilder():
    '''    public void setTreeBuilder(final IloRequirementTreeBuilder treeBuilder)
    '''
def getIssueReporter():
    '''    public IloIssueReporter getIssueReporter()
    '''
def setIssueReporter():
    '''    public void setIssueReporter(final IloIssueReporter errorReporter)
    '''
def getModelName():
    '''    public String getModelName()
    '''
def setModelName():
    '''    public void setModelName(final String modelName)
    '''
def getAlgorithmHeuristic():
    '''    public int getAlgorithmHeuristic()
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def next():
    '''    public IloCplexRequirement next()
    '''
def remove():
    '''    public void remove()
    '''
