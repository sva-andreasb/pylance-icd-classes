def ProxyClient():
    '''public ProxyClient()
    public ProxyClient(final HttpClientParams params)
    '''
def getState():
    '''public synchronized HttpState getState()
    '''
def setState():
    '''public synchronized void setState(final HttpState state)
    '''
def getHostConfiguration():
    '''public synchronized HostConfiguration getHostConfiguration()
    '''
def setHostConfiguration():
    '''public synchronized void setHostConfiguration(final HostConfiguration hostConfiguration)
    '''
def getParams():
    '''public synchronized HttpClientParams getParams()
    public HttpConnectionManagerParams getParams()
    '''
def setParams():
    '''public synchronized void setParams(final HttpClientParams params)
    public void setParams(final HttpConnectionManagerParams params)
    '''
def connect():
    '''public ConnectResponse connect()
    '''
def getConnectMethod():
    '''public ConnectMethod getConnectMethod()
    '''
def getSocket():
    '''public Socket getSocket()
    '''
def closeIdleConnections():
    '''public void closeIdleConnections(final long idleTimeout)
    '''
def getConnection():
    '''public HttpConnection getConnection()
    public HttpConnection getConnection(final HostConfiguration hostConfiguration, final long timeout)
    public HttpConnection getConnection(final HostConfiguration hostConfiguration)
    '''
def setConnectionParams():
    '''public void setConnectionParams(final HttpParams httpParams)
    '''
def getConnectionWithTimeout():
    '''public HttpConnection getConnectionWithTimeout(final HostConfiguration hostConfiguration, final long timeout)
    '''
def releaseConnection():
    '''public void releaseConnection(final HttpConnection conn)
    '''
