def sslProvider():
    '''returns SslContextBuilder\n\n
    sslProvider(final SslProvider provider)\n
    '''
def keyStoreType():
    '''returns SslContextBuilder\n\n
    keyStoreType(final String keyStoreType)\n
    '''
def sslContextProvider():
    '''returns SslContextBuilder\n\n
    sslContextProvider(final Provider sslContextProvider)\n
    '''
def trustManager():
    '''returns SslContextBuilder\n\n
    trustManager(final File trustCertCollectionFile)\n
    trustManager(final InputStream trustCertCollectionInputStream)\n
    trustManager(final X509Certificate... trustCertCollection)\n
    trustManager(final Iterable<? extends X509Certificate> trustCertCollection)\n
    trustManager(final TrustManagerFactory trustManagerFactory)\n
    trustManager(final TrustManager trustManager)\n
    '''
def keyManager():
    '''returns SslContextBuilder\n\n
    keyManager(final File keyCertChainFile, final File keyFile)\n
    keyManager(final InputStream keyCertChainInputStream, final InputStream keyInputStream)\n
    keyManager(final PrivateKey key, final X509Certificate... keyCertChain)\n
    keyManager(final PrivateKey key, final Iterable<? extends X509Certificate> keyCertChain)\n
    keyManager(final File keyCertChainFile, final File keyFile, final String keyPassword)\n
    keyManager(final InputStream keyCertChainInputStream, final InputStream keyInputStream, final String keyPassword)\n
    keyManager(final PrivateKey key, final String keyPassword, final X509Certificate... keyCertChain)\n
    keyManager(final PrivateKey key, final String keyPassword, final Iterable<? extends X509Certificate> keyCertChain)\n
    keyManager(final KeyManagerFactory keyManagerFactory)\n
    keyManager(final KeyManager keyManager)\n
    '''
def ciphers():
    '''returns SslContextBuilder\n\n
    ciphers(final Iterable<String> ciphers)\n
    ciphers(final Iterable<String> ciphers, final CipherSuiteFilter cipherFilter)\n
    '''
def applicationProtocolConfig():
    '''returns SslContextBuilder\n\n
    applicationProtocolConfig(final ApplicationProtocolConfig apn)\n
    '''
def sessionCacheSize():
    '''returns SslContextBuilder\n\n
    sessionCacheSize(final long sessionCacheSize)\n
    '''
def sessionTimeout():
    '''returns SslContextBuilder\n\n
    sessionTimeout(final long sessionTimeout)\n
    '''
def clientAuth():
    '''returns SslContextBuilder\n\n
    clientAuth(final ClientAuth clientAuth)\n
    '''
def protocols():
    '''returns SslContextBuilder\n\n
    protocols(final String... protocols)\n
    protocols(final Iterable<String> protocols)\n
    '''
def startTls():
    '''returns SslContextBuilder\n\n
    startTls(final boolean startTls)\n
    '''
def enableOcsp():
    '''returns SslContextBuilder\n\n
    enableOcsp(final boolean enableOcsp)\n
    '''
def build():
    '''returns SslContext\n\n
    build()\n
    '''
