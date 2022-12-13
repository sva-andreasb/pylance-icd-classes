COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def IloDecisionModelImpl():
    '''public IloDecisionModelImpl(final String name, final IloDecisionModel parent)
    public IloDecisionModelImpl(final String name, final IloSharedDefs defs)
    '''
def setEngineController():
    '''public void setEngineController(final IloEngineController ctl)
    '''
def getEngineController():
    '''public IloEngineController getEngineController()
    '''
def getSharedDefs():
    '''public IloSharedDefs getSharedDefs()
    '''
def getId():
    '''public int getId()
    '''
def reset():
    '''public void reset()
    '''
def registerRequirement():
    '''public void registerRequirement(final IloRequirement req, final boolean force)
    public void registerRequirement(final IloRequirement r)
    '''
def unregisterRequirement():
    '''public IloRequirement unregisterRequirement(final String name)
    '''
def internalPutReq():
    '''public void internalPutReq(final IloRequirement req)
    '''
def internalRemoveReq():
    '''public IloRequirement internalRemoveReq(final String name)
    '''
def getRequirement():
    '''public IloRequirement getRequirement(final String name)
    public IloRequirement getRequirement(final String name, final boolean searchParent)
    public IloRequirement getRequirement(final IloRequirementId id)
    '''
def setParentModel():
    '''public void setParentModel(final IloDecisionModel model)
    '''
def getParentModel():
    '''public IloDecisionModel getParentModel()
    '''
def getObjective():
    '''public IloDecisionObjective getObjective(final String name)
    public IloDecisionObjective getObjective(final String name, final boolean transitive)
    public IloDecisionObjective getObjective(final IloObjectiveId id)
    '''
def registerObjective():
    '''public void registerObjective(final IloDecisionObjective o, final boolean force)
    '''
def unregisterObjective():
    '''public IloDecisionObjective unregisterObjective(final String name)
    '''
def getName():
    '''public String getName()
    public String getName()
    '''
def getObjectivePropsDef():
    '''public IloPropertiesDef getObjectivePropsDef()
    '''
def getDecisionVarPropsDef():
    '''public IloPropertiesDef getDecisionVarPropsDef()
    '''
def getReqPropertiesDef():
    '''public IloReqPropertiesDef getReqPropertiesDef()
    '''
def nextRequirementId():
    '''public int nextRequirementId()
    '''
def getRequirementFilter():
    '''public IloRequirementFilter getRequirementFilter(final String name, final boolean transitive)
    '''
def registerRequirementFilter():
    '''public void registerRequirementFilter(final String name, final IloRequirementFilter filter)
    '''
def unregisterRequirementFilter():
    '''public IloRequirementFilter unregisterRequirementFilter(final String name)
    '''
def getModel():
    '''public IloDecisionModel getModel()
    '''
def objectivesIterator():
    '''public Iterator<IloDecisionObjective> objectivesIterator()
    '''
def onRenameRequirement():
    '''public void onRenameRequirement(final IloRequirement r, final String oldName)
    '''
def getPriority():
    '''public IloPriority getPriority(final IloRequirement req)
    '''
def getProperty():
    '''public Object getProperty(final Element elt, final int propIndex)
    public Object getProperty(final int index, final boolean inherited)
    '''
def registerDecisionVariable():
    '''public void registerDecisionVariable(final IloDecisionVariable v, final boolean force)
    '''
def getDecisionVariable():
    '''public IloDecisionVariable getDecisionVariable(final String name)
    public IloDecisionVariable getDecisionVariable(final String name, final boolean searchParent)
    public IloDecisionVariable getDecisionVariable(final IloCompositeId name)
    '''
def internalRemoveVar():
    '''public void internalRemoveVar(final String name)
    '''
def internalPutVar():
    '''public void internalPutVar(final IloDecisionVariable var)
    '''
def getRequirementConnectorImpl():
    '''public IloRequirementConnectorImpl getRequirementConnectorImpl()
    '''
def hasNext():
    '''public boolean hasNext()
    public boolean hasNext()
    public boolean hasNext()
    '''
def next():
    '''public Object next()
    public IloRequirement next()
    public IloDecisionObjective next()
    '''
def remove():
    '''public void remove()
    public void remove()
    public void remove()
    '''
def getChildCount():
    '''public int getChildCount()
    '''
def isComposite():
    '''public boolean isComposite()
    '''
def isLeaf():
    '''public boolean isLeaf()
    '''
def getParent():
    '''public IloRequirementNode getParent()
    '''
def getDefaultPriorityManager():
    '''public IloDefaultPriorityManager getDefaultPriorityManager()
    '''
def getIntProperty():
    '''public int getIntProperty(final int index, final int defaultVal, final boolean inherited)
    '''
def getDoubleProperty():
    '''public double getDoubleProperty(final int index, final double defaultVal, final boolean inherited)
    '''
def getBooleanProperty():
    '''public boolean getBooleanProperty(final int index, final boolean defaultVal, final boolean inherited)
    '''
def setIntProperty():
    '''public void setIntProperty(final int index, final int value)
    '''
def setDoubleProperty():
    '''public void setDoubleProperty(final int index, final double value)
    '''
def setBooleanProperty():
    '''public void setBooleanProperty(final int index, final boolean value)
    '''
def setProperty():
    '''public void setProperty(final int index, final Object value)
    '''
def internalNullifyProp():
    '''public void internalNullifyProp(final int index, final boolean propagate)
    '''
def print():
    '''public IloTabulatedStream print(final IloTabulatedStream stm, final IloPublisher publisher)
    '''
def toString():
    '''public String toString()
    '''
def setName():
    '''public void setName(final String name)
    '''
def getExplanation():
    '''public IloMessage getExplanation()
    '''
def getFormattedExplanation():
    '''public String getFormattedExplanation(final IloMessageParameterFormatter ctl)
    '''
def setExplanation():
    '''public void setExplanation(final IloMessage message)
    public void setExplanation(final String text)
    '''
def getController():
    '''public IloEngineController getController()
    '''
