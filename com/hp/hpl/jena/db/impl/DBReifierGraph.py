def ():
    '''returns DBReifierGraph\n\n
    (final GraphRDB parent, final List<SpecializedGraphReifier> reifiers)\n
    '''
def add():
    '''returns None\n\n
    add(final Triple t)\n
    '''
def delete():
    '''returns None\n\n
    delete(final Triple t)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final Triple t)\n
    contains(final Node s, final Node p, final Node o)\n
    '''
def getStatisticsHandler():
    '''returns GraphStatisticsHandler\n\n
    getStatisticsHandler()\n
    '''
def find():
    '''returns ExtendedIterator<Triple>\n\n
    find(final TripleMatch m)\n
    find(final Node s, final Node p, final Node o)\n
    '''
def getPrefixMapping():
    '''returns PrefixMapping\n\n
    getPrefixMapping()\n
    '''
def getTransactionHandler():
    '''returns TransactionHandler\n\n
    getTransactionHandler()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def getEventManager():
    '''returns GraphEventManager\n\n
    getEventManager()\n
    '''
def dependsOn():
    '''returns boolean\n\n
    dependsOn(final Graph other)\n
    '''
def queryHandler():
    '''returns QueryHandler\n\n
    queryHandler()\n
    '''
def getBulkUpdateHandler():
    '''returns BulkUpdateHandler\n\n
    getBulkUpdateHandler()\n
    '''
def getCapabilities():
    '''returns Capabilities\n\n
    getCapabilities()\n
    '''
def getReifier():
    '''returns Reifier\n\n
    getReifier()\n
    '''
def isIsomorphicWith():
    '''returns boolean\n\n
    isIsomorphicWith(final Graph g)\n
    '''
def capabilities():
    '''returns int\n\n
    capabilities()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
