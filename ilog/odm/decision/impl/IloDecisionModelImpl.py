COPYRIGHT_NOTICE = "String  Copyright IBM Corporation 2005,2012""
def IloDecisionModelImpl():
'''public IloDecisionModelImpl(final String name, final IloDecisionModel parent)
public IloDecisionModelImpl(final String name, final IloSharedDefs defs)
'''
pass
def setEngineController():
'''public void setEngineController(final IloEngineController ctl)
'''
pass
def getEngineController():
'''public IloEngineController getEngineController()
'''
pass
def getSharedDefs():
'''public IloSharedDefs getSharedDefs()
'''
pass
def getId():
'''public int getId()
'''
pass
def reset():
'''public void reset()
'''
pass
def registerRequirement():
'''public void registerRequirement(final IloRequirement req, final boolean force)
public void registerRequirement(final IloRequirement r)
'''
pass
def unregisterRequirement():
'''public IloRequirement unregisterRequirement(final String name)
'''
pass
def internalPutReq():
'''public void internalPutReq(final IloRequirement req)
'''
pass
def internalRemoveReq():
'''public IloRequirement internalRemoveReq(final String name)
'''
pass
def getRequirement():
'''public IloRequirement getRequirement(final String name)
public IloRequirement getRequirement(final String name, final boolean searchParent)
public IloRequirement getRequirement(final IloRequirementId id)
'''
pass
def setParentModel():
'''public void setParentModel(final IloDecisionModel model)
'''
pass
def getParentModel():
'''public IloDecisionModel getParentModel()
'''
pass
def getObjective():
'''public IloDecisionObjective getObjective(final String name)
public IloDecisionObjective getObjective(final String name, final boolean transitive)
public IloDecisionObjective getObjective(final IloObjectiveId id)
'''
pass
def registerObjective():
'''public void registerObjective(final IloDecisionObjective o, final boolean force)
'''
pass
def unregisterObjective():
'''public IloDecisionObjective unregisterObjective(final String name)
'''
pass
def getName():
'''public String getName()
public String getName()
'''
pass
def getObjectivePropsDef():
'''public IloPropertiesDef getObjectivePropsDef()
'''
pass
def getDecisionVarPropsDef():
'''public IloPropertiesDef getDecisionVarPropsDef()
'''
pass
def getReqPropertiesDef():
'''public IloReqPropertiesDef getReqPropertiesDef()
'''
pass
def nextRequirementId():
'''public int nextRequirementId()
'''
pass
def getRequirementFilter():
'''public IloRequirementFilter getRequirementFilter(final String name, final boolean transitive)
'''
pass
def registerRequirementFilter():
'''public void registerRequirementFilter(final String name, final IloRequirementFilter filter)
'''
pass
def unregisterRequirementFilter():
'''public IloRequirementFilter unregisterRequirementFilter(final String name)
'''
pass
def getModel():
'''public IloDecisionModel getModel()
'''
pass
def objectivesIterator():
'''public Iterator<IloDecisionObjective> objectivesIterator()
'''
pass
def onRenameRequirement():
'''public void onRenameRequirement(final IloRequirement r, final String oldName)
'''
pass
def getPriority():
'''public IloPriority getPriority(final IloRequirement req)
'''
pass
def getProperty():
'''public Object getProperty(final Element elt, final int propIndex)
public Object getProperty(final int index, final boolean inherited)
'''
pass
def registerDecisionVariable():
'''public void registerDecisionVariable(final IloDecisionVariable v, final boolean force)
'''
pass
def getDecisionVariable():
'''public IloDecisionVariable getDecisionVariable(final String name)
public IloDecisionVariable getDecisionVariable(final String name, final boolean searchParent)
public IloDecisionVariable getDecisionVariable(final IloCompositeId name)
'''
pass
def internalRemoveVar():
'''public void internalRemoveVar(final String name)
'''
pass
def internalPutVar():
'''public void internalPutVar(final IloDecisionVariable var)
'''
pass
def getRequirementConnectorImpl():
'''public IloRequirementConnectorImpl getRequirementConnectorImpl()
'''
pass
def hasNext():
'''public boolean hasNext()
public boolean hasNext()
public boolean hasNext()
'''
pass
def next():
'''public Object next()
public IloRequirement next()
public IloDecisionObjective next()
'''
pass
def remove():
'''public void remove()
public void remove()
public void remove()
'''
pass
def getChildCount():
'''public int getChildCount()
'''
pass
def isComposite():
'''public boolean isComposite()
'''
pass
def isLeaf():
'''public boolean isLeaf()
'''
pass
def getParent():
'''public IloRequirementNode getParent()
'''
pass
def getDefaultPriorityManager():
'''public IloDefaultPriorityManager getDefaultPriorityManager()
'''
pass
def getIntProperty():
'''public int getIntProperty(final int index, final int defaultVal, final boolean inherited)
'''
pass
def getDoubleProperty():
'''public double getDoubleProperty(final int index, final double defaultVal, final boolean inherited)
'''
pass
def getBooleanProperty():
'''public boolean getBooleanProperty(final int index, final boolean defaultVal, final boolean inherited)
'''
pass
def setIntProperty():
'''public void setIntProperty(final int index, final int value)
'''
pass
def setDoubleProperty():
'''public void setDoubleProperty(final int index, final double value)
'''
pass
def setBooleanProperty():
'''public void setBooleanProperty(final int index, final boolean value)
'''
pass
def setProperty():
'''public void setProperty(final int index, final Object value)
'''
pass
def internalNullifyProp():
'''public void internalNullifyProp(final int index, final boolean propagate)
'''
pass
def print():
'''public IloTabulatedStream print(final IloTabulatedStream stm, final IloPublisher publisher)
'''
pass
def toString():
'''public String toString()
'''
pass
def setName():
'''public void setName(final String name)
'''
pass
def getExplanation():
'''public IloMessage getExplanation()
'''
pass
def getFormattedExplanation():
'''public String getFormattedExplanation(final IloMessageParameterFormatter ctl)
'''
pass
def setExplanation():
'''public void setExplanation(final IloMessage message)
public void setExplanation(final String text)
'''
pass
def getController():
'''public IloEngineController getController()
'''
pass
