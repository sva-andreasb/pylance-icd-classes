COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def getProperty():
    '''returns Object\n\n
    getProperty(final int index, final boolean inherited)\n
    '''
def setPriorityForBranch():
    '''returns None\n\n
    setPriorityForBranch(final IloPriority priority)\n
    '''
def onSetController():
    '''returns None\n\n
    onSetController(final IloEngineController ctl)\n
    '''
def registerRequirement():
    '''returns None\n\n
    registerRequirement(final IloRequirement req, final boolean force)\n
    '''
def unregisterRequirement():
    '''returns IloRequirement\n\n
    unregisterRequirement(final String name)\n
    '''
def internalPutReq():
    '''returns None\n\n
    internalPutReq(final IloRequirement r)\n
    '''
def onRenameRequirement():
    '''returns None\n\n
    onRenameRequirement(final IloRequirement r, final String oldName)\n
    '''
def internalRemoveReq():
    '''returns IloRequirement\n\n
    internalRemoveReq(final String name)\n
    '''
def getRequirement():
    '''returns IloRequirement\n\n
    getRequirement(final String id)\n
    '''
def getModel():
    '''returns IloDecisionModel\n\n
    getModel()\n
    '''
def getReqPropertiesDef():
    '''returns IloReqPropertiesDef\n\n
    getReqPropertiesDef()\n
    '''
def print():
    '''returns IloTabulatedStream\n\n
    print(final IloTabulatedStream stm, final IloPublisher publisher)\n
    '''
def nullifyChildrenProperty():
    '''returns None\n\n
    nullifyChildrenProperty(final int index)\n
    '''
def internalNullifyProp():
    '''returns None\n\n
    internalNullifyProp(final int index, final boolean resetIncluded)\n
    '''
def decrActivePrio():
    '''returns None\n\n
    decrActivePrio()\n
    '''
def incrActivePrio():
    '''returns None\n\n
    incrActivePrio()\n
    '''
def testActivePrio():
    '''returns boolean\n\n
    testActivePrio()\n
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
def getChildCount():
    '''returns int\n\n
    getChildCount()\n
    '''
