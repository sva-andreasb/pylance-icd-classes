MISUSE_MESSAGE = "String  \"Invalid use of BasicClientConnManager: connection still allocated.\nMake sure to release the connection before allocating another one.\""
def ():
    '''returns BasicClientConnectionManager\n\n
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
    '''
def releaseConnection():
    '''returns None\n\n
    releaseConnection(final ManagedClientConnection conn, final long keepalive, final TimeUnit tunit)\n
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
