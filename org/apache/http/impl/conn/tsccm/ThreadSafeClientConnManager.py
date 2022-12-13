def ThreadSafeClientConnManager():
    '''    public ThreadSafeClientConnManager(final SchemeRegistry schreg)
    public ThreadSafeClientConnManager()
    public ThreadSafeClientConnManager(final SchemeRegistry schreg, final long connTTL, final TimeUnit connTTLTimeUnit)
    public ThreadSafeClientConnManager(final SchemeRegistry schreg, final long connTTL, final TimeUnit connTTLTimeUnit, final ConnPerRouteBean connPerRoute)
    public ThreadSafeClientConnManager(final HttpParams params, final SchemeRegistry schreg)
    '''
def getSchemeRegistry():
    '''    public SchemeRegistry getSchemeRegistry()
    '''
def requestConnection():
    '''    public ClientConnectionRequest requestConnection(final HttpRoute route, final Object state)
    '''
def abortRequest():
    '''    public void abortRequest()
    '''
def getConnection():
    '''    public ManagedClientConnection getConnection(final long timeout, final TimeUnit tunit)
    '''
def releaseConnection():
    '''    public void releaseConnection(final ManagedClientConnection conn, final long validDuration, final TimeUnit timeUnit)
    '''
def shutdown():
    '''    public void shutdown()
    '''
def getConnectionsInPool():
    '''    public int getConnectionsInPool(final HttpRoute route)
    public int getConnectionsInPool()
    '''
def closeIdleConnections():
    '''    public void closeIdleConnections(final long idleTimeout, final TimeUnit tunit)
    '''
def closeExpiredConnections():
    '''    public void closeExpiredConnections()
    '''
def getMaxTotal():
    '''    public int getMaxTotal()
    '''
def setMaxTotal():
    '''    public void setMaxTotal(final int max)
    '''
def getDefaultMaxPerRoute():
    '''    public int getDefaultMaxPerRoute()
    '''
def setDefaultMaxPerRoute():
    '''    public void setDefaultMaxPerRoute(final int max)
    '''
def getMaxForRoute():
    '''    public int getMaxForRoute(final HttpRoute route)
    '''
def setMaxForRoute():
    '''    public void setMaxForRoute(final HttpRoute route, final int max)
    '''
