def PoolingClientConnectionManager():
'''public PoolingClientConnectionManager(final SchemeRegistry schreg)
public PoolingClientConnectionManager(final SchemeRegistry schreg, final DnsResolver dnsResolver)
public PoolingClientConnectionManager()
public PoolingClientConnectionManager(final SchemeRegistry schemeRegistry, final long timeToLive, final TimeUnit tunit)
public PoolingClientConnectionManager(final SchemeRegistry schemeRegistry, final long timeToLive, final TimeUnit tunit, final DnsResolver dnsResolver)
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
'''public void releaseConnection(final ManagedClientConnection conn, final long keepalive, final TimeUnit tunit)
'''
pass
def shutdown():
'''public void shutdown()
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
def getMaxPerRoute():
'''public int getMaxPerRoute(final HttpRoute route)
'''
pass
def setMaxPerRoute():
'''public void setMaxPerRoute(final HttpRoute route, final int max)
'''
pass
def getTotalStats():
'''public PoolStats getTotalStats()
'''
pass
def getStats():
'''public PoolStats getStats(final HttpRoute route)
'''
pass
