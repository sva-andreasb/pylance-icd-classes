CONNECTOR_SOCKET = "int  0"
CONNECTOR_SELECT_CHANNEL = "int  2"
def ():
    '''returns HttpClient\n\n
    ()\n
    (final SslContextFactory sslContextFactory)\n
    '''
def isConnectBlocking():
    '''returns boolean\n\n
    isConnectBlocking()\n
    '''
def setConnectBlocking():
    '''returns None\n\n
    setConnectBlocking(final boolean connectBlocking)\n
    '''
def send():
    '''returns None\n\n
    send(final HttpExchange exchange)\n
    '''
def getThreadPool():
    '''returns ThreadPool\n\n
    getThreadPool()\n
    '''
def setThreadPool():
    '''returns None\n\n
    setThreadPool(final ThreadPool threadPool)\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final String name)\n
    '''
def getAttributeNames():
    '''returns Enumeration\n\n
    getAttributeNames()\n
    '''
def removeAttribute():
    '''returns None\n\n
    removeAttribute(final String name)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final String name, final Object attribute)\n
    '''
def clearAttributes():
    '''returns None\n\n
    clearAttributes()\n
    '''
def getDestination():
    '''returns HttpDestination\n\n
    getDestination(final Address remote, final boolean ssl)\n
    '''
def schedule():
    '''returns None\n\n
    schedule(final Timeout.Task task)\n
    schedule(final Timeout.Task task, final long timeout)\n
    '''
def scheduleIdle():
    '''returns None\n\n
    scheduleIdle(final Timeout.Task task)\n
    '''
def cancel():
    '''returns None\n\n
    cancel(final Timeout.Task task)\n
    '''
def getUseDirectBuffers():
    '''returns boolean\n\n
    getUseDirectBuffers()\n
    '''
def setRealmResolver():
    '''returns None\n\n
    setRealmResolver(final RealmResolver resolver)\n
    '''
def getRealmResolver():
    '''returns RealmResolver\n\n
    getRealmResolver()\n
    '''
def hasRealms():
    '''returns boolean\n\n
    hasRealms()\n
    '''
def registerListener():
    '''returns None\n\n
    registerListener(final String listenerClass)\n
    '''
def getRegisteredListeners():
    '''returns LinkedList<String>\n\n
    getRegisteredListeners()\n
    '''
def setUseDirectBuffers():
    '''returns None\n\n
    setUseDirectBuffers(final boolean direct)\n
    '''
def getConnectorType():
    '''returns int\n\n
    getConnectorType()\n
    '''
def setConnectorType():
    '''returns None\n\n
    setConnectorType(final int connectorType)\n
    '''
def getMaxConnectionsPerAddress():
    '''returns int\n\n
    getMaxConnectionsPerAddress()\n
    '''
def setMaxConnectionsPerAddress():
    '''returns None\n\n
    setMaxConnectionsPerAddress(final int maxConnectionsPerAddress)\n
    '''
def getMaxQueueSizePerAddress():
    '''returns int\n\n
    getMaxQueueSizePerAddress()\n
    '''
def setMaxQueueSizePerAddress():
    '''returns None\n\n
    setMaxQueueSizePerAddress(final int maxQueueSizePerAddress)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def getSslContextFactory():
    '''returns SslContextFactory\n\n
    getSslContextFactory()\n
    '''
def getIdleTimeout():
    '''returns long\n\n
    getIdleTimeout()\n
    '''
def setIdleTimeout():
    '''returns None\n\n
    setIdleTimeout(final long ms)\n
    '''
def getSoTimeout():
    '''returns int\n\n
    getSoTimeout()\n
    '''
def setSoTimeout():
    '''returns None\n\n
    setSoTimeout(final int timeout)\n
    '''
def getTimeout():
    '''returns long\n\n
    getTimeout()\n
    '''
def setTimeout():
    '''returns None\n\n
    setTimeout(final long timeout)\n
    '''
def getConnectTimeout():
    '''returns int\n\n
    getConnectTimeout()\n
    '''
def setConnectTimeout():
    '''returns None\n\n
    setConnectTimeout(final int connectTimeout)\n
    '''
def getProxy():
    '''returns Address\n\n
    getProxy()\n
    '''
def setProxy():
    '''returns None\n\n
    setProxy(final Address proxy)\n
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
def getNoProxy():
    '''returns Set<String>\n\n
    getNoProxy()\n
    '''
def setNoProxy():
    '''returns None\n\n
    setNoProxy(final Set<String> noProxyAddresses)\n
    '''
def maxRetries():
    '''returns int\n\n
    maxRetries()\n
    '''
def setMaxRetries():
    '''returns None\n\n
    setMaxRetries(final int retries)\n
    '''
def maxRedirects():
    '''returns int\n\n
    maxRedirects()\n
    '''
def setMaxRedirects():
    '''returns None\n\n
    setMaxRedirects(final int redirects)\n
    '''
def getRequestBufferSize():
    '''returns int\n\n
    getRequestBufferSize()\n
    '''
def setRequestBufferSize():
    '''returns None\n\n
    setRequestBufferSize(final int requestBufferSize)\n
    '''
def getRequestHeaderSize():
    '''returns int\n\n
    getRequestHeaderSize()\n
    '''
def setRequestHeaderSize():
    '''returns None\n\n
    setRequestHeaderSize(final int requestHeaderSize)\n
    '''
def getResponseBufferSize():
    '''returns int\n\n
    getResponseBufferSize()\n
    '''
def setResponseBufferSize():
    '''returns None\n\n
    setResponseBufferSize(final int responseBufferSize)\n
    '''
def getResponseHeaderSize():
    '''returns int\n\n
    getResponseHeaderSize()\n
    '''
def setResponseHeaderSize():
    '''returns None\n\n
    setResponseHeaderSize(final int responseHeaderSize)\n
    '''
def setRequestBuffers():
    '''returns None\n\n
    setRequestBuffers(final Buffers requestBuffers)\n
    '''
def setResponseBuffers():
    '''returns None\n\n
    setResponseBuffers(final Buffers responseBuffers)\n
    '''
def getRequestBuffers():
    '''returns Buffers\n\n
    getRequestBuffers()\n
    '''
def getResponseBuffers():
    '''returns Buffers\n\n
    getResponseBuffers()\n
    '''
def setMaxBuffers():
    '''returns None\n\n
    setMaxBuffers(final int maxBuffers)\n
    '''
def getMaxBuffers():
    '''returns int\n\n
    getMaxBuffers()\n
    '''
def getTrustStoreLocation():
    '''returns String\n\n
    getTrustStoreLocation()\n
    '''
def setTrustStoreLocation():
    '''returns None\n\n
    setTrustStoreLocation(final String trustStoreLocation)\n
    '''
def getTrustStoreInputStream():
    '''returns InputStream\n\n
    getTrustStoreInputStream()\n
    '''
def setTrustStoreInputStream():
    '''returns None\n\n
    setTrustStoreInputStream(final InputStream trustStoreInputStream)\n
    '''
def getKeyStoreLocation():
    '''returns String\n\n
    getKeyStoreLocation()\n
    '''
def setKeyStoreLocation():
    '''returns None\n\n
    setKeyStoreLocation(final String keyStoreLocation)\n
    '''
def getKeyStoreInputStream():
    '''returns InputStream\n\n
    getKeyStoreInputStream()\n
    '''
def setKeyStoreInputStream():
    '''returns None\n\n
    setKeyStoreInputStream(final InputStream keyStoreInputStream)\n
    '''
def setKeyStorePassword():
    '''returns None\n\n
    setKeyStorePassword(final String keyStorePassword)\n
    '''
def setKeyManagerPassword():
    '''returns None\n\n
    setKeyManagerPassword(final String keyManagerPassword)\n
    '''
def setTrustStorePassword():
    '''returns None\n\n
    setTrustStorePassword(final String trustStorePassword)\n
    '''
def getKeyStoreType():
    '''returns String\n\n
    getKeyStoreType()\n
    '''
def setKeyStoreType():
    '''returns None\n\n
    setKeyStoreType(final String keyStoreType)\n
    '''
def getTrustStoreType():
    '''returns String\n\n
    getTrustStoreType()\n
    '''
def setTrustStoreType():
    '''returns None\n\n
    setTrustStoreType(final String trustStoreType)\n
    '''
def getKeyManagerAlgorithm():
    '''returns String\n\n
    getKeyManagerAlgorithm()\n
    '''
def setKeyManagerAlgorithm():
    '''returns None\n\n
    setKeyManagerAlgorithm(final String keyManagerAlgorithm)\n
    '''
def getTrustManagerAlgorithm():
    '''returns String\n\n
    getTrustManagerAlgorithm()\n
    '''
def setTrustManagerAlgorithm():
    '''returns None\n\n
    setTrustManagerAlgorithm(final String trustManagerAlgorithm)\n
    '''
def getProtocol():
    '''returns String\n\n
    getProtocol()\n
    '''
def setProtocol():
    '''returns None\n\n
    setProtocol(final String protocol)\n
    '''
def getProvider():
    '''returns String\n\n
    getProvider()\n
    '''
def setProvider():
    '''returns None\n\n
    setProvider(final String provider)\n
    '''
def getSecureRandomAlgorithm():
    '''returns String\n\n
    getSecureRandomAlgorithm()\n
    '''
def setSecureRandomAlgorithm():
    '''returns None\n\n
    setSecureRandomAlgorithm(final String secureRandomAlgorithm)\n
    '''
