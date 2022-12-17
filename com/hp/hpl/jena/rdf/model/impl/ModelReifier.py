def ():
    '''returns ModelReifier\n\n
    (final ModelCom model)\n
    '''
def map1():
    '''returns ReifiedStatement\n\n
    map1(final Node node)\n
    '''
def getReificationStyle():
    '''returns ReificationStyle\n\n
    getReificationStyle()\n
    '''
def graphBaseFind():
    '''returns ExtendedIterator<Triple>\n\n
    graphBaseFind(final TripleMatch m)\n
    '''
def getHiddenStatements():
    '''returns Model\n\n
    getHiddenStatements()\n
    '''
def createReifiedStatement():
    '''returns ReifiedStatement\n\n
    createReifiedStatement(final Statement s)\n
    createReifiedStatement(final String uri, final Statement s)\n
    '''
def getAnyReifiedStatement():
    '''returns Resource\n\n
    getAnyReifiedStatement(final Statement s)\n
    '''
def isReified():
    '''returns boolean\n\n
    isReified(final FrontsTriple s)\n
    '''
def removeAllReifications():
    '''returns None\n\n
    removeAllReifications(final FrontsTriple s)\n
    '''
def removeReification():
    '''returns None\n\n
    removeReification(final ReifiedStatement rs)\n
    '''
def listReifiedStatements():
    '''returns RSIterator\n\n
    listReifiedStatements()\n
    listReifiedStatements(final FrontsTriple s)\n
    '''
def noteIfReified():
    '''returns None\n\n
    noteIfReified(final RDFNode s, final RDFNode p, final RDFNode o)\n
    '''
