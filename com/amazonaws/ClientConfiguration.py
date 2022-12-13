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
'''public ClientConfiguration()
public ClientConfiguration(final ClientConfiguration other)
'''
pass
def getProtocol():
'''public Protocol getProtocol()
'''
pass
def setProtocol():
'''public void setProtocol(final Protocol protocol)
'''
pass
def withProtocol():
'''public ClientConfiguration withProtocol(final Protocol protocol)
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
def withMaxConnections():
'''public ClientConfiguration withMaxConnections(final int maxConnections)
'''
pass
def getUserAgent():
'''public String getUserAgent()
'''
pass
def setUserAgent():
'''public void setUserAgent(final String userAgent)
'''
pass
def withUserAgent():
'''public ClientConfiguration withUserAgent(final String userAgent)
'''
pass
def getLocalAddress():
'''public InetAddress getLocalAddress()
'''
pass
def setLocalAddress():
'''public void setLocalAddress(final InetAddress localAddress)
'''
pass
def withLocalAddress():
'''public ClientConfiguration withLocalAddress(final InetAddress localAddress)
'''
pass
def getProxyHost():
'''public String getProxyHost()
'''
pass
def setProxyHost():
'''public void setProxyHost(final String proxyHost)
'''
pass
def withProxyHost():
'''public ClientConfiguration withProxyHost(final String proxyHost)
'''
pass
def getProxyPort():
'''public int getProxyPort()
'''
pass
def setProxyPort():
'''public void setProxyPort(final int proxyPort)
'''
pass
def withProxyPort():
'''public ClientConfiguration withProxyPort(final int proxyPort)
'''
pass
def getProxyUsername():
'''public String getProxyUsername()
'''
pass
def setProxyUsername():
'''public void setProxyUsername(final String proxyUsername)
'''
pass
def withProxyUsername():
'''public ClientConfiguration withProxyUsername(final String proxyUsername)
'''
pass
def getProxyPassword():
'''public String getProxyPassword()
'''
pass
def setProxyPassword():
'''public void setProxyPassword(final String proxyPassword)
'''
pass
def withProxyPassword():
'''public ClientConfiguration withProxyPassword(final String proxyPassword)
'''
pass
def getProxyDomain():
'''public String getProxyDomain()
'''
pass
def setProxyDomain():
'''public void setProxyDomain(final String proxyDomain)
'''
pass
def withProxyDomain():
'''public ClientConfiguration withProxyDomain(final String proxyDomain)
'''
pass
def getProxyWorkstation():
'''public String getProxyWorkstation()
'''
pass
def setProxyWorkstation():
'''public void setProxyWorkstation(final String proxyWorkstation)
'''
pass
def withProxyWorkstation():
'''public ClientConfiguration withProxyWorkstation(final String proxyWorkstation)
'''
pass
def getRetryPolicy():
'''public RetryPolicy getRetryPolicy()
'''
pass
def setRetryPolicy():
'''public void setRetryPolicy(final RetryPolicy retryPolicy)
'''
pass
def withRetryPolicy():
'''public ClientConfiguration withRetryPolicy(final RetryPolicy retryPolicy)
'''
pass
def getMaxErrorRetry():
'''public int getMaxErrorRetry()
'''
pass
def setMaxErrorRetry():
'''public void setMaxErrorRetry(final int maxErrorRetry)
'''
pass
def withMaxErrorRetry():
'''public ClientConfiguration withMaxErrorRetry(final int maxErrorRetry)
'''
pass
def getSocketTimeout():
'''public int getSocketTimeout()
'''
pass
def setSocketTimeout():
'''public void setSocketTimeout(final int socketTimeout)
'''
pass
def withSocketTimeout():
'''public ClientConfiguration withSocketTimeout(final int socketTimeout)
'''
pass
def getConnectionTimeout():
'''public int getConnectionTimeout()
'''
pass
def setConnectionTimeout():
'''public void setConnectionTimeout(final int connectionTimeout)
'''
pass
def withConnectionTimeout():
'''public ClientConfiguration withConnectionTimeout(final int connectionTimeout)
'''
pass
def getRequestTimeout():
'''public int getRequestTimeout()
'''
pass
def setRequestTimeout():
'''public void setRequestTimeout(final int requestTimeout)
'''
pass
def withRequestTimeout():
'''public ClientConfiguration withRequestTimeout(final int requestTimeout)
'''
pass
def getClientExecutionTimeout():
'''public int getClientExecutionTimeout()
'''
pass
def setClientExecutionTimeout():
'''public void setClientExecutionTimeout(final int clientExecutionTimeout)
'''
pass
def withClientExecutionTimeout():
'''public ClientConfiguration withClientExecutionTimeout(final int clientExecutionTimeout)
'''
pass
def useReaper():
'''public boolean useReaper()
'''
pass
def setUseReaper():
'''public void setUseReaper(final boolean use)
'''
pass
def withReaper():
'''public ClientConfiguration withReaper(final boolean use)
'''
pass
def useThrottledRetries():
'''public boolean useThrottledRetries()
'''
pass
def setUseThrottleRetries():
'''public void setUseThrottleRetries(final boolean use)
'''
pass
def withThrottledRetries():
'''public ClientConfiguration withThrottledRetries(final boolean use)
'''
pass
def useGzip():
'''public boolean useGzip()
'''
pass
def setUseGzip():
'''public void setUseGzip(final boolean use)
'''
pass
def withGzip():
'''public ClientConfiguration withGzip(final boolean use)
'''
pass
def getSocketBufferSizeHints():
'''public int[] getSocketBufferSizeHints()
'''
pass
def setSocketBufferSizeHints():
'''public void setSocketBufferSizeHints(final int socketSendBufferSizeHint, final int socketReceiveBufferSizeHint)
'''
pass
def withSocketBufferSizeHints():
'''public ClientConfiguration withSocketBufferSizeHints(final int socketSendBufferSizeHint, final int socketReceiveBufferSizeHint)
'''
pass
def getSignerOverride():
'''public String getSignerOverride()
'''
pass
def setSignerOverride():
'''public void setSignerOverride(final String value)
'''
pass
def withSignerOverride():
'''public ClientConfiguration withSignerOverride(final String value)
'''
pass
def isPreemptiveBasicProxyAuth():
'''public boolean isPreemptiveBasicProxyAuth()
'''
pass
def setPreemptiveBasicProxyAuth():
'''public void setPreemptiveBasicProxyAuth(final Boolean preemptiveBasicProxyAuth)
'''
pass
def withPreemptiveBasicProxyAuth():
'''public ClientConfiguration withPreemptiveBasicProxyAuth(final boolean preemptiveBasicProxyAuth)
'''
pass
def getConnectionTTL():
'''public long getConnectionTTL()
'''
pass
def setConnectionTTL():
'''public void setConnectionTTL(final long connectionTTL)
'''
pass
def withConnectionTTL():
'''public ClientConfiguration withConnectionTTL(final long connectionTTL)
'''
pass
def getConnectionMaxIdleMillis():
'''public long getConnectionMaxIdleMillis()
'''
pass
def setConnectionMaxIdleMillis():
'''public void setConnectionMaxIdleMillis(final long connectionMaxIdleMillis)
'''
pass
def withConnectionMaxIdleMillis():
'''public ClientConfiguration withConnectionMaxIdleMillis(final long connectionMaxIdleMillis)
'''
pass
def useTcpKeepAlive():
'''public boolean useTcpKeepAlive()
'''
pass
def setUseTcpKeepAlive():
'''public void setUseTcpKeepAlive(final boolean use)
'''
pass
def withTcpKeepAlive():
'''public ClientConfiguration withTcpKeepAlive(final boolean use)
'''
pass
def getDnsResolver():
'''public DnsResolver getDnsResolver()
'''
pass
def setDnsResolver():
'''public void setDnsResolver(final DnsResolver resolver)
'''
pass
def withDnsResolver():
'''public ClientConfiguration withDnsResolver(final DnsResolver resolver)
'''
pass
def getResponseMetadataCacheSize():
'''public int getResponseMetadataCacheSize()
'''
pass
def setResponseMetadataCacheSize():
'''public void setResponseMetadataCacheSize(final int responseMetadataCacheSize)
'''
pass
def withResponseMetadataCacheSize():
'''public ClientConfiguration withResponseMetadataCacheSize(final int responseMetadataCacheSize)
'''
pass
def getApacheHttpClientConfig():
'''public ApacheHttpClientConfig getApacheHttpClientConfig()
'''
pass
def getSecureRandom():
'''public SecureRandom getSecureRandom()
'''
pass
def setSecureRandom():
'''public void setSecureRandom(final SecureRandom secureRandom)
'''
pass
def withSecureRandom():
'''public ClientConfiguration withSecureRandom(final SecureRandom secureRandom)
'''
pass
def isUseExpectContinue():
'''public boolean isUseExpectContinue()
'''
pass
def setUseExpectContinue():
'''public void setUseExpectContinue(final boolean useExpectContinue)
'''
pass
def withUseExpectContinue():
'''public ClientConfiguration withUseExpectContinue(final boolean useExpectContinue)
'''
pass
