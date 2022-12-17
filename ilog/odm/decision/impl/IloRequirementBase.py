COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloRequirementBase\n\n
    (final String name, final IloReqPropertiesDef props)\n
    '''
def isComposite():
    '''returns boolean\n\n
    isComposite()\n
    '''
def getContainer():
    '''returns IloRequirementContainer\n\n
    getContainer()\n
    '''
def setRemovedFromEngine():
    '''returns None\n\n
    setRemovedFromEngine(final boolean status)\n
    '''
def isRemovedFromEngine():
    '''returns boolean\n\n
    isRemovedFromEngine()\n
    '''
def getModel():
    '''returns IloDecisionModel\n\n
    getModel()\n
    '''
def getIdentifier():
    '''returns IloRequirementId\n\n
    getIdentifier()\n
    '''
def getPriority():
    '''returns IloPriority\n\n
    getPriority(final boolean inherited)\n
    '''
def getPropertiesDef():
    '''returns IloPropertiesDef\n\n
    getPropertiesDef()\n
    '''
def getReqPropertiesDef():
    '''returns IloReqPropertiesDef\n\n
    getReqPropertiesDef()\n
    '''
def setPriority():
    '''returns None\n\n
    setPriority(final IloPriority priority)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final int index, final Object value)\n
    '''
def onChangeProperty():
    '''returns None\n\n
    onChangeProperty(final int index, final Object oldValue, final IloEngineController ctl)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String newName)\n
    '''
def registerMe():
    '''returns None\n\n
    registerMe(final IloRequirementContainer cont, final boolean force)\n
    '''
def getStatus():
    '''returns Status\n\n
    getStatus()\n
    '''
def unregisterMe():
    '''returns None\n\n
    unregisterMe()\n
    '''
