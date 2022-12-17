def ():
    '''returns PredicatesFilter\n\n
    (final Resource node)\n
    ()\n
    ()\n
    (final Path basePath)\n
    (final Collection<Property> preds)\n
    (final Property[] preds)\n
    (final Property pred)\n
    '''
def getNode():
    '''returns Resource\n\n
    getNode()\n
    '''
def getParent():
    '''returns DisjointSet\n\n
    getParent()\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final DisjointSet parent)\n
    '''
def getRank():
    '''returns int\n\n
    getRank()\n
    '''
def incrementRank():
    '''returns None\n\n
    incrementRank()\n
    '''
def getAncestor():
    '''returns DisjointSet\n\n
    getAncestor()\n
    '''
def setAncestor():
    '''returns None\n\n
    setAncestor(final DisjointSet anc)\n
    '''
def setBlack():
    '''returns None\n\n
    setBlack()\n
    '''
def isBlack():
    '''returns boolean\n\n
    isBlack()\n
    '''
def used():
    '''returns boolean\n\n
    used()\n
    '''
def setUsed():
    '''returns None\n\n
    setUsed()\n
    '''
def find():
    '''returns DisjointSet\n\n
    find()\n
    '''
def union():
    '''returns None\n\n
    union(final DisjointSet y)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def toShortString():
    '''returns String\n\n
    toShortString()\n
    '''
def getLCA():
    '''returns Resource\n\n
    getLCA(final Resource u, final Resource v)\n
    '''
def setLCA():
    '''returns None\n\n
    setLCA(final Resource u, final Resource v, final Resource lca)\n
    '''
def getSet():
    '''returns DisjointSet\n\n
    getSet(final Resource r)\n
    '''
def getStatement():
    '''returns Statement\n\n
    getStatement(final int i)\n
    '''
def append():
    '''returns Path\n\n
    append(final Statement s)\n
    '''
def hasTerminus():
    '''returns boolean\n\n
    hasTerminus(final RDFNode n)\n
    '''
def getTerminal():
    '''returns RDFNode\n\n
    getTerminal()\n
    '''
def getTerminalResource():
    '''returns Resource\n\n
    getTerminalResource()\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final Statement s)\n
    '''
