COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloCplexEvaluatedDecisionVariable\n\n
    (final String name, final Object explanation, final IloPropertiesDef props, final double value)\n
    '''
def getDecisionVariable():
    '''returns IloDecisionVariable\n\n
    getDecisionVariable(final String name)\n
    getDecisionVariable(final IloCompositeId name)\n
    '''
def getValue():
    '''returns Double\n\n
    getValue()\n
    '''
def internalRemoveVar():
    '''returns None\n\n
    internalRemoveVar(final String var)\n
    '''
def internalPutVar():
    '''returns None\n\n
    internalPutVar(final IloDecisionVariable var)\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns Object\n\n
    next()\n
    '''
def addChild():
    '''returns None\n\n
    addChild(final IloBreakdownVariable bv)\n
    '''
def getContainer():
    '''returns IloDecisionVariableContainer\n\n
    getContainer()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final double value)\n
    '''
def addEpsilon():
    '''returns None\n\n
    addEpsilon(final double value)\n
    '''
def hasChildren():
    '''returns boolean\n\n
    hasChildren()\n
    '''
def getChild():
    '''returns IloBreakdownVariable\n\n
    getChild(final String key)\n
    '''
def children():
    '''returns Iterator<IloDecisionVariable>\n\n
    children()\n
    '''
def compare():
    '''returns int\n\n
    compare(final IloDecisionVariable var1, final IloDecisionVariable var2)\n
    '''
