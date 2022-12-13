CONNECTOR_SOCKET = "int  0"
CONNECTOR_SELECT_CHANNEL = "int  2"
def HttpClient():
    '''public HttpClient()
    public HttpClient(final SslContextFactory sslContextFactory)
    '''
def isConnectBlocking():
    '''public boolean isConnectBlocking()
    '''
def setConnectBlocking():
    '''public void setConnectBlocking(final boolean connectBlocking)
    '''
def send():
    '''public void send(final HttpExchange exchange)
    '''
def getThreadPool():
    '''public ThreadPool getThreadPool()
    '''
def setThreadPool():
    '''public void setThreadPool(final ThreadPool threadPool)
    '''
def getAttribute():
    '''public Object getAttribute(final String name)
    '''
def getAttributeNames():
    '''public Enumeration getAttributeNames()
    '''
def removeAttribute():
    '''public void removeAttribute(final String name)
    '''
def setAttribute():
    '''public void setAttribute(final String name, final Object attribute)
    '''
def clearAttributes():
    '''public void clearAttributes()
    '''
def getDestination():
    '''public HttpDestination getDestination(final Address remote, final boolean ssl)
    '''
def schedule():
    '''public void schedule(final Timeout.Task task)
    public void schedule(final Timeout.Task task, final long timeout)
    '''
def scheduleIdle():
    '''public void scheduleIdle(final Timeout.Task task)
    '''
def cancel():
    '''public void cancel(final Timeout.Task task)
    '''
def getUseDirectBuffers():
    '''public boolean getUseDirectBuffers()
    '''
def setRealmResolver():
    '''public void setRealmResolver(final RealmResolver resolver)
    '''
def getRealmResolver():
    '''public RealmResolver getRealmResolver()
    '''
def hasRealms():
    '''public boolean hasRealms()
    '''
def registerListener():
    '''public void registerListener(final String listenerClass)
    '''
def getRegisteredListeners():
    '''public LinkedList<String> getRegisteredListeners()
    '''
def setUseDirectBuffers():
    '''public void setUseDirectBuffers(final boolean direct)
    '''
def getConnectorType():
    '''public int getConnectorType()
    '''
def setConnectorType():
    '''public void setConnectorType(final int connectorType)
    '''
def getMaxConnectionsPerAddress():
    '''public int getMaxConnectionsPerAddress()
    '''
def setMaxConnectionsPerAddress():
    '''public void setMaxConnectionsPerAddress(final int maxConnectionsPerAddress)
    '''
def getMaxQueueSizePerAddress():
    '''public int getMaxQueueSizePerAddress()
    '''
def setMaxQueueSizePerAddress():
    '''public void setMaxQueueSizePerAddress(final int maxQueueSizePerAddress)
    '''
def run():
    '''public void run()
    '''
def getSslContextFactory():
    '''public SslContextFactory getSslContextFactory()
    '''
def getIdleTimeout():
    '''public long getIdleTimeout()
    '''
def setIdleTimeout():
    '''public void setIdleTimeout(final long ms)
    '''
def getSoTimeout():
    '''public int getSoTimeout()
    '''
def setSoTimeout():
    '''public void setSoTimeout(final int timeout)
    '''
def getTimeout():
    '''public long getTimeout()
    '''
def setTimeout():
    '''public void setTimeout(final long timeout)
    '''
def getConnectTimeout():
    '''public int getConnectTimeout()
    '''
def setConnectTimeout():
    '''public void setConnectTimeout(final int connectTimeout)
    '''
def getProxy():
    '''public Address getProxy()
    '''
def setProxy():
    '''public void setProxy(final Address proxy)
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
def getNoProxy():
    '''public Set<String> getNoProxy()
    '''
def setNoProxy():
    '''public void setNoProxy(final Set<String> noProxyAddresses)
    '''
def maxRetries():
    '''public int maxRetries()
    '''
def setMaxRetries():
    '''public void setMaxRetries(final int retries)
    '''
def maxRedirects():
    '''public int maxRedirects()
    '''
def setMaxRedirects():
    '''public void setMaxRedirects(final int redirects)
    '''
def getRequestBufferSize():
    '''public int getRequestBufferSize()
    '''
def setRequestBufferSize():
    '''public void setRequestBufferSize(final int requestBufferSize)
    '''
def getRequestHeaderSize():
    '''public int getRequestHeaderSize()
    '''
def setRequestHeaderSize():
    '''public void setRequestHeaderSize(final int requestHeaderSize)
    '''
def getResponseBufferSize():
    '''public int getResponseBufferSize()
    '''
def setResponseBufferSize():
    '''public void setResponseBufferSize(final int responseBufferSize)
    '''
def getResponseHeaderSize():
    '''public int getResponseHeaderSize()
    '''
def setResponseHeaderSize():
    '''public void setResponseHeaderSize(final int responseHeaderSize)
    '''
def setRequestBuffers():
    '''public void setRequestBuffers(final Buffers requestBuffers)
    '''
def setResponseBuffers():
    '''public void setResponseBuffers(final Buffers responseBuffers)
    '''
def getRequestBuffers():
    '''public Buffers getRequestBuffers()
    '''
def getResponseBuffers():
    '''public Buffers getResponseBuffers()
    '''
def setMaxBuffers():
    '''public void setMaxBuffers(final int maxBuffers)
    '''
def getMaxBuffers():
    '''public int getMaxBuffers()
    '''
def getTrustStoreLocation():
    '''public String getTrustStoreLocation()
    '''
def setTrustStoreLocation():
    '''public void setTrustStoreLocation(final String trustStoreLocation)
    '''
def getTrustStoreInputStream():
    '''public InputStream getTrustStoreInputStream()
    '''
def setTrustStoreInputStream():
    '''public void setTrustStoreInputStream(final InputStream trustStoreInputStream)
    '''
def getKeyStoreLocation():
    '''public String getKeyStoreLocation()
    '''
def setKeyStoreLocation():
    '''public void setKeyStoreLocation(final String keyStoreLocation)
    '''
def getKeyStoreInputStream():
    '''public InputStream getKeyStoreInputStream()
    '''
def setKeyStoreInputStream():
    '''public void setKeyStoreInputStream(final InputStream keyStoreInputStream)
    '''
def setKeyStorePassword():
    '''public void setKeyStorePassword(final String keyStorePassword)
    '''
def setKeyManagerPassword():
    '''public void setKeyManagerPassword(final String keyManagerPassword)
    '''
def setTrustStorePassword():
    '''public void setTrustStorePassword(final String trustStorePassword)
    '''
def getKeyStoreType():
    '''public String getKeyStoreType()
    '''
def setKeyStoreType():
    '''public void setKeyStoreType(final String keyStoreType)
    '''
def getTrustStoreType():
    '''public String getTrustStoreType()
    '''
def setTrustStoreType():
    '''public void setTrustStoreType(final String trustStoreType)
    '''
def getKeyManagerAlgorithm():
    '''public String getKeyManagerAlgorithm()
    '''
def setKeyManagerAlgorithm():
    '''public void setKeyManagerAlgorithm(final String keyManagerAlgorithm)
    '''
def getTrustManagerAlgorithm():
    '''public String getTrustManagerAlgorithm()
    '''
def setTrustManagerAlgorithm():
    '''public void setTrustManagerAlgorithm(final String trustManagerAlgorithm)
    '''
def getProtocol():
    '''public String getProtocol()
    '''
def setProtocol():
    '''public void setProtocol(final String protocol)
    '''
def getProvider():
    '''public String getProvider()
    '''
def setProvider():
    '''public void setProvider(final String provider)
    '''
def getSecureRandomAlgorithm():
    '''public String getSecureRandomAlgorithm()
    '''
def setSecureRandomAlgorithm():
    '''public void setSecureRandomAlgorithm(final String secureRandomAlgorithm)
    '''
