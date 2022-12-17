COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def publish():
    '''returns None\n\n
    publish(final Object publishable)\n
    '''
def isSilent():
    '''returns boolean\n\n
    isSilent()\n
    '''
def setSilent():
    '''returns None\n\n
    setSilent(final boolean status)\n
    '''
def getEngineReport():
    '''returns IloEngineReport\n\n
    getEngineReport()\n
    '''
def explainAllObjectives():
    '''returns IloExplanation\n\n
    explainAllObjectives(String[] properties)\n
    '''
def explainObjectives():
    '''returns IloExplanation\n\n
    explainObjectives(final IloDecisionObjective[] objectives, String[] properties)\n
    '''
def explainRequirements():
    '''returns IloExplanation\n\n
    explainRequirements(final Iterator<?> reqIt, String[] properties, final int depth, final boolean explainParents)\n
    '''
def getDecisionModel():
    '''returns IloDecisionModel\n\n
    getDecisionModel()\n
    '''
def getFormattedProperty():
    '''returns Serializable\n\n
    getFormattedProperty(final IloDecisionModel.Element elt, final int index, final IloPropertiesDef propDefs)\n
    '''
def interpretInput():
    '''returns Object[]\n\n
    interpretInput(final Object value, final Class<?> requiredType)\n
    interpretInput(final Object[] values, final Class<?>[] requiredTypes)\n
    '''
def objectiveIterator():
    '''returns Iterator<IloDecisionObjective>\n\n
    objectiveIterator()\n
    '''
def formatValue():
    '''returns Serializable\n\n
    formatValue(final Object value)\n
    '''
def formatValues():
    '''returns Serializable[]\n\n
    formatValues(final Object[] values)\n
    '''
def interpretDataAccess():
    '''returns Object\n\n
    interpretDataAccess(final IloDataAccess path, final Class<?> requiredType)\n
    '''
def declareObjectHandle():
    '''returns None\n\n
    declareObjectHandle(final Object o, final IloObjectHandle handle)\n
    '''
def getObject():
    '''returns Object\n\n
    getObject(final IloObjectHandle handle)\n
    '''
def getObjectHandle():
    '''returns IloObjectHandle\n\n
    getObjectHandle(final Object obj)\n
    '''
def undeclareObjectHandle():
    '''returns Object\n\n
    undeclareObjectHandle(final IloObjectHandle handle)\n
    '''
def getCurrentModel():
    '''returns IloDecisionModel\n\n
    getCurrentModel()\n
    '''
def selectSharedScope():
    '''returns None\n\n
    selectSharedScope(final boolean isShared)\n
    '''
def isSharedScope():
    '''returns boolean\n\n
    isSharedScope()\n
    '''
def print():
    '''returns None\n\n
    print(final OutputStream os, final Iterator<?> modelEltIt)\n
    '''
def nextTmplInstId():
    '''returns String\n\n
    nextTmplInstId(final String templateNm)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def getRequirement():
    '''returns IloRequirement\n\n
    getRequirement(final String name)\n
    getRequirement(final String name, final IloCompositeRequirement parent)\n
    '''
def runEngine():
    '''returns boolean\n\n
    runEngine(final int mode, final int explainDepth, final int timeLimitSeconds)\n
    '''
def getRequirementConnector():
    '''returns IloRequirementConnector\n\n
    getRequirementConnector()\n
    '''
def getDefaultPriorityMananger():
    '''returns IloDefaultPriorityManager\n\n
    getDefaultPriorityMananger()\n
    '''
def getMessageEvaluatorManager():
    '''returns IloMessageEvaluatorManager\n\n
    getMessageEvaluatorManager()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    hasNext()\n
    hasNext()\n
    '''
def next():
    '''returns IloRequirement\n\n
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
def ():
    '''returns ReqIterator\n\n
    (final Iterator<?> it, final IloRequirement.Status status)\n
    (final Iterator<?> it, final IloRequirement.Status[] statusArray)\n
    '''
