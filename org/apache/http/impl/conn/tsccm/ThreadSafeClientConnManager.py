def ThreadSafeClientConnManager():
'''public ThreadSafeClientConnManager(final SchemeRegistry schreg)
public ThreadSafeClientConnManager()
public ThreadSafeClientConnManager(final SchemeRegistry schreg, final long connTTL, final TimeUnit connTTLTimeUnit)
public ThreadSafeClientConnManager(final SchemeRegistry schreg, final long connTTL, final TimeUnit connTTLTimeUnit, final ConnPerRouteBean connPerRoute)
public ThreadSafeClientConnManager(final HttpParams params, final SchemeRegistry schreg)
'''
pass
def getSchemeRegistry():
'''public SchemeRegistry getSchemeRegistry()
'''
pass
def requestConnection():
'''public ClientConnectionRequest requestConnection(final HttpRoute route, final Object state)
'''
pass
def abortRequest():
'''public void abortRequest()
'''
pass
def getConnection():
'''public ManagedClientConnection getConnection(final long timeout, final TimeUnit tunit)
'''
pass
def releaseConnection():
'''public void releaseConnection(final ManagedClientConnection conn, final long validDuration, final TimeUnit timeUnit)
'''
pass
def shutdown():
'''public void shutdown()
'''
pass
def getConnectionsInPool():
'''public int getConnectionsInPool(final HttpRoute route)
public int getConnectionsInPool()
'''
pass
def closeIdleConnections():
'''public void closeIdleConnections(final long idleTimeout, final TimeUnit tunit)
'''
pass
def closeExpiredConnections():
'''public void closeExpiredConnections()
'''
pass
def getMaxTotal():
'''public int getMaxTotal()
'''
pass
def setMaxTotal():
'''public void setMaxTotal(final int max)
'''
pass
def getDefaultMaxPerRoute():
'''public int getDefaultMaxPerRoute()
'''
pass
def setDefaultMaxPerRoute():
'''public void setDefaultMaxPerRoute(final int max)
'''
pass
def getMaxForRoute():
'''public int getMaxForRoute(final HttpRoute route)
'''
pass
def setMaxForRoute():
'''public void setMaxForRoute(final HttpRoute route, final int max)
'''
pass
