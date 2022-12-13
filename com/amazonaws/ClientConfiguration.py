DEFAULT_CONNECTION_TIMEOUT = "int  10000"
DEFAULT_SOCKET_TIMEOUT = "int  50000"
DEFAULT_REQUEST_TIMEOUT = "int  0"
DEFAULT_CLIENT_EXECUTION_TIMEOUT = "int  0"
DEFAULT_MAX_CONNECTIONS = "int  50"
DEFAULT_USE_REAPER = "boolean  true"
DEFAULT_USE_GZIP = "boolean  false"
DEFAULT_CONNECTION_TTL = "long  -1L"
DEFAULT_CONNECTION_MAX_IDLE_MILLIS = "long  60000L"
DEFAULT_TCP_KEEP_ALIVE = "boolean  false"
DEFAULT_THROTTLE_RETRIES = "boolean  false"
DEFAULT_RESPONSE_METADATA_CACHE_SIZE = "int  50"
def ClientConfiguration():
    '''    public ClientConfiguration()
    public ClientConfiguration(final ClientConfiguration other)
    '''
def getProtocol():
    '''    public Protocol getProtocol()
    '''
def setProtocol():
    '''    public void setProtocol(final Protocol protocol)
    '''
def withProtocol():
    '''    public ClientConfiguration withProtocol(final Protocol protocol)
    '''
def getMaxConnections():
    '''    public int getMaxConnections()
    '''
def setMaxConnections():
    '''    public void setMaxConnections(final int maxConnections)
    '''
def withMaxConnections():
    '''    public ClientConfiguration withMaxConnections(final int maxConnections)
    '''
def getUserAgent():
    '''    public String getUserAgent()
    '''
def setUserAgent():
    '''    public void setUserAgent(final String userAgent)
    '''
def withUserAgent():
    '''    public ClientConfiguration withUserAgent(final String userAgent)
    '''
def getLocalAddress():
    '''    public InetAddress getLocalAddress()
    '''
def setLocalAddress():
    '''    public void setLocalAddress(final InetAddress localAddress)
    '''
def withLocalAddress():
    '''    public ClientConfiguration withLocalAddress(final InetAddress localAddress)
    '''
def getProxyHost():
    '''    public String getProxyHost()
    '''
def setProxyHost():
    '''    public void setProxyHost(final String proxyHost)
    '''
def withProxyHost():
    '''    public ClientConfiguration withProxyHost(final String proxyHost)
    '''
def getProxyPort():
    '''    public int getProxyPort()
    '''
def setProxyPort():
    '''    public void setProxyPort(final int proxyPort)
    '''
def withProxyPort():
    '''    public ClientConfiguration withProxyPort(final int proxyPort)
    '''
def getProxyUsername():
    '''    public String getProxyUsername()
    '''
def setProxyUsername():
    '''    public void setProxyUsername(final String proxyUsername)
    '''
def withProxyUsername():
    '''    public ClientConfiguration withProxyUsername(final String proxyUsername)
    '''
def getProxyPassword():
    '''    public String getProxyPassword()
    '''
def setProxyPassword():
    '''    public void setProxyPassword(final String proxyPassword)
    '''
def withProxyPassword():
    '''    public ClientConfiguration withProxyPassword(final String proxyPassword)
    '''
def getProxyDomain():
    '''    public String getProxyDomain()
    '''
def setProxyDomain():
    '''    public void setProxyDomain(final String proxyDomain)
    '''
def withProxyDomain():
    '''    public ClientConfiguration withProxyDomain(final String proxyDomain)
    '''
def getProxyWorkstation():
    '''    public String getProxyWorkstation()
    '''
def setProxyWorkstation():
    '''    public void setProxyWorkstation(final String proxyWorkstation)
    '''
def withProxyWorkstation():
    '''    public ClientConfiguration withProxyWorkstation(final String proxyWorkstation)
    '''
def getRetryPolicy():
    '''    public RetryPolicy getRetryPolicy()
    '''
def setRetryPolicy():
    '''    public void setRetryPolicy(final RetryPolicy retryPolicy)
    '''
def withRetryPolicy():
    '''    public ClientConfiguration withRetryPolicy(final RetryPolicy retryPolicy)
    '''
def getMaxErrorRetry():
    '''    public int getMaxErrorRetry()
    '''
def setMaxErrorRetry():
    '''    public void setMaxErrorRetry(final int maxErrorRetry)
    '''
def withMaxErrorRetry():
    '''    public ClientConfiguration withMaxErrorRetry(final int maxErrorRetry)
    '''
def getSocketTimeout():
    '''    public int getSocketTimeout()
    '''
def setSocketTimeout():
    '''    public void setSocketTimeout(final int socketTimeout)
    '''
def withSocketTimeout():
    '''    public ClientConfiguration withSocketTimeout(final int socketTimeout)
    '''
def getConnectionTimeout():
    '''    public int getConnectionTimeout()
    '''
def setConnectionTimeout():
    '''    public void setConnectionTimeout(final int connectionTimeout)
    '''
def withConnectionTimeout():
    '''    public ClientConfiguration withConnectionTimeout(final int connectionTimeout)
    '''
def getRequestTimeout():
    '''    public int getRequestTimeout()
    '''
def setRequestTimeout():
    '''    public void setRequestTimeout(final int requestTimeout)
    '''
def withRequestTimeout():
    '''    public ClientConfiguration withRequestTimeout(final int requestTimeout)
    '''
def getClientExecutionTimeout():
    '''    public int getClientExecutionTimeout()
    '''
def setClientExecutionTimeout():
    '''    public void setClientExecutionTimeout(final int clientExecutionTimeout)
    '''
def withClientExecutionTimeout():
    '''    public ClientConfiguration withClientExecutionTimeout(final int clientExecutionTimeout)
    '''
def useReaper():
    '''    public boolean useReaper()
    '''
def setUseReaper():
    '''    public void setUseReaper(final boolean use)
    '''
def withReaper():
    '''    public ClientConfiguration withReaper(final boolean use)
    '''
def useThrottledRetries():
    '''    public boolean useThrottledRetries()
    '''
def setUseThrottleRetries():
    '''    public void setUseThrottleRetries(final boolean use)
    '''
def withThrottledRetries():
    '''    public ClientConfiguration withThrottledRetries(final boolean use)
    '''
def useGzip():
    '''    public boolean useGzip()
    '''
def setUseGzip():
    '''    public void setUseGzip(final boolean use)
    '''
def withGzip():
    '''    public ClientConfiguration withGzip(final boolean use)
    '''
def getSocketBufferSizeHints():
    '''    public int[] getSocketBufferSizeHints()
    '''
def setSocketBufferSizeHints():
    '''    public void setSocketBufferSizeHints(final int socketSendBufferSizeHint, final int socketReceiveBufferSizeHint)
    '''
def withSocketBufferSizeHints():
    '''    public ClientConfiguration withSocketBufferSizeHints(final int socketSendBufferSizeHint, final int socketReceiveBufferSizeHint)
    '''
def getSignerOverride():
    '''    public String getSignerOverride()
    '''
def setSignerOverride():
    '''    public void setSignerOverride(final String value)
    '''
def withSignerOverride():
    '''    public ClientConfiguration withSignerOverride(final String value)
    '''
def isPreemptiveBasicProxyAuth():
    '''    public boolean isPreemptiveBasicProxyAuth()
    '''
def setPreemptiveBasicProxyAuth():
    '''    public void setPreemptiveBasicProxyAuth(final Boolean preemptiveBasicProxyAuth)
    '''
def withPreemptiveBasicProxyAuth():
    '''    public ClientConfiguration withPreemptiveBasicProxyAuth(final boolean preemptiveBasicProxyAuth)
    '''
def getConnectionTTL():
    '''    public long getConnectionTTL()
    '''
def setConnectionTTL():
    '''    public void setConnectionTTL(final long connectionTTL)
    '''
def withConnectionTTL():
    '''    public ClientConfiguration withConnectionTTL(final long connectionTTL)
    '''
def getConnectionMaxIdleMillis():
    '''    public long getConnectionMaxIdleMillis()
    '''
def setConnectionMaxIdleMillis():
    '''    public void setConnectionMaxIdleMillis(final long connectionMaxIdleMillis)
    '''
def withConnectionMaxIdleMillis():
    '''    public ClientConfiguration withConnectionMaxIdleMillis(final long connectionMaxIdleMillis)
    '''
def useTcpKeepAlive():
    '''    public boolean useTcpKeepAlive()
    '''
def setUseTcpKeepAlive():
    '''    public void setUseTcpKeepAlive(final boolean use)
    '''
def withTcpKeepAlive():
    '''    public ClientConfiguration withTcpKeepAlive(final boolean use)
    '''
def getDnsResolver():
    '''    public DnsResolver getDnsResolver()
    '''
def setDnsResolver():
    '''    public void setDnsResolver(final DnsResolver resolver)
    '''
def withDnsResolver():
    '''    public ClientConfiguration withDnsResolver(final DnsResolver resolver)
    '''
def getResponseMetadataCacheSize():
    '''    public int getResponseMetadataCacheSize()
    '''
def setResponseMetadataCacheSize():
    '''    public void setResponseMetadataCacheSize(final int responseMetadataCacheSize)
    '''
def withResponseMetadataCacheSize():
    '''    public ClientConfiguration withResponseMetadataCacheSize(final int responseMetadataCacheSize)
    '''
def getApacheHttpClientConfig():
    '''    public ApacheHttpClientConfig getApacheHttpClientConfig()
    '''
def getSecureRandom():
    '''    public SecureRandom getSecureRandom()
    '''
def setSecureRandom():
    '''    public void setSecureRandom(final SecureRandom secureRandom)
    '''
def withSecureRandom():
    '''    public ClientConfiguration withSecureRandom(final SecureRandom secureRandom)
    '''
def isUseExpectContinue():
    '''    public boolean isUseExpectContinue()
    '''
def setUseExpectContinue():
    '''    public void setUseExpectContinue(final boolean useExpectContinue)
    '''
def withUseExpectContinue():
    '''    public ClientConfiguration withUseExpectContinue(final boolean useExpectContinue)
    '''
