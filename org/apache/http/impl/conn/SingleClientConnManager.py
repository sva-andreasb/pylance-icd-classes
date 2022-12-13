MISUSE_MESSAGE = "String  \"Invalid use of SingleClientConnManager: connection still allocated.\nMake sure to release the connection before allocating another one.\""
def SingleClientConnManager():
    '''    public SingleClientConnManager(final HttpParams params, final SchemeRegistry schreg)
    public SingleClientConnManager(final SchemeRegistry schreg)
    public SingleClientConnManager()
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
    public ManagedClientConnection getConnection(final HttpRoute route, final Object state)
    '''
def releaseConnection():
    '''    public void releaseConnection(final ManagedClientConnection conn, final long validDuration, final TimeUnit timeUnit)
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
