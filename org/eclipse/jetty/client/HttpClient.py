CONNECTOR_SOCKET = "int  0"
CONNECTOR_SELECT_CHANNEL = "int  2"
def HttpClient():
'''public HttpClient()
public HttpClient(final SslContextFactory sslContextFactory)
'''
pass
def isConnectBlocking():
'''public boolean isConnectBlocking()
'''
pass
def setConnectBlocking():
'''public void setConnectBlocking(final boolean connectBlocking)
'''
pass
def send():
'''public void send(final HttpExchange exchange)
'''
pass
def getThreadPool():
'''public ThreadPool getThreadPool()
'''
pass
def setThreadPool():
'''public void setThreadPool(final ThreadPool threadPool)
'''
pass
def getAttribute():
'''public Object getAttribute(final String name)
'''
pass
def getAttributeNames():
'''public Enumeration getAttributeNames()
'''
pass
def removeAttribute():
'''public void removeAttribute(final String name)
'''
pass
def setAttribute():
'''public void setAttribute(final String name, final Object attribute)
'''
pass
def clearAttributes():
'''public void clearAttributes()
'''
pass
def getDestination():
'''public HttpDestination getDestination(final Address remote, final boolean ssl)
'''
pass
def schedule():
'''public void schedule(final Timeout.Task task)
public void schedule(final Timeout.Task task, final long timeout)
'''
pass
def scheduleIdle():
'''public void scheduleIdle(final Timeout.Task task)
'''
pass
def cancel():
'''public void cancel(final Timeout.Task task)
'''
pass
def getUseDirectBuffers():
'''public boolean getUseDirectBuffers()
'''
pass
def setRealmResolver():
'''public void setRealmResolver(final RealmResolver resolver)
'''
pass
def getRealmResolver():
'''public RealmResolver getRealmResolver()
'''
pass
def hasRealms():
'''public boolean hasRealms()
'''
pass
def registerListener():
'''public void registerListener(final String listenerClass)
'''
pass
def getRegisteredListeners():
'''public LinkedList<String> getRegisteredListeners()
'''
pass
def setUseDirectBuffers():
'''public void setUseDirectBuffers(final boolean direct)
'''
pass
def getConnectorType():
'''public int getConnectorType()
'''
pass
def setConnectorType():
'''public void setConnectorType(final int connectorType)
'''
pass
def getMaxConnectionsPerAddress():
'''public int getMaxConnectionsPerAddress()
'''
pass
def setMaxConnectionsPerAddress():
'''public void setMaxConnectionsPerAddress(final int maxConnectionsPerAddress)
'''
pass
def getMaxQueueSizePerAddress():
'''public int getMaxQueueSizePerAddress()
'''
pass
def setMaxQueueSizePerAddress():
'''public void setMaxQueueSizePerAddress(final int maxQueueSizePerAddress)
'''
pass
def run():
'''public void run()
'''
pass
def getSslContextFactory():
'''public SslContextFactory getSslContextFactory()
'''
pass
def getIdleTimeout():
'''public long getIdleTimeout()
'''
pass
def setIdleTimeout():
'''public void setIdleTimeout(final long ms)
'''
pass
def getSoTimeout():
'''public int getSoTimeout()
'''
pass
def setSoTimeout():
'''public void setSoTimeout(final int timeout)
'''
pass
def getTimeout():
'''public long getTimeout()
'''
pass
def setTimeout():
'''public void setTimeout(final long timeout)
'''
pass
def getConnectTimeout():
'''public int getConnectTimeout()
'''
pass
def setConnectTimeout():
'''public void setConnectTimeout(final int connectTimeout)
'''
pass
def getProxy():
'''public Address getProxy()
'''
pass
def setProxy():
'''public void setProxy(final Address proxy)
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
def getNoProxy():
'''public Set<String> getNoProxy()
'''
pass
def setNoProxy():
'''public void setNoProxy(final Set<String> noProxyAddresses)
'''
pass
def maxRetries():
'''public int maxRetries()
'''
pass
def setMaxRetries():
'''public void setMaxRetries(final int retries)
'''
pass
def maxRedirects():
'''public int maxRedirects()
'''
pass
def setMaxRedirects():
'''public void setMaxRedirects(final int redirects)
'''
pass
def getRequestBufferSize():
'''public int getRequestBufferSize()
'''
pass
def setRequestBufferSize():
'''public void setRequestBufferSize(final int requestBufferSize)
'''
pass
def getRequestHeaderSize():
'''public int getRequestHeaderSize()
'''
pass
def setRequestHeaderSize():
'''public void setRequestHeaderSize(final int requestHeaderSize)
'''
pass
def getResponseBufferSize():
'''public int getResponseBufferSize()
'''
pass
def setResponseBufferSize():
'''public void setResponseBufferSize(final int responseBufferSize)
'''
pass
def getResponseHeaderSize():
'''public int getResponseHeaderSize()
'''
pass
def setResponseHeaderSize():
'''public void setResponseHeaderSize(final int responseHeaderSize)
'''
pass
def setRequestBuffers():
'''public void setRequestBuffers(final Buffers requestBuffers)
'''
pass
def setResponseBuffers():
'''public void setResponseBuffers(final Buffers responseBuffers)
'''
pass
def getRequestBuffers():
'''public Buffers getRequestBuffers()
'''
pass
def getResponseBuffers():
'''public Buffers getResponseBuffers()
'''
pass
def setMaxBuffers():
'''public void setMaxBuffers(final int maxBuffers)
'''
pass
def getMaxBuffers():
'''public int getMaxBuffers()
'''
pass
def getTrustStoreLocation():
'''public String getTrustStoreLocation()
'''
pass
def setTrustStoreLocation():
'''public void setTrustStoreLocation(final String trustStoreLocation)
'''
pass
def getTrustStoreInputStream():
'''public InputStream getTrustStoreInputStream()
'''
pass
def setTrustStoreInputStream():
'''public void setTrustStoreInputStream(final InputStream trustStoreInputStream)
'''
pass
def getKeyStoreLocation():
'''public String getKeyStoreLocation()
'''
pass
def setKeyStoreLocation():
'''public void setKeyStoreLocation(final String keyStoreLocation)
'''
pass
def getKeyStoreInputStream():
'''public InputStream getKeyStoreInputStream()
'''
pass
def setKeyStoreInputStream():
'''public void setKeyStoreInputStream(final InputStream keyStoreInputStream)
'''
pass
def setKeyStorePassword():
'''public void setKeyStorePassword(final String keyStorePassword)
'''
pass
def setKeyManagerPassword():
'''public void setKeyManagerPassword(final String keyManagerPassword)
'''
pass
def setTrustStorePassword():
'''public void setTrustStorePassword(final String trustStorePassword)
'''
pass
def getKeyStoreType():
'''public String getKeyStoreType()
'''
pass
def setKeyStoreType():
'''public void setKeyStoreType(final String keyStoreType)
'''
pass
def getTrustStoreType():
'''public String getTrustStoreType()
'''
pass
def setTrustStoreType():
'''public void setTrustStoreType(final String trustStoreType)
'''
pass
def getKeyManagerAlgorithm():
'''public String getKeyManagerAlgorithm()
'''
pass
def setKeyManagerAlgorithm():
'''public void setKeyManagerAlgorithm(final String keyManagerAlgorithm)
'''
pass
def getTrustManagerAlgorithm():
'''public String getTrustManagerAlgorithm()
'''
pass
def setTrustManagerAlgorithm():
'''public void setTrustManagerAlgorithm(final String trustManagerAlgorithm)
'''
pass
def getProtocol():
'''public String getProtocol()
'''
pass
def setProtocol():
'''public void setProtocol(final String protocol)
'''
pass
def getProvider():
'''public String getProvider()
'''
pass
def setProvider():
'''public void setProvider(final String provider)
'''
pass
def getSecureRandomAlgorithm():
'''public String getSecureRandomAlgorithm()
'''
pass
def setSecureRandomAlgorithm():
'''public void setSecureRandomAlgorithm(final String secureRandomAlgorithm)
'''
pass
