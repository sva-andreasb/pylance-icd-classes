MISUSE_MESSAGE = "String  \"Invalid use of BasicClientConnManager: connection still allocated.\nMake sure to release the connection before allocating another one.\""
def BasicClientConnectionManager():
    '''    public BasicClientConnectionManager(final SchemeRegistry schreg)
    public BasicClientConnectionManager()
    '''
def getSchemeRegistry():
    '''    public SchemeRegistry getSchemeRegistry()
    '''
def requestConnection():
    '''    public final ClientConnectionRequest requestConnection(final HttpRoute route, final Object state)
    '''
def abortRequest():
    '''    public void abortRequest()
    '''
def getConnection():
    '''    public ManagedClientConnection getConnection(final long timeout, final TimeUnit tunit)
    '''
def releaseConnection():
    '''    public void releaseConnection(final ManagedClientConnection conn, final long keepalive, final TimeUnit tunit)
    '''
def closeExpiredConnections():
    '''    public void closeExpiredConnections()
    '''
def closeIdleConnections():
    '''    public void closeIdleConnections(final long idletime, final TimeUnit tunit)
    '''
def shutdown():
    '''    public void shutdown()
    '''
