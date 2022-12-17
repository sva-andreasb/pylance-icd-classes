MISUSE_MESSAGE = "String  \"Invalid use of SingleClientConnManager: connection still allocated.\nMake sure to release the connection before allocating another one.\""
def ():
    '''returns SingleClientConnManager\n\n
    (final HttpParams params, final SchemeRegistry schreg)\n
    (final SchemeRegistry schreg)\n
    ()\n
    '''
def getSchemeRegistry():
    '''returns SchemeRegistry\n\n
    getSchemeRegistry()\n
    '''
def abortRequest():
    '''returns None\n\n
    abortRequest()\n
    '''
def getConnection():
    '''returns ManagedClientConnection\n\n
    getConnection(final long timeout, final TimeUnit tunit)\n
    getConnection(final HttpRoute route, final Object state)\n
    '''
def releaseConnection():
    '''returns None\n\n
    releaseConnection(final ManagedClientConnection conn, final long validDuration, final TimeUnit timeUnit)\n
    '''
def closeExpiredConnections():
    '''returns None\n\n
    closeExpiredConnections()\n
    '''
def closeIdleConnections():
    '''returns None\n\n
    closeIdleConnections(final long idletime, final TimeUnit tunit)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
