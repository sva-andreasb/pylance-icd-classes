def getHttpClient():
'''public HttpClient getHttpClient()
'''
pass
def getAddress():
'''public Address getAddress()
'''
pass
def isSecure():
'''public boolean isSecure()
'''
pass
def getHostHeader():
'''public Buffer getHostHeader()
'''
pass
def getMaxConnections():
'''public int getMaxConnections()
'''
pass
def setMaxConnections():
'''public void setMaxConnections(final int maxConnections)
'''
pass
def getMaxQueueSize():
'''public int getMaxQueueSize()
'''
pass
def setMaxQueueSize():
'''public void setMaxQueueSize(final int maxQueueSize)
'''
pass
def getConnections():
'''public int getConnections()
'''
pass
def getIdleConnections():
'''public int getIdleConnections()
'''
pass
def addAuthorization():
'''public void addAuthorization(final String pathSpec, final Authentication authorization)
'''
pass
def addCookie():
'''public void addCookie(final HttpCookie cookie)
'''
pass
def reserveConnection():
'''public AbstractHttpConnection reserveConnection(final long timeout)
'''
pass
def getIdleConnection():
'''public AbstractHttpConnection getIdleConnection()
'''
pass
def onConnectionFailed():
'''public void onConnectionFailed(final Throwable throwable)
'''
pass
def onException():
'''public void onException(final Throwable throwable)
'''
pass
def onNewConnection():
'''public void onNewConnection(final AbstractHttpConnection connection)
'''
pass
def returnConnection():
'''public void returnConnection(final AbstractHttpConnection connection, final boolean close)
'''
pass
def returnIdleConnection():
'''public void returnIdleConnection(final AbstractHttpConnection connection)
'''
pass
def send():
'''public void send(final HttpExchange ex)
'''
pass
def resend():
'''public void resend(final HttpExchange ex)
'''
pass
def toString():
'''public synchronized String toString()
'''
pass
def toDetailString():
'''public synchronized String toDetailString()
'''
pass
def setProxy():
'''public void setProxy(final Address proxy)
'''
pass
def getProxy():
'''public Address getProxy()
'''
pass
def getProxyAuthentication():
'''public Authentication getProxyAuthentication()
'''
pass
def setProxyAuthentication():
'''public void setProxyAuthentication(final Authentication authentication)
'''
pass
def isProxied():
'''public boolean isProxied()
'''
pass
def close():
'''public void close()
'''
pass
def dump():
'''public String dump()
public void dump(final Appendable out, final String indent)
'''
pass
def ConnectExchange():
'''public ConnectExchange(final Address serverAddress, final SelectConnector.UpgradableEndPoint proxyEndPoint, final HttpExchange exchange)
'''
pass
