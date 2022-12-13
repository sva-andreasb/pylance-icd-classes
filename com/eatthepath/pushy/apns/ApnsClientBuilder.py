PRODUCTION_APNS_HOST = "String  \"api.push.apple.com\""
DEVELOPMENT_APNS_HOST = "String  \"api.sandbox.push.apple.com\""
DEFAULT_APNS_PORT = "int  443"
ALTERNATE_APNS_PORT = "int  2197"
def ApnsClientBuilder():
    '''    public ApnsClientBuilder()
    '''
def setApnsServer():
    '''    public ApnsClientBuilder setApnsServer(final String hostname)
    public ApnsClientBuilder setApnsServer(final String hostname, final int port)
    '''
def setClientCredentials():
    '''    public ApnsClientBuilder setClientCredentials(final File p12File, final String p12Password)
    public ApnsClientBuilder setClientCredentials(final InputStream p12InputStream, final String p12Password)
    public ApnsClientBuilder setClientCredentials(final X509Certificate clientCertificate, final PrivateKey privateKey, final String privateKeyPassword)
    '''
def setSigningKey():
    '''    public ApnsClientBuilder setSigningKey(final ApnsSigningKey signingKey)
    '''
def setTokenExpiration():
    '''    public ApnsClientBuilder setTokenExpiration(final Duration tokenExpiration)
    '''
def setTrustedServerCertificateChain():
    '''    public ApnsClientBuilder setTrustedServerCertificateChain(final File certificatePemFile)
    public ApnsClientBuilder setTrustedServerCertificateChain(final InputStream certificateInputStream)
    public ApnsClientBuilder setTrustedServerCertificateChain(final X509Certificate... certificates)
    '''
def setEventLoopGroup():
    '''    public ApnsClientBuilder setEventLoopGroup(final EventLoopGroup eventLoopGroup)
    '''
def setConcurrentConnections():
    '''    public ApnsClientBuilder setConcurrentConnections(final int concurrentConnections)
    '''
def setMetricsListener():
    '''    public ApnsClientBuilder setMetricsListener(final ApnsClientMetricsListener metricsListener)
    '''
def setProxyHandlerFactory():
    '''    public ApnsClientBuilder setProxyHandlerFactory(final ProxyHandlerFactory proxyHandlerFactory)
    '''
def setConnectionTimeout():
    '''    public ApnsClientBuilder setConnectionTimeout(final Duration timeout)
    '''
def setIdlePingInterval():
    '''    public ApnsClientBuilder setIdlePingInterval(final Duration idlePingInterval)
    '''
def setGracefulShutdownTimeout():
    '''    public ApnsClientBuilder setGracefulShutdownTimeout(final Duration gracefulShutdownTimeout)
    '''
def setFrameLogger():
    '''    public ApnsClientBuilder setFrameLogger(final Http2FrameLogger frameLogger)
    '''
def build():
    '''    public ApnsClient build()
    '''
