def setServerCredentials():
    '''returns MockApnsServerBuilder\n\n
    setServerCredentials(final File certificatePemFile, final File privateKeyPkcs8File, final String privateKeyPassword)\n
    setServerCredentials(final InputStream certificatePemInputStream, final InputStream privateKeyPkcs8InputStream, final String privateKeyPassword)\n
    setServerCredentials(final X509Certificate[] certificates, final PrivateKey privateKey, final String privateKeyPassword)\n
    '''
def setTrustedClientCertificateChain():
    '''returns MockApnsServerBuilder\n\n
    setTrustedClientCertificateChain(final File certificatePemFile)\n
    setTrustedClientCertificateChain(final InputStream certificateInputStream)\n
    '''
def setTrustedServerCertificateChain():
    '''returns MockApnsServerBuilder\n\n
    setTrustedServerCertificateChain(final X509Certificate... certificates)\n
    '''
def setEventLoopGroup():
    '''returns MockApnsServerBuilder\n\n
    setEventLoopGroup(final EventLoopGroup eventLoopGroup)\n
    '''
def setMaxConcurrentStreams():
    '''returns MockApnsServerBuilder\n\n
    setMaxConcurrentStreams(final int maxConcurrentStreams)\n
    '''
def setUseAlpn():
    '''returns MockApnsServerBuilder\n\n
    setUseAlpn(final boolean useAlpn)\n
    '''
def setHandlerFactory():
    '''returns MockApnsServerBuilder\n\n
    setHandlerFactory(final PushNotificationHandlerFactory handlerFactory)\n
    '''
def setListener():
    '''returns MockApnsServerBuilder\n\n
    setListener(final MockApnsServerListener listener)\n
    '''
def build():
    '''returns MockApnsServer\n\n
    build()\n
    '''
