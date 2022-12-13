def ConnPoolByRoute():
'''public ConnPoolByRoute(final ClientConnectionOperator operator, final ConnPerRoute connPerRoute, final int maxTotalConnections)
public ConnPoolByRoute(final ClientConnectionOperator operator, final ConnPerRoute connPerRoute, final int maxTotalConnections, final long connTTL, final TimeUnit connTTLTimeUnit)
public ConnPoolByRoute(final ClientConnectionOperator operator, final HttpParams params)
'''
pass
def getConnectionsInPool():
'''public int getConnectionsInPool(final HttpRoute route)
public int getConnectionsInPool()
'''
pass
def requestPoolEntry():
'''public PoolEntryRequest requestPoolEntry(final HttpRoute route, final Object state)
'''
pass
def abortRequest():
'''public void abortRequest()
'''
pass
def getPoolEntry():
'''public BasicPoolEntry getPoolEntry(final long timeout, final TimeUnit tunit)
'''
pass
def freeEntry():
'''public void freeEntry(final BasicPoolEntry entry, final boolean reusable, final long validDuration, final TimeUnit timeUnit)
'''
pass
def deleteClosedConnections():
'''public void deleteClosedConnections()
'''
pass
def closeIdleConnections():
'''public void closeIdleConnections(final long idletime, final TimeUnit tunit)
'''
pass
def closeExpiredConnections():
'''public void closeExpiredConnections()
'''
pass
def shutdown():
'''public void shutdown()
'''
pass
def setMaxTotalConnections():
'''public void setMaxTotalConnections(final int max)
'''
pass
def getMaxTotalConnections():
'''public int getMaxTotalConnections()
'''
pass
