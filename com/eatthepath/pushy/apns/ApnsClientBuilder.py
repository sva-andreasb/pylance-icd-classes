PRODUCTION_APNS_HOST = "String  \"api.push.apple.com\""
DEVELOPMENT_APNS_HOST = "String  \"api.sandbox.push.apple.com\""
DEFAULT_APNS_PORT = "int  443"
ALTERNATE_APNS_PORT = "int  2197"
def ():
    '''returns ApnsClientBuilder\n\n
    ()\n
    '''
def setApnsServer():
    '''returns ApnsClientBuilder\n\n
    setApnsServer(final String hostname)\n
    setApnsServer(final String hostname, final int port)\n
    '''
def setClientCredentials():
    '''returns ApnsClientBuilder\n\n
    setClientCredentials(final File p12File, final String p12Password)\n
    setClientCredentials(final InputStream p12InputStream, final String p12Password)\n
    setClientCredentials(final X509Certificate clientCertificate, final PrivateKey privateKey, final String privateKeyPassword)\n
    '''
def setSigningKey():
    '''returns ApnsClientBuilder\n\n
    setSigningKey(final ApnsSigningKey signingKey)\n
    '''
def setTokenExpiration():
    '''returns ApnsClientBuilder\n\n
    setTokenExpiration(final Duration tokenExpiration)\n
    '''
def setTrustedServerCertificateChain():
    '''returns ApnsClientBuilder\n\n
    setTrustedServerCertificateChain(final File certificatePemFile)\n
    setTrustedServerCertificateChain(final InputStream certificateInputStream)\n
    setTrustedServerCertificateChain(final X509Certificate... certificates)\n
    '''
def setEventLoopGroup():
    '''returns ApnsClientBuilder\n\n
    setEventLoopGroup(final EventLoopGroup eventLoopGroup)\n
    '''
def setConcurrentConnections():
    '''returns ApnsClientBuilder\n\n
    setConcurrentConnections(final int concurrentConnections)\n
    '''
def setMetricsListener():
    '''returns ApnsClientBuilder\n\n
    setMetricsListener(final ApnsClientMetricsListener metricsListener)\n
    '''
def setProxyHandlerFactory():
    '''returns ApnsClientBuilder\n\n
    setProxyHandlerFactory(final ProxyHandlerFactory proxyHandlerFactory)\n
    '''
def setConnectionTimeout():
    '''returns ApnsClientBuilder\n\n
    setConnectionTimeout(final Duration timeout)\n
    '''
def setIdlePingInterval():
    '''returns ApnsClientBuilder\n\n
    setIdlePingInterval(final Duration idlePingInterval)\n
    '''
def setGracefulShutdownTimeout():
    '''returns ApnsClientBuilder\n\n
    setGracefulShutdownTimeout(final Duration gracefulShutdownTimeout)\n
    '''
def setFrameLogger():
    '''returns ApnsClientBuilder\n\n
    setFrameLogger(final Http2FrameLogger frameLogger)\n
    '''
def build():
    '''returns ApnsClient\n\n
    build()\n
    '''
