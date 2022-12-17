def setServerCredentials():
    '''returns BenchmarkApnsServerBuilder\n\n
    setServerCredentials(final File certificatePemFile, final File privateKeyPkcs8File, final String privateKeyPassword)\n
    setServerCredentials(final InputStream certificatePemInputStream, final InputStream privateKeyPkcs8InputStream, final String privateKeyPassword)\n
    setServerCredentials(final X509Certificate[] certificates, final PrivateKey privateKey, final String privateKeyPassword)\n
    '''
def setTrustedClientCertificateChain():
    '''returns BenchmarkApnsServerBuilder\n\n
    setTrustedClientCertificateChain(final File certificatePemFile)\n
    setTrustedClientCertificateChain(final InputStream certificateInputStream)\n
    '''
def setTrustedServerCertificateChain():
    '''returns BenchmarkApnsServerBuilder\n\n
    setTrustedServerCertificateChain(final X509Certificate... certificates)\n
    '''
def setEventLoopGroup():
    '''returns BenchmarkApnsServerBuilder\n\n
    setEventLoopGroup(final EventLoopGroup eventLoopGroup)\n
    '''
def setMaxConcurrentStreams():
    '''returns BenchmarkApnsServerBuilder\n\n
    setMaxConcurrentStreams(final int maxConcurrentStreams)\n
    '''
def setUseAlpn():
    '''returns BenchmarkApnsServerBuilder\n\n
    setUseAlpn(final boolean useAlpn)\n
    '''
def build():
    '''returns BenchmarkApnsServer\n\n
    build()\n
    '''
