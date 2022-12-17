COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloMultipleForAllRangesRequirement\n\n
    (final String id, final IloForAllRange[] ranges, final Object explanation, final IloCplexReqPropsDef props)\n
    '''
def onSetController():
    '''returns None\n\n
    onSetController(final IloEngineController ctl)\n
    '''
def getChildCount():
    '''returns int\n\n
    getChildCount()\n
    '''
def isLeaf():
    '''returns boolean\n\n
    isLeaf()\n
    '''
def getParent():
    '''returns IloRequirementNode\n\n
    getParent()\n
    '''
def postToCplex():
    '''returns None\n\n
    postToCplex(final IloCplexController ctl, final boolean propagate)\n
    '''
def removeFromCplex():
    '''returns None\n\n
    removeFromCplex(final IloCplexController ctl, final boolean propagate)\n
    '''
def changeRangesPriority():
    '''returns None\n\n
    changeRangesPriority(final IloCplexController ctl)\n
    '''
def addRange():
    '''returns None\n\n
    addRange(final IloForAllRange range)\n
    '''
def addRangeInList():
    '''returns None\n\n
    addRangeInList(final ArrayList<IloForAllRange> list)\n
    '''
def forallRangeIterator():
    '''returns Iterator<IloForAllRange>\n\n
    forallRangeIterator()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns IloForAllRange\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def isComposite():
    '''returns boolean\n\n
    isComposite()\n
    '''
