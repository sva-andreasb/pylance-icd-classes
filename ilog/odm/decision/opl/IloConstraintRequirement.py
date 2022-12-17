COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloConstraintRequirement\n\n
    (final IloConstraint range, final Object explanation, final IloCplexReqPropsDef props)\n
    (final String id, final IloConstraint range, final Object explanation, final IloCplexReqPropsDef props)\n
    (final String id, final IloConstraint range, final Object explanation, final Object relaxation, final IloCplexReqPropsDef props)\n
    '''
def onSetController():
    '''returns None\n\n
    onSetController(final IloEngineController ctl)\n
    '''
def addRangeInList():
    '''returns None\n\n
    addRangeInList(final ArrayList<IloConstraint> list)\n
    '''
def changeRangesPriority():
    '''returns None\n\n
    changeRangesPriority(final IloCplexController ctl)\n
    '''
def postToCplex():
    '''returns None\n\n
    postToCplex(final IloCplexController ctl, final boolean arg1)\n
    '''
def removeFromCplex():
    '''returns None\n\n
    removeFromCplex(final IloCplexController ctl, final boolean arg1)\n
    '''
def getChildCount():
    '''returns int\n\n
    getChildCount()\n
    '''
def getParent():
    '''returns IloRequirementNode\n\n
    getParent()\n
    '''
def isLeaf():
    '''returns boolean\n\n
    isLeaf()\n
    '''
