def ConnPoolByRoute():
    '''public ConnPoolByRoute(final ClientConnectionOperator operator, final ConnPerRoute connPerRoute, final int maxTotalConnections)
    public ConnPoolByRoute(final ClientConnectionOperator operator, final ConnPerRoute connPerRoute, final int maxTotalConnections, final long connTTL, final TimeUnit connTTLTimeUnit)
    public ConnPoolByRoute(final ClientConnectionOperator operator, final HttpParams params)
    '''
def getConnectionsInPool():
    '''public int getConnectionsInPool(final HttpRoute route)
    public int getConnectionsInPool()
    '''
def requestPoolEntry():
    '''public PoolEntryRequest requestPoolEntry(final HttpRoute route, final Object state)
    '''
def abortRequest():
    '''public void abortRequest()
    '''
def getPoolEntry():
    '''public BasicPoolEntry getPoolEntry(final long timeout, final TimeUnit tunit)
    '''
def freeEntry():
    '''public void freeEntry(final BasicPoolEntry entry, final boolean reusable, final long validDuration, final TimeUnit timeUnit)
    '''
def deleteClosedConnections():
    '''public void deleteClosedConnections()
    '''
def closeIdleConnections():
    '''public void closeIdleConnections(final long idletime, final TimeUnit tunit)
    '''
def closeExpiredConnections():
    '''public void closeExpiredConnections()
    '''
def shutdown():
    '''public void shutdown()
    '''
def setMaxTotalConnections():
    '''public void setMaxTotalConnections(final int max)
    '''
def getMaxTotalConnections():
    '''public int getMaxTotalConnections()
    '''
