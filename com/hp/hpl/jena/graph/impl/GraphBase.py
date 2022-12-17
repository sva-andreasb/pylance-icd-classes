TOSTRING_TRIPLE_BASE = "int  10"
TOSTRING_TRIPLE_LIMIT = "int  17"
def ():
    '''returns GraphBase\n\n
    ()\n
    (final ReificationStyle style)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def dependsOn():
    '''returns boolean\n\n
    dependsOn(final Graph other)\n
    '''
def queryHandler():
    '''returns QueryHandler\n\n
    queryHandler()\n
    '''
def getStatisticsHandler():
    '''returns GraphStatisticsHandler\n\n
    getStatisticsHandler()\n
    '''
def getEventManager():
    '''returns GraphEventManager\n\n
    getEventManager()\n
    '''
def notifyAdd():
    '''returns None\n\n
    notifyAdd(final Triple t)\n
    '''
def notifyDelete():
    '''returns None\n\n
    notifyDelete(final Triple t)\n
    '''
def getTransactionHandler():
    '''returns TransactionHandler\n\n
    getTransactionHandler()\n
    '''
def getBulkUpdateHandler():
    '''returns BulkUpdateHandler\n\n
    getBulkUpdateHandler()\n
    '''
def getCapabilities():
    '''returns Capabilities\n\n
    getCapabilities()\n
    '''
def getPrefixMapping():
    '''returns PrefixMapping\n\n
    getPrefixMapping()\n
    '''
def add():
    '''returns None\n\n
    add(final Triple t)\n
    '''
def performAdd():
    '''returns None\n\n
    performAdd(final Triple t)\n
    '''
def performDelete():
    '''returns None\n\n
    performDelete(final Triple t)\n
    '''
def forTestingOnly_graphBaseFind():
    '''returns ExtendedIterator<Triple>\n\n
    forTestingOnly_graphBaseFind(final TripleMatch tm)\n
    '''
def getReifier():
    '''returns Reifier\n\n
    getReifier()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def isIsomorphicWith():
    '''returns boolean\n\n
    isIsomorphicWith(final Graph g)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
