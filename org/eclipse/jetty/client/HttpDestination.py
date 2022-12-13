def getHttpClient():
    '''public HttpClient getHttpClient()
    '''
def getAddress():
    '''public Address getAddress()
    '''
def isSecure():
    '''public boolean isSecure()
    '''
def getHostHeader():
    '''public Buffer getHostHeader()
    '''
def getMaxConnections():
    '''public int getMaxConnections()
    '''
def setMaxConnections():
    '''public void setMaxConnections(final int maxConnections)
    '''
def getMaxQueueSize():
    '''public int getMaxQueueSize()
    '''
def setMaxQueueSize():
    '''public void setMaxQueueSize(final int maxQueueSize)
    '''
def getConnections():
    '''public int getConnections()
    '''
def getIdleConnections():
    '''public int getIdleConnections()
    '''
def addAuthorization():
    '''public void addAuthorization(final String pathSpec, final Authentication authorization)
    '''
def addCookie():
    '''public void addCookie(final HttpCookie cookie)
    '''
def reserveConnection():
    '''public AbstractHttpConnection reserveConnection(final long timeout)
    '''
def getIdleConnection():
    '''public AbstractHttpConnection getIdleConnection()
    '''
def onConnectionFailed():
    '''public void onConnectionFailed(final Throwable throwable)
    '''
def onException():
    '''public void onException(final Throwable throwable)
    '''
def onNewConnection():
    '''public void onNewConnection(final AbstractHttpConnection connection)
    '''
def returnConnection():
    '''public void returnConnection(final AbstractHttpConnection connection, final boolean close)
    '''
def returnIdleConnection():
    '''public void returnIdleConnection(final AbstractHttpConnection connection)
    '''
def send():
    '''public void send(final HttpExchange ex)
    '''
def resend():
    '''public void resend(final HttpExchange ex)
    '''
def toString():
    '''public synchronized String toString()
    '''
def toDetailString():
    '''public synchronized String toDetailString()
    '''
def setProxy():
    '''public void setProxy(final Address proxy)
    '''
def getProxy():
    '''public Address getProxy()
    '''
def getProxyAuthentication():
    '''public Authentication getProxyAuthentication()
    '''
def setProxyAuthentication():
    '''public void setProxyAuthentication(final Authentication authentication)
    '''
def isProxied():
    '''public boolean isProxied()
    '''
def close():
    '''public void close()
    '''
def dump():
    '''public String dump()
    public void dump(final Appendable out, final String indent)
    '''
def ConnectExchange():
    '''public ConnectExchange(final Address serverAddress, final SelectConnector.UpgradableEndPoint proxyEndPoint, final HttpExchange exchange)
    '''
