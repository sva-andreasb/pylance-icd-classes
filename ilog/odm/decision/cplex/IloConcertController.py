COPYRIGHT_NOTICE = "String  Copyright IBM Corporation 2005,2012""
def getCplexSharedDefs():
'''public IloCplexSharedDefs getCplexSharedDefs()
'''
pass
def getSharedDefs():
'''public IloSharedDefs getSharedDefs()
'''
pass
def getCurrentExecMode():
'''public int getCurrentExecMode()
'''
pass
def getModelingFactory():
'''public IloCplexModelingFactory getModelingFactory()
'''
pass
def registerRequirement():
'''public void registerRequirement(final IloCplexRequirement req, final IloPriority prio, final boolean force)
public void registerRequirement(final IloCplexRequirement req, final IloPriority prio)
'''
pass
def registerWeightedObjective():
'''public IloWeightedObjective registerWeightedObjective(final String name, final IloCplexDecisionVariable o, final IloObjectiveSense sense)
public IloWeightedObjective registerWeightedObjective(final String name, final IloCplexDecisionVariable o, final IloObjectiveSense sense, final double weight, final boolean force, final boolean isPublished, final boolean isMonitored)
'''
pass
def unregisterWeightedObjective():
'''public void unregisterWeightedObjective(final IloWeightedObjective obj)
public void unregisterWeightedObjective(final String id)
'''
pass
def unregisterRequirement():
'''public void unregisterRequirement(final IloRequirement req)
public IloRequirement unregisterRequirement(final IloRequirementId reqId)
'''
pass
def solveAnyway():
'''public boolean solveAnyway(final int timeLimitSeconds, final boolean optimizeObjective)
'''
pass
def onChangeProperty():
'''public void onChangeProperty(final IloDecisionObjective o, final int propIndex, final Object oldValue)
public void onChangeProperty(final IloDecisionVariable o, final int propIndex, final Object oldValue)
'''
pass
def getCurrentObjective():
'''public IloObjective getCurrentObjective()
'''
pass
def isAborted():
'''public boolean isAborted()
'''
pass
def resetAbort():
'''public void resetAbort()
'''
pass
def setRelaxationPref():
'''public void setRelaxationPref(final IloRange range, final double pref)
public void setRelaxationPref(final IloRange range, final double lbPref, final double ubPref)
'''
pass
def buildRequirement():
'''public IloRangeRequirement buildRequirement(final IloRange rg)
'''
pass
def getRequirementProps():
'''public IloCplexReqPropsDef getRequirementProps()
'''
pass
def end():
'''public void end()
'''
pass
def isEnded():
'''public boolean isEnded()
'''
pass
def abort():
'''public void abort()
'''
pass
def findObjectiveBound():
'''public boolean findObjectiveBound(final String objectiveName, final IloPriority lowestPriority, final int timeLimitSeconds, final boolean isBest)
'''
pass
def getScenarioProcessor():
'''public IloScenarioProcessor getScenarioProcessor()
'''
pass
def getHighestIgnoredPriority():
'''public IloPriority getHighestIgnoredPriority()
'''
pass
def ignorePriorityLowerOrEqualsTo():
'''public void ignorePriorityLowerOrEqualsTo(final IloPriority priority)
'''
pass
def getIssuesReport():
'''public IloIssuesReport getIssuesReport()
'''
pass
def getValueAccessor():
'''public IloValueAccessor getValueAccessor()
'''
pass
def setValueAccessor():
'''public void setValueAccessor(final IloValueAccessor accessor)
'''
pass
def getMonitoringManager():
'''public IloMonitoringManager getMonitoringManager()
'''
pass
def getRootRequirementNode():
'''public IloRequirementNode getRootRequirementNode()
'''
pass
def getRequirement():
'''public IloRequirement getRequirement(final IloRequirementId id)
'''
pass
def getObjective():
'''public IloWeightedObjective getObjective(final String objectiveName)
'''
pass
def getRequirementConnector():
'''public IloRequirementConnector getRequirementConnector()
'''
pass
def getTreeBuilder():
'''public IloRequirementTreeBuilder getTreeBuilder()
'''
pass
def setTreeBuilder():
'''public void setTreeBuilder(final IloRequirementTreeBuilder treeBuilder)
'''
pass
def getIssueReporter():
'''public IloIssueReporter getIssueReporter()
'''
pass
def setIssueReporter():
'''public void setIssueReporter(final IloIssueReporter errorReporter)
'''
pass
def getModelName():
'''public String getModelName()
'''
pass
def setModelName():
'''public void setModelName(final String modelName)
'''
pass
def getAlgorithmHeuristic():
'''public int getAlgorithmHeuristic()
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def next():
'''public IloCplexRequirement next()
'''
pass
def remove():
'''public void remove()
'''
pass
