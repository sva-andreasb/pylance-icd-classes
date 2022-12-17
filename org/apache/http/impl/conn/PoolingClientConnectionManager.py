def ():
    '''returns PoolingClientConnectionManager\n\n
    (final SchemeRegistry schreg)\n
    (final SchemeRegistry schreg, final DnsResolver dnsResolver)\n
    ()\n
    (final SchemeRegistry schemeRegistry, final long timeToLive, final TimeUnit tunit)\n
    (final SchemeRegistry schemeRegistry, final long timeToLive, final TimeUnit tunit, final DnsResolver dnsResolver)\n
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
    releaseConnection(final ManagedClientConnection conn, final long keepalive, final TimeUnit tunit)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
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
def getMaxPerRoute():
    '''returns int\n\n
    getMaxPerRoute(final HttpRoute route)\n
    '''
def setMaxPerRoute():
    '''returns None\n\n
    setMaxPerRoute(final HttpRoute route, final int max)\n
    '''
def getTotalStats():
    '''returns PoolStats\n\n
    getTotalStats()\n
    '''
def getStats():
    '''returns PoolStats\n\n
    getStats(final HttpRoute route)\n
    '''
