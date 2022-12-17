def ():
    '''returns ConnPoolByRoute\n\n
    (final ClientConnectionOperator operator, final ConnPerRoute connPerRoute, final int maxTotalConnections)\n
    (final ClientConnectionOperator operator, final ConnPerRoute connPerRoute, final int maxTotalConnections, final long connTTL, final TimeUnit connTTLTimeUnit)\n
    (final ClientConnectionOperator operator, final HttpParams params)\n
    '''
def getConnectionsInPool():
    '''returns int\n\n
    getConnectionsInPool(final HttpRoute route)\n
    getConnectionsInPool()\n
    '''
def requestPoolEntry():
    '''returns PoolEntryRequest\n\n
    requestPoolEntry(final HttpRoute route, final Object state)\n
    '''
def abortRequest():
    '''returns None\n\n
    abortRequest()\n
    '''
def getPoolEntry():
    '''returns BasicPoolEntry\n\n
    getPoolEntry(final long timeout, final TimeUnit tunit)\n
    '''
def freeEntry():
    '''returns None\n\n
    freeEntry(final BasicPoolEntry entry, final boolean reusable, final long validDuration, final TimeUnit timeUnit)\n
    '''
def deleteClosedConnections():
    '''returns None\n\n
    deleteClosedConnections()\n
    '''
def closeIdleConnections():
    '''returns None\n\n
    closeIdleConnections(final long idletime, final TimeUnit tunit)\n
    '''
def closeExpiredConnections():
    '''returns None\n\n
    closeExpiredConnections()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def setMaxTotalConnections():
    '''returns None\n\n
    setMaxTotalConnections(final int max)\n
    '''
def getMaxTotalConnections():
    '''returns int\n\n
    getMaxTotalConnections()\n
    '''
