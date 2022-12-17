COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDecisionModelImpl\n\n
    (final String name, final IloDecisionModel parent)\n
    (final String name, final IloSharedDefs defs)\n
    '''
def setEngineController():
    '''returns None\n\n
    setEngineController(final IloEngineController ctl)\n
    '''
def getEngineController():
    '''returns IloEngineController\n\n
    getEngineController()\n
    '''
def getSharedDefs():
    '''returns IloSharedDefs\n\n
    getSharedDefs()\n
    '''
def getId():
    '''returns int\n\n
    getId()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def registerRequirement():
    '''returns None\n\n
    registerRequirement(final IloRequirement req, final boolean force)\n
    registerRequirement(final IloRequirement r)\n
    '''
def unregisterRequirement():
    '''returns IloRequirement\n\n
    unregisterRequirement(final String name)\n
    '''
def internalPutReq():
    '''returns None\n\n
    internalPutReq(final IloRequirement req)\n
    '''
def internalRemoveReq():
    '''returns IloRequirement\n\n
    internalRemoveReq(final String name)\n
    '''
def getRequirement():
    '''returns IloRequirement\n\n
    getRequirement(final String name)\n
    getRequirement(final String name, final boolean searchParent)\n
    getRequirement(final IloRequirementId id)\n
    '''
def setParentModel():
    '''returns None\n\n
    setParentModel(final IloDecisionModel model)\n
    '''
def getParentModel():
    '''returns IloDecisionModel\n\n
    getParentModel()\n
    '''
def getObjective():
    '''returns IloDecisionObjective\n\n
    getObjective(final String name)\n
    getObjective(final String name, final boolean transitive)\n
    getObjective(final IloObjectiveId id)\n
    '''
def registerObjective():
    '''returns None\n\n
    registerObjective(final IloDecisionObjective o, final boolean force)\n
    '''
def unregisterObjective():
    '''returns IloDecisionObjective\n\n
    unregisterObjective(final String name)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    getName()\n
    '''
def getObjectivePropsDef():
    '''returns IloPropertiesDef\n\n
    getObjectivePropsDef()\n
    '''
def getDecisionVarPropsDef():
    '''returns IloPropertiesDef\n\n
    getDecisionVarPropsDef()\n
    '''
def getReqPropertiesDef():
    '''returns IloReqPropertiesDef\n\n
    getReqPropertiesDef()\n
    '''
def nextRequirementId():
    '''returns int\n\n
    nextRequirementId()\n
    '''
def getRequirementFilter():
    '''returns IloRequirementFilter\n\n
    getRequirementFilter(final String name, final boolean transitive)\n
    '''
def registerRequirementFilter():
    '''returns None\n\n
    registerRequirementFilter(final String name, final IloRequirementFilter filter)\n
    '''
def unregisterRequirementFilter():
    '''returns IloRequirementFilter\n\n
    unregisterRequirementFilter(final String name)\n
    '''
def getModel():
    '''returns IloDecisionModel\n\n
    getModel()\n
    '''
def objectivesIterator():
    '''returns Iterator<IloDecisionObjective>\n\n
    objectivesIterator()\n
    '''
def onRenameRequirement():
    '''returns None\n\n
    onRenameRequirement(final IloRequirement r, final String oldName)\n
    '''
def getPriority():
    '''returns IloPriority\n\n
    getPriority(final IloRequirement req)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final Element elt, final int propIndex)\n
    getProperty(final int index, final boolean inherited)\n
    '''
def registerDecisionVariable():
    '''returns None\n\n
    registerDecisionVariable(final IloDecisionVariable v, final boolean force)\n
    '''
def getDecisionVariable():
    '''returns IloDecisionVariable\n\n
    getDecisionVariable(final String name)\n
    getDecisionVariable(final String name, final boolean searchParent)\n
    getDecisionVariable(final IloCompositeId name)\n
    '''
def internalRemoveVar():
    '''returns None\n\n
    internalRemoveVar(final String name)\n
    '''
def internalPutVar():
    '''returns None\n\n
    internalPutVar(final IloDecisionVariable var)\n
    '''
def getRequirementConnectorImpl():
    '''returns IloRequirementConnectorImpl\n\n
    getRequirementConnectorImpl()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    hasNext()\n
    hasNext()\n
    '''
def next():
    '''returns IloDecisionObjective\n\n
    next()\n
    next()\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    remove()\n
    remove()\n
    '''
def getChildCount():
    '''returns int\n\n
    getChildCount()\n
    '''
def isComposite():
    '''returns boolean\n\n
    isComposite()\n
    '''
def isLeaf():
    '''returns boolean\n\n
    isLeaf()\n
    '''
def getParent():
    '''returns IloRequirementNode\n\n
    getParent()\n
    '''
def getDefaultPriorityManager():
    '''returns IloDefaultPriorityManager\n\n
    getDefaultPriorityManager()\n
    '''
def getIntProperty():
    '''returns int\n\n
    getIntProperty(final int index, final int defaultVal, final boolean inherited)\n
    '''
def getDoubleProperty():
    '''returns double\n\n
    getDoubleProperty(final int index, final double defaultVal, final boolean inherited)\n
    '''
def getBooleanProperty():
    '''returns boolean\n\n
    getBooleanProperty(final int index, final boolean defaultVal, final boolean inherited)\n
    '''
def setIntProperty():
    '''returns None\n\n
    setIntProperty(final int index, final int value)\n
    '''
def setDoubleProperty():
    '''returns None\n\n
    setDoubleProperty(final int index, final double value)\n
    '''
def setBooleanProperty():
    '''returns None\n\n
    setBooleanProperty(final int index, final boolean value)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final int index, final Object value)\n
    '''
def internalNullifyProp():
    '''returns None\n\n
    internalNullifyProp(final int index, final boolean propagate)\n
    '''
def print():
    '''returns IloTabulatedStream\n\n
    print(final IloTabulatedStream stm, final IloPublisher publisher)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getExplanation():
    '''returns IloMessage\n\n
    getExplanation()\n
    '''
def getFormattedExplanation():
    '''returns String\n\n
    getFormattedExplanation(final IloMessageParameterFormatter ctl)\n
    '''
def setExplanation():
    '''returns None\n\n
    setExplanation(final IloMessage message)\n
    setExplanation(final String text)\n
    '''
def getController():
    '''returns IloEngineController\n\n
    getController()\n
    '''
