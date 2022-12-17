def getHttpClient():
    '''returns HttpClient\n\n
    getHttpClient()\n
    '''
def getAddress():
    '''returns Address\n\n
    getAddress()\n
    '''
def isSecure():
    '''returns boolean\n\n
    isSecure()\n
    '''
def getHostHeader():
    '''returns Buffer\n\n
    getHostHeader()\n
    '''
def getMaxConnections():
    '''returns int\n\n
    getMaxConnections()\n
    '''
def setMaxConnections():
    '''returns None\n\n
    setMaxConnections(final int maxConnections)\n
    '''
def getMaxQueueSize():
    '''returns int\n\n
    getMaxQueueSize()\n
    '''
def setMaxQueueSize():
    '''returns None\n\n
    setMaxQueueSize(final int maxQueueSize)\n
    '''
def getConnections():
    '''returns int\n\n
    getConnections()\n
    '''
def getIdleConnections():
    '''returns int\n\n
    getIdleConnections()\n
    '''
def addAuthorization():
    '''returns None\n\n
    addAuthorization(final String pathSpec, final Authentication authorization)\n
    '''
def addCookie():
    '''returns None\n\n
    addCookie(final HttpCookie cookie)\n
    '''
def reserveConnection():
    '''returns AbstractHttpConnection\n\n
    reserveConnection(final long timeout)\n
    '''
def getIdleConnection():
    '''returns AbstractHttpConnection\n\n
    getIdleConnection()\n
    '''
def onConnectionFailed():
    '''returns None\n\n
    onConnectionFailed(final Throwable throwable)\n
    '''
def onException():
    '''returns None\n\n
    onException(final Throwable throwable)\n
    '''
def onNewConnection():
    '''returns None\n\n
    onNewConnection(final AbstractHttpConnection connection)\n
    '''
def returnConnection():
    '''returns None\n\n
    returnConnection(final AbstractHttpConnection connection, final boolean close)\n
    '''
def returnIdleConnection():
    '''returns None\n\n
    returnIdleConnection(final AbstractHttpConnection connection)\n
    '''
def send():
    '''returns None\n\n
    send(final HttpExchange ex)\n
    '''
def resend():
    '''returns None\n\n
    resend(final HttpExchange ex)\n
    '''
def setProxy():
    '''returns None\n\n
    setProxy(final Address proxy)\n
    '''
def getProxy():
    '''returns Address\n\n
    getProxy()\n
    '''
def getProxyAuthentication():
    '''returns Authentication\n\n
    getProxyAuthentication()\n
    '''
def setProxyAuthentication():
    '''returns None\n\n
    setProxyAuthentication(final Authentication authentication)\n
    '''
def isProxied():
    '''returns boolean\n\n
    isProxied()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def dump():
    '''returns None\n\n
    dump()\n
    dump(final Appendable out, final String indent)\n
    '''
def ():
    '''returns ConnectExchange\n\n
    (final Address serverAddress, final SelectConnector.UpgradableEndPoint proxyEndPoint, final HttpExchange exchange)\n
    '''
