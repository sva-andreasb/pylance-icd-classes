def SimpleHttpConnectionManager():
    '''public SimpleHttpConnectionManager(final boolean alwaysClose)
    public SimpleHttpConnectionManager()
    '''
def getConnection():
    '''public HttpConnection getConnection(final HostConfiguration hostConfiguration)
    public HttpConnection getConnection(final HostConfiguration hostConfiguration, final long timeout)
    '''
def isConnectionStaleCheckingEnabled():
    '''public boolean isConnectionStaleCheckingEnabled()
    '''
def setConnectionStaleCheckingEnabled():
    '''public void setConnectionStaleCheckingEnabled(final boolean connectionStaleCheckingEnabled)
    '''
def getConnectionWithTimeout():
    '''public HttpConnection getConnectionWithTimeout(final HostConfiguration hostConfiguration, final long timeout)
    '''
def releaseConnection():
    '''public void releaseConnection(final HttpConnection conn)
    '''
def getParams():
    '''public HttpConnectionManagerParams getParams()
    '''
def setParams():
    '''public void setParams(final HttpConnectionManagerParams params)
    '''
def closeIdleConnections():
    '''public void closeIdleConnections(final long idleTimeout)
    '''
def shutdown():
    '''public void shutdown()
    '''
