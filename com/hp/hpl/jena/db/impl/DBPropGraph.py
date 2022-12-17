def ():
    '''returns DBPropGraph\n\n
    (final SpecializedGraph g, final String symbolicName, final String type)\n
    (final SpecializedGraph g, final Node n)\n
    (final SpecializedGraph g, final String newSymbolicName, final Graph oldProperties)\n
    '''
def begin():
    '''returns boolean\n\n
    begin()\n
    '''
def conditionalCommit():
    '''returns None\n\n
    conditionalCommit(final boolean commit)\n
    '''
def addLSet():
    '''returns None\n\n
    addLSet(final DBPropLSet lset)\n
    '''
def addPrefix():
    '''returns None\n\n
    addPrefix(final String prefix, final String uri)\n
    '''
def bnodeForPrefix():
    '''returns Node\n\n
    bnodeForPrefix(final Node prefixNode)\n
    '''
def removePrefix():
    '''returns None\n\n
    removePrefix(final String prefix)\n
    '''
def addGraphId():
    '''returns None\n\n
    addGraphId(final int id)\n
    '''
def addStmtTable():
    '''returns None\n\n
    addStmtTable(final String table)\n
    '''
def addReifTable():
    '''returns None\n\n
    addReifTable(final String table)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
def getStmtTable():
    '''returns String\n\n
    getStmtTable()\n
    '''
def getReifTable():
    '''returns String\n\n
    getReifTable()\n
    '''
def getGraphId():
    '''returns int\n\n
    getGraphId()\n
    '''
def getAllLSets():
    '''returns ExtendedIterator<DBPropLSet>\n\n
    getAllLSets()\n
    '''
def getAllPrefixes():
    '''returns ExtendedIterator<DBPropPrefix>\n\n
    getAllPrefixes()\n
    '''
def listTriples():
    '''returns ExtendedIterator<Triple>\n\n
    listTriples()\n
    '''
def isDBPropGraphOk():
    '''returns boolean\n\n
    isDBPropGraphOk(final String name)\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def map1():
    '''returns DBPropPrefix\n\n
    map1(final Triple t)\n
    map1(final Triple t)\n
    '''
