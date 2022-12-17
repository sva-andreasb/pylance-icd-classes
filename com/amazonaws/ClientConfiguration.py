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
def ():
    '''returns ClientConfiguration\n\n
    ()\n
    (final ClientConfiguration other)\n
    '''
def getProtocol():
    '''returns Protocol\n\n
    getProtocol()\n
    '''
def setProtocol():
    '''returns None\n\n
    setProtocol(final Protocol protocol)\n
    '''
def withProtocol():
    '''returns ClientConfiguration\n\n
    withProtocol(final Protocol protocol)\n
    '''
def getMaxConnections():
    '''returns int\n\n
    getMaxConnections()\n
    '''
def setMaxConnections():
    '''returns None\n\n
    setMaxConnections(final int maxConnections)\n
    '''
def withMaxConnections():
    '''returns ClientConfiguration\n\n
    withMaxConnections(final int maxConnections)\n
    '''
def getUserAgent():
    '''returns String\n\n
    getUserAgent()\n
    '''
def setUserAgent():
    '''returns None\n\n
    setUserAgent(final String userAgent)\n
    '''
def withUserAgent():
    '''returns ClientConfiguration\n\n
    withUserAgent(final String userAgent)\n
    '''
def getLocalAddress():
    '''returns InetAddress\n\n
    getLocalAddress()\n
    '''
def setLocalAddress():
    '''returns None\n\n
    setLocalAddress(final InetAddress localAddress)\n
    '''
def withLocalAddress():
    '''returns ClientConfiguration\n\n
    withLocalAddress(final InetAddress localAddress)\n
    '''
def getProxyHost():
    '''returns String\n\n
    getProxyHost()\n
    '''
def setProxyHost():
    '''returns None\n\n
    setProxyHost(final String proxyHost)\n
    '''
def withProxyHost():
    '''returns ClientConfiguration\n\n
    withProxyHost(final String proxyHost)\n
    '''
def getProxyPort():
    '''returns int\n\n
    getProxyPort()\n
    '''
def setProxyPort():
    '''returns None\n\n
    setProxyPort(final int proxyPort)\n
    '''
def withProxyPort():
    '''returns ClientConfiguration\n\n
    withProxyPort(final int proxyPort)\n
    '''
def getProxyUsername():
    '''returns String\n\n
    getProxyUsername()\n
    '''
def setProxyUsername():
    '''returns None\n\n
    setProxyUsername(final String proxyUsername)\n
    '''
def withProxyUsername():
    '''returns ClientConfiguration\n\n
    withProxyUsername(final String proxyUsername)\n
    '''
def getProxyPassword():
    '''returns String\n\n
    getProxyPassword()\n
    '''
def setProxyPassword():
    '''returns None\n\n
    setProxyPassword(final String proxyPassword)\n
    '''
def withProxyPassword():
    '''returns ClientConfiguration\n\n
    withProxyPassword(final String proxyPassword)\n
    '''
def getProxyDomain():
    '''returns String\n\n
    getProxyDomain()\n
    '''
def setProxyDomain():
    '''returns None\n\n
    setProxyDomain(final String proxyDomain)\n
    '''
def withProxyDomain():
    '''returns ClientConfiguration\n\n
    withProxyDomain(final String proxyDomain)\n
    '''
def getProxyWorkstation():
    '''returns String\n\n
    getProxyWorkstation()\n
    '''
def setProxyWorkstation():
    '''returns None\n\n
    setProxyWorkstation(final String proxyWorkstation)\n
    '''
def withProxyWorkstation():
    '''returns ClientConfiguration\n\n
    withProxyWorkstation(final String proxyWorkstation)\n
    '''
def getRetryPolicy():
    '''returns RetryPolicy\n\n
    getRetryPolicy()\n
    '''
def setRetryPolicy():
    '''returns None\n\n
    setRetryPolicy(final RetryPolicy retryPolicy)\n
    '''
def withRetryPolicy():
    '''returns ClientConfiguration\n\n
    withRetryPolicy(final RetryPolicy retryPolicy)\n
    '''
def getMaxErrorRetry():
    '''returns int\n\n
    getMaxErrorRetry()\n
    '''
def setMaxErrorRetry():
    '''returns None\n\n
    setMaxErrorRetry(final int maxErrorRetry)\n
    '''
def withMaxErrorRetry():
    '''returns ClientConfiguration\n\n
    withMaxErrorRetry(final int maxErrorRetry)\n
    '''
def getSocketTimeout():
    '''returns int\n\n
    getSocketTimeout()\n
    '''
def setSocketTimeout():
    '''returns None\n\n
    setSocketTimeout(final int socketTimeout)\n
    '''
def withSocketTimeout():
    '''returns ClientConfiguration\n\n
    withSocketTimeout(final int socketTimeout)\n
    '''
def getConnectionTimeout():
    '''returns int\n\n
    getConnectionTimeout()\n
    '''
def setConnectionTimeout():
    '''returns None\n\n
    setConnectionTimeout(final int connectionTimeout)\n
    '''
def withConnectionTimeout():
    '''returns ClientConfiguration\n\n
    withConnectionTimeout(final int connectionTimeout)\n
    '''
def getRequestTimeout():
    '''returns int\n\n
    getRequestTimeout()\n
    '''
def setRequestTimeout():
    '''returns None\n\n
    setRequestTimeout(final int requestTimeout)\n
    '''
def withRequestTimeout():
    '''returns ClientConfiguration\n\n
    withRequestTimeout(final int requestTimeout)\n
    '''
def getClientExecutionTimeout():
    '''returns int\n\n
    getClientExecutionTimeout()\n
    '''
def setClientExecutionTimeout():
    '''returns None\n\n
    setClientExecutionTimeout(final int clientExecutionTimeout)\n
    '''
def withClientExecutionTimeout():
    '''returns ClientConfiguration\n\n
    withClientExecutionTimeout(final int clientExecutionTimeout)\n
    '''
def useReaper():
    '''returns boolean\n\n
    useReaper()\n
    '''
def setUseReaper():
    '''returns None\n\n
    setUseReaper(final boolean use)\n
    '''
def withReaper():
    '''returns ClientConfiguration\n\n
    withReaper(final boolean use)\n
    '''
def useThrottledRetries():
    '''returns boolean\n\n
    useThrottledRetries()\n
    '''
def setUseThrottleRetries():
    '''returns None\n\n
    setUseThrottleRetries(final boolean use)\n
    '''
def withThrottledRetries():
    '''returns ClientConfiguration\n\n
    withThrottledRetries(final boolean use)\n
    '''
def useGzip():
    '''returns boolean\n\n
    useGzip()\n
    '''
def setUseGzip():
    '''returns None\n\n
    setUseGzip(final boolean use)\n
    '''
def withGzip():
    '''returns ClientConfiguration\n\n
    withGzip(final boolean use)\n
    '''
def getSocketBufferSizeHints():
    '''returns int[]\n\n
    getSocketBufferSizeHints()\n
    '''
def setSocketBufferSizeHints():
    '''returns None\n\n
    setSocketBufferSizeHints(final int socketSendBufferSizeHint, final int socketReceiveBufferSizeHint)\n
    '''
def withSocketBufferSizeHints():
    '''returns ClientConfiguration\n\n
    withSocketBufferSizeHints(final int socketSendBufferSizeHint, final int socketReceiveBufferSizeHint)\n
    '''
def getSignerOverride():
    '''returns String\n\n
    getSignerOverride()\n
    '''
def setSignerOverride():
    '''returns None\n\n
    setSignerOverride(final String value)\n
    '''
def withSignerOverride():
    '''returns ClientConfiguration\n\n
    withSignerOverride(final String value)\n
    '''
def isPreemptiveBasicProxyAuth():
    '''returns boolean\n\n
    isPreemptiveBasicProxyAuth()\n
    '''
def setPreemptiveBasicProxyAuth():
    '''returns None\n\n
    setPreemptiveBasicProxyAuth(final Boolean preemptiveBasicProxyAuth)\n
    '''
def withPreemptiveBasicProxyAuth():
    '''returns ClientConfiguration\n\n
    withPreemptiveBasicProxyAuth(final boolean preemptiveBasicProxyAuth)\n
    '''
def getConnectionTTL():
    '''returns long\n\n
    getConnectionTTL()\n
    '''
def setConnectionTTL():
    '''returns None\n\n
    setConnectionTTL(final long connectionTTL)\n
    '''
def withConnectionTTL():
    '''returns ClientConfiguration\n\n
    withConnectionTTL(final long connectionTTL)\n
    '''
def getConnectionMaxIdleMillis():
    '''returns long\n\n
    getConnectionMaxIdleMillis()\n
    '''
def setConnectionMaxIdleMillis():
    '''returns None\n\n
    setConnectionMaxIdleMillis(final long connectionMaxIdleMillis)\n
    '''
def withConnectionMaxIdleMillis():
    '''returns ClientConfiguration\n\n
    withConnectionMaxIdleMillis(final long connectionMaxIdleMillis)\n
    '''
def useTcpKeepAlive():
    '''returns boolean\n\n
    useTcpKeepAlive()\n
    '''
def setUseTcpKeepAlive():
    '''returns None\n\n
    setUseTcpKeepAlive(final boolean use)\n
    '''
def withTcpKeepAlive():
    '''returns ClientConfiguration\n\n
    withTcpKeepAlive(final boolean use)\n
    '''
def getDnsResolver():
    '''returns DnsResolver\n\n
    getDnsResolver()\n
    '''
def setDnsResolver():
    '''returns None\n\n
    setDnsResolver(final DnsResolver resolver)\n
    '''
def withDnsResolver():
    '''returns ClientConfiguration\n\n
    withDnsResolver(final DnsResolver resolver)\n
    '''
def getResponseMetadataCacheSize():
    '''returns int\n\n
    getResponseMetadataCacheSize()\n
    '''
def setResponseMetadataCacheSize():
    '''returns None\n\n
    setResponseMetadataCacheSize(final int responseMetadataCacheSize)\n
    '''
def withResponseMetadataCacheSize():
    '''returns ClientConfiguration\n\n
    withResponseMetadataCacheSize(final int responseMetadataCacheSize)\n
    '''
def getApacheHttpClientConfig():
    '''returns ApacheHttpClientConfig\n\n
    getApacheHttpClientConfig()\n
    '''
def getSecureRandom():
    '''returns SecureRandom\n\n
    getSecureRandom()\n
    '''
def setSecureRandom():
    '''returns None\n\n
    setSecureRandom(final SecureRandom secureRandom)\n
    '''
def withSecureRandom():
    '''returns ClientConfiguration\n\n
    withSecureRandom(final SecureRandom secureRandom)\n
    '''
def isUseExpectContinue():
    '''returns boolean\n\n
    isUseExpectContinue()\n
    '''
def setUseExpectContinue():
    '''returns None\n\n
    setUseExpectContinue(final boolean useExpectContinue)\n
    '''
def withUseExpectContinue():
    '''returns ClientConfiguration\n\n
    withUseExpectContinue(final boolean useExpectContinue)\n
    '''
