def ():
    '''returns ProxyClient\n\n
    ()\n
    (final HttpClientParams params)\n
    '''
def connect():
    '''returns ConnectResponse\n\n
    connect()\n
    '''
def getConnectMethod():
    '''returns ConnectMethod\n\n
    getConnectMethod()\n
    '''
def getSocket():
    '''returns Socket\n\n
    getSocket()\n
    '''
def closeIdleConnections():
    '''returns None\n\n
    closeIdleConnections(final long idleTimeout)\n
    '''
def getConnection():
    '''returns HttpConnection\n\n
    getConnection()\n
    getConnection(final HostConfiguration hostConfiguration, final long timeout)\n
    getConnection(final HostConfiguration hostConfiguration)\n
    '''
def setConnectionParams():
    '''returns None\n\n
    setConnectionParams(final HttpParams httpParams)\n
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
