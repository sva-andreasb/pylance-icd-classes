COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloBreakdownVariableImpl\n\n
    (final String name, final Object explanation, final double value)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getParent():
    '''returns IloBreakdownVariable\n\n
    getParent()\n
    '''
def getIdentifier():
    '''returns IloCompositeId\n\n
    getIdentifier()\n
    '''
def getValue():
    '''returns Double\n\n
    getValue()\n
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
def getFormattedExplanation():
    '''returns String\n\n
    getFormattedExplanation(final IloMessageParameterFormatter parameter)\n
    '''
def addChild():
    '''returns None\n\n
    addChild(final IloBreakdownVariable v)\n
    '''
def getChild():
    '''returns IloBreakdownVariable\n\n
    getChild(final String key)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def compare():
    '''returns int\n\n
    compare(final IloBreakdownVariable var1, final IloBreakdownVariable var2)\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final IloBreakdownVariable parent)\n
    '''
