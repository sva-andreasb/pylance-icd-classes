def setServerCredentials():
    '''    public BenchmarkApnsServerBuilder setServerCredentials(final File certificatePemFile, final File privateKeyPkcs8File, final String privateKeyPassword)
    public BenchmarkApnsServerBuilder setServerCredentials(final InputStream certificatePemInputStream, final InputStream privateKeyPkcs8InputStream, final String privateKeyPassword)
    public BenchmarkApnsServerBuilder setServerCredentials(final X509Certificate[] certificates, final PrivateKey privateKey, final String privateKeyPassword)
    '''
def setTrustedClientCertificateChain():
    '''    public BenchmarkApnsServerBuilder setTrustedClientCertificateChain(final File certificatePemFile)
    public BenchmarkApnsServerBuilder setTrustedClientCertificateChain(final InputStream certificateInputStream)
    '''
def setTrustedServerCertificateChain():
    '''    public BenchmarkApnsServerBuilder setTrustedServerCertificateChain(final X509Certificate... certificates)
    '''
def setEventLoopGroup():
    '''    public BenchmarkApnsServerBuilder setEventLoopGroup(final EventLoopGroup eventLoopGroup)
    '''
def setMaxConcurrentStreams():
    '''    public BenchmarkApnsServerBuilder setMaxConcurrentStreams(final int maxConcurrentStreams)
    '''
def setUseAlpn():
    '''    public BenchmarkApnsServerBuilder setUseAlpn(final boolean useAlpn)
    '''
def build():
    '''    public BenchmarkApnsServer build()
    '''
