COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def getExpr():
    '''returns IloNumExpr\n\n
    getExpr()\n
    '''
def getValue():
    '''returns Double\n\n
    getValue()\n
    '''
def getExplanation():
    '''returns IloMessage\n\n
    getExplanation()\n
    '''
def setExplanation():
    '''returns None\n\n
    setExplanation(final IloMessage message)\n
    setExplanation(final String text)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final double value)\n
    '''
def addEpsilon():
    '''returns None\n\n
    addEpsilon(final double value)\n
    '''
def addChild():
    '''returns None\n\n
    addChild(final IloBreakdownVariable variable)\n
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
    '''returns Iterator<IloBreakdownVariable>\n\n
    children()\n
    '''
