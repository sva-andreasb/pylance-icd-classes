MISUSE_MESSAGE = "String  Invalid use of SingleClientConnManager: connection still allocated.\nMake sure to release the connection before allocating another one.""
def SingleClientConnManager():
'''public SingleClientConnManager(final HttpParams params, final SchemeRegistry schreg)
public SingleClientConnManager(final SchemeRegistry schreg)
public SingleClientConnManager()
'''
pass
def getSchemeRegistry():
'''public SchemeRegistry getSchemeRegistry()
'''
pass
def requestConnection():
'''public final ClientConnectionRequest requestConnection(final HttpRoute route, final Object state)
'''
pass
def abortRequest():
'''public void abortRequest()
'''
pass
def getConnection():
'''public ManagedClientConnection getConnection(final long timeout, final TimeUnit tunit)
public ManagedClientConnection getConnection(final HttpRoute route, final Object state)
'''
pass
def releaseConnection():
'''public void releaseConnection(final ManagedClientConnection conn, final long validDuration, final TimeUnit timeUnit)
'''
pass
def closeExpiredConnections():
'''public void closeExpiredConnections()
'''
pass
def closeIdleConnections():
'''public void closeIdleConnections(final long idletime, final TimeUnit tunit)
'''
pass
def shutdown():
'''public void shutdown()
'''
pass
