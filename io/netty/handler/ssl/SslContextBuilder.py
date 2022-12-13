def forClient():
'''public static SslContextBuilder forClient()
'''
pass
def forServer():
'''public static SslContextBuilder forServer(final File keyCertChainFile, final File keyFile)
public static SslContextBuilder forServer(final InputStream keyCertChainInputStream, final InputStream keyInputStream)
public static SslContextBuilder forServer(final PrivateKey key, final X509Certificate... keyCertChain)
public static SslContextBuilder forServer(final PrivateKey key, final Iterable<? extends X509Certificate> keyCertChain)
public static SslContextBuilder forServer(final File keyCertChainFile, final File keyFile, final String keyPassword)
public static SslContextBuilder forServer(final InputStream keyCertChainInputStream, final InputStream keyInputStream, final String keyPassword)
public static SslContextBuilder forServer(final PrivateKey key, final String keyPassword, final X509Certificate... keyCertChain)
public static SslContextBuilder forServer(final PrivateKey key, final String keyPassword, final Iterable<? extends X509Certificate> keyCertChain)
public static SslContextBuilder forServer(final KeyManagerFactory keyManagerFactory)
public static SslContextBuilder forServer(final KeyManager keyManager)
'''
pass
def sslProvider():
'''public SslContextBuilder sslProvider(final SslProvider provider)
'''
pass
def keyStoreType():
'''public SslContextBuilder keyStoreType(final String keyStoreType)
'''
pass
def sslContextProvider():
'''public SslContextBuilder sslContextProvider(final Provider sslContextProvider)
'''
pass
def trustManager():
'''public SslContextBuilder trustManager(final File trustCertCollectionFile)
public SslContextBuilder trustManager(final InputStream trustCertCollectionInputStream)
public SslContextBuilder trustManager(final X509Certificate... trustCertCollection)
public SslContextBuilder trustManager(final Iterable<? extends X509Certificate> trustCertCollection)
public SslContextBuilder trustManager(final TrustManagerFactory trustManagerFactory)
public SslContextBuilder trustManager(final TrustManager trustManager)
'''
pass
def keyManager():
'''public SslContextBuilder keyManager(final File keyCertChainFile, final File keyFile)
public SslContextBuilder keyManager(final InputStream keyCertChainInputStream, final InputStream keyInputStream)
public SslContextBuilder keyManager(final PrivateKey key, final X509Certificate... keyCertChain)
public SslContextBuilder keyManager(final PrivateKey key, final Iterable<? extends X509Certificate> keyCertChain)
public SslContextBuilder keyManager(final File keyCertChainFile, final File keyFile, final String keyPassword)
public SslContextBuilder keyManager(final InputStream keyCertChainInputStream, final InputStream keyInputStream, final String keyPassword)
public SslContextBuilder keyManager(final PrivateKey key, final String keyPassword, final X509Certificate... keyCertChain)
public SslContextBuilder keyManager(final PrivateKey key, final String keyPassword, final Iterable<? extends X509Certificate> keyCertChain)
public SslContextBuilder keyManager(final KeyManagerFactory keyManagerFactory)
public SslContextBuilder keyManager(final KeyManager keyManager)
'''
pass
def ciphers():
'''public SslContextBuilder ciphers(final Iterable<String> ciphers)
public SslContextBuilder ciphers(final Iterable<String> ciphers, final CipherSuiteFilter cipherFilter)
'''
pass
def applicationProtocolConfig():
'''public SslContextBuilder applicationProtocolConfig(final ApplicationProtocolConfig apn)
'''
pass
def sessionCacheSize():
'''public SslContextBuilder sessionCacheSize(final long sessionCacheSize)
'''
pass
def sessionTimeout():
'''public SslContextBuilder sessionTimeout(final long sessionTimeout)
'''
pass
def clientAuth():
'''public SslContextBuilder clientAuth(final ClientAuth clientAuth)
'''
pass
def protocols():
'''public SslContextBuilder protocols(final String... protocols)
public SslContextBuilder protocols(final Iterable<String> protocols)
'''
pass
def startTls():
'''public SslContextBuilder startTls(final boolean startTls)
'''
pass
def enableOcsp():
'''public SslContextBuilder enableOcsp(final boolean enableOcsp)
'''
pass
def build():
'''public SslContext build()
'''
pass