def ():
    '''returns ThreadSafeClientConnManager\n\n
    (final SchemeRegistry schreg)\n
    ()\n
    (final SchemeRegistry schreg, final long connTTL, final TimeUnit connTTLTimeUnit)\n
    (final SchemeRegistry schreg, final long connTTL, final TimeUnit connTTLTimeUnit, final ConnPerRouteBean connPerRoute)\n
    (final HttpParams params, final SchemeRegistry schreg)\n
    '''
def getSchemeRegistry():
    '''returns SchemeRegistry\n\n
    getSchemeRegistry()\n
    '''
def requestConnection():
    '''returns ClientConnectionRequest\n\n
    requestConnection(final HttpRoute route, final Object state)\n
    '''
def abortRequest():
    '''returns None\n\n
    abortRequest()\n
    '''
def getConnection():
    '''returns ManagedClientConnection\n\n
    getConnection(final long timeout, final TimeUnit tunit)\n
    '''
def releaseConnection():
    '''returns None\n\n
    releaseConnection(final ManagedClientConnection conn, final long validDuration, final TimeUnit timeUnit)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def getConnectionsInPool():
    '''returns int\n\n
    getConnectionsInPool(final HttpRoute route)\n
    getConnectionsInPool()\n
    '''
def closeIdleConnections():
    '''returns None\n\n
    closeIdleConnections(final long idleTimeout, final TimeUnit tunit)\n
    '''
def closeExpiredConnections():
    '''returns None\n\n
    closeExpiredConnections()\n
    '''
def getMaxTotal():
    '''returns int\n\n
    getMaxTotal()\n
    '''
def setMaxTotal():
    '''returns None\n\n
    setMaxTotal(final int max)\n
    '''
def getDefaultMaxPerRoute():
    '''returns int\n\n
    getDefaultMaxPerRoute()\n
    '''
def setDefaultMaxPerRoute():
    '''returns None\n\n
    setDefaultMaxPerRoute(final int max)\n
    '''
def getMaxForRoute():
    '''returns int\n\n
    getMaxForRoute(final HttpRoute route)\n
    '''
def setMaxForRoute():
    '''returns None\n\n
    setMaxForRoute(final HttpRoute route, final int max)\n
    '''
