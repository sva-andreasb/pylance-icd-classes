def PoolingClientConnectionManager():
    '''public PoolingClientConnectionManager(final SchemeRegistry schreg)
    public PoolingClientConnectionManager(final SchemeRegistry schreg, final DnsResolver dnsResolver)
    public PoolingClientConnectionManager()
    public PoolingClientConnectionManager(final SchemeRegistry schemeRegistry, final long timeToLive, final TimeUnit tunit)
    public PoolingClientConnectionManager(final SchemeRegistry schemeRegistry, final long timeToLive, final TimeUnit tunit, final DnsResolver dnsResolver)
    '''
def getSchemeRegistry():
    '''public SchemeRegistry getSchemeRegistry()
    '''
def requestConnection():
    '''public ClientConnectionRequest requestConnection(final HttpRoute route, final Object state)
    '''
def abortRequest():
    '''public void abortRequest()
    '''
def getConnection():
    '''public ManagedClientConnection getConnection(final long timeout, final TimeUnit tunit)
    '''
def releaseConnection():
    '''public void releaseConnection(final ManagedClientConnection conn, final long keepalive, final TimeUnit tunit)
    '''
def shutdown():
    '''public void shutdown()
    '''
def closeIdleConnections():
    '''public void closeIdleConnections(final long idleTimeout, final TimeUnit tunit)
    '''
def closeExpiredConnections():
    '''public void closeExpiredConnections()
    '''
def getMaxTotal():
    '''public int getMaxTotal()
    '''
def setMaxTotal():
    '''public void setMaxTotal(final int max)
    '''
def getDefaultMaxPerRoute():
    '''public int getDefaultMaxPerRoute()
    '''
def setDefaultMaxPerRoute():
    '''public void setDefaultMaxPerRoute(final int max)
    '''
def getMaxPerRoute():
    '''public int getMaxPerRoute(final HttpRoute route)
    '''
def setMaxPerRoute():
    '''public void setMaxPerRoute(final HttpRoute route, final int max)
    '''
def getTotalStats():
    '''public PoolStats getTotalStats()
    '''
def getStats():
    '''public PoolStats getStats(final HttpRoute route)
    '''
