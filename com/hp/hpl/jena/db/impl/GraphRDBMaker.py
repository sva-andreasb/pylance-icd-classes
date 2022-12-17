def ():
    '''returns GraphRDBMaker\n\n
    (final IDBConnection c, final ReificationStyle style)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final String x)\n
    '''
def getGraph():
    '''returns Graph\n\n
    getGraph()\n
    '''
def openGraph():
    '''returns Graph\n\n
    openGraph()\n
    openGraph(final String name, final boolean strict)\n
    '''
def createGraph():
    '''returns Graph\n\n
    createGraph()\n
    createGraph(final String name, final boolean strict)\n
    '''
def freshGraphName():
    '''returns String\n\n
    freshGraphName()\n
    '''
def removeGraph():
    '''returns None\n\n
    removeGraph(final String name)\n
    '''
def hasGraph():
    '''returns boolean\n\n
    hasGraph(final String name)\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def listGraphs():
    '''returns ExtendedIterator<String>\n\n
    listGraphs()\n
    '''
