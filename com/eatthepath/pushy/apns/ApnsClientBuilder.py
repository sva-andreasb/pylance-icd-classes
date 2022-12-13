PRODUCTION_APNS_HOST = "String  api.push.apple.com""
DEVELOPMENT_APNS_HOST = "String  api.sandbox.push.apple.com""
DEFAULT_APNS_PORT = "int  443"
ALTERNATE_APNS_PORT = "int  2197"
def ApnsClientBuilder():
'''public ApnsClientBuilder()
'''
pass
def setApnsServer():
'''public ApnsClientBuilder setApnsServer(final String hostname)
public ApnsClientBuilder setApnsServer(final String hostname, final int port)
'''
pass
def setClientCredentials():
'''public ApnsClientBuilder setClientCredentials(final File p12File, final String p12Password)
public ApnsClientBuilder setClientCredentials(final InputStream p12InputStream, final String p12Password)
public ApnsClientBuilder setClientCredentials(final X509Certificate clientCertificate, final PrivateKey privateKey, final String privateKeyPassword)
'''
pass
def setSigningKey():
'''public ApnsClientBuilder setSigningKey(final ApnsSigningKey signingKey)
'''
pass
def setTokenExpiration():
'''public ApnsClientBuilder setTokenExpiration(final Duration tokenExpiration)
'''
pass
def setTrustedServerCertificateChain():
'''public ApnsClientBuilder setTrustedServerCertificateChain(final File certificatePemFile)
public ApnsClientBuilder setTrustedServerCertificateChain(final InputStream certificateInputStream)
public ApnsClientBuilder setTrustedServerCertificateChain(final X509Certificate... certificates)
'''
pass
def setEventLoopGroup():
'''public ApnsClientBuilder setEventLoopGroup(final EventLoopGroup eventLoopGroup)
'''
pass
def setConcurrentConnections():
'''public ApnsClientBuilder setConcurrentConnections(final int concurrentConnections)
'''
pass
def setMetricsListener():
'''public ApnsClientBuilder setMetricsListener(final ApnsClientMetricsListener metricsListener)
'''
pass
def setProxyHandlerFactory():
'''public ApnsClientBuilder setProxyHandlerFactory(final ProxyHandlerFactory proxyHandlerFactory)
'''
pass
def setConnectionTimeout():
'''public ApnsClientBuilder setConnectionTimeout(final Duration timeout)
'''
pass
def setIdlePingInterval():
'''public ApnsClientBuilder setIdlePingInterval(final Duration idlePingInterval)
'''
pass
def setGracefulShutdownTimeout():
'''public ApnsClientBuilder setGracefulShutdownTimeout(final Duration gracefulShutdownTimeout)
'''
pass
def setFrameLogger():
'''public ApnsClientBuilder setFrameLogger(final Http2FrameLogger frameLogger)
'''
pass
def build():
'''public ApnsClient build()
'''
pass
