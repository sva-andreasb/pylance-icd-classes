def ():
    '''returns SimpleHttpConnectionManager\n\n
    (final boolean alwaysClose)\n
    ()\n
    '''
def getConnection():
    '''returns HttpConnection\n\n
    getConnection(final HostConfiguration hostConfiguration)\n
    getConnection(final HostConfiguration hostConfiguration, final long timeout)\n
    '''
def isConnectionStaleCheckingEnabled():
    '''returns boolean\n\n
    isConnectionStaleCheckingEnabled()\n
    '''
def setConnectionStaleCheckingEnabled():
    '''returns None\n\n
    setConnectionStaleCheckingEnabled(final boolean connectionStaleCheckingEnabled)\n
    '''
def getConnectionWithTimeout():
    '''returns HttpConnection\n\n
    getConnectionWithTimeout(final HostConfiguration hostConfiguration, final long timeout)\n
    '''
def releaseConnection():
    '''returns None\n\n
    releaseConnection(final HttpConnection conn)\n
    '''
def getParams():
    '''returns HttpConnectionManagerParams\n\n
    getParams()\n
    '''
def setParams():
    '''returns None\n\n
    setParams(final HttpConnectionManagerParams params)\n
    '''
def closeIdleConnections():
    '''returns None\n\n
    closeIdleConnections(final long idleTimeout)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
