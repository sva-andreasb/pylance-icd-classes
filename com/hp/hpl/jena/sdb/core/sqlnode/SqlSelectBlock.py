def isSelectBlock():
    '''returns boolean\n\n
    isSelectBlock()\n
    '''
def asSelectBlock():
    '''returns SqlSelectBlock\n\n
    asSelectBlock()\n
    '''
def setBlockAlias():
    '''returns None\n\n
    setBlockAlias(final String alias)\n
    '''
def getCols():
    '''returns List<ColAlias>\n\n
    getCols()\n
    '''
def add():
    '''returns None\n\n
    add(final ColAlias c)\n
    '''
def addAll():
    '''returns None\n\n
    addAll(final Collection<ColAlias> vc)\n
    '''
def clearView():
    '''returns SqlNode\n\n
    clearView()\n
    '''
def getConditions():
    '''returns SqlExprList\n\n
    getConditions()\n
    '''
def hasSlice():
    '''returns boolean\n\n
    hasSlice()\n
    '''
def hasConditions():
    '''returns boolean\n\n
    hasConditions()\n
    '''
def getStart():
    '''returns long\n\n
    getStart()\n
    '''
def getLength():
    '''returns long\n\n
    getLength()\n
    '''
def getIdScope():
    '''returns Scope\n\n
    getIdScope()\n
    '''
def getNodeScope():
    '''returns Scope\n\n
    getNodeScope()\n
    '''
def apply():
    '''returns SqlNode\n\n
    apply(final SqlTransform transform, final SqlNode newSubNode)\n
    '''
def copy():
    '''returns SqlNode\n\n
    copy(final SqlNode subNode)\n
    '''
def visit():
    '''returns None\n\n
    visit(final SqlNodeVisitor visitor)\n
    '''
def getDistinct():
    '''returns boolean\n\n
    getDistinct()\n
    '''
