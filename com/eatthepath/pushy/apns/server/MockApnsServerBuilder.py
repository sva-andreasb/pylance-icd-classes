def setServerCredentials():
    '''public MockApnsServerBuilder setServerCredentials(final File certificatePemFile, final File privateKeyPkcs8File, final String privateKeyPassword)
    public MockApnsServerBuilder setServerCredentials(final InputStream certificatePemInputStream, final InputStream privateKeyPkcs8InputStream, final String privateKeyPassword)
    public MockApnsServerBuilder setServerCredentials(final X509Certificate[] certificates, final PrivateKey privateKey, final String privateKeyPassword)
    '''
def setTrustedClientCertificateChain():
    '''public MockApnsServerBuilder setTrustedClientCertificateChain(final File certificatePemFile)
    public MockApnsServerBuilder setTrustedClientCertificateChain(final InputStream certificateInputStream)
    '''
def setTrustedServerCertificateChain():
    '''public MockApnsServerBuilder setTrustedServerCertificateChain(final X509Certificate... certificates)
    '''
def setEventLoopGroup():
    '''public MockApnsServerBuilder setEventLoopGroup(final EventLoopGroup eventLoopGroup)
    '''
def setMaxConcurrentStreams():
    '''public MockApnsServerBuilder setMaxConcurrentStreams(final int maxConcurrentStreams)
    '''
def setUseAlpn():
    '''public MockApnsServerBuilder setUseAlpn(final boolean useAlpn)
    '''
def setHandlerFactory():
    '''public MockApnsServerBuilder setHandlerFactory(final PushNotificationHandlerFactory handlerFactory)
    '''
def setListener():
    '''public MockApnsServerBuilder setListener(final MockApnsServerListener listener)
    '''
def build():
    '''public MockApnsServer build()
    '''
