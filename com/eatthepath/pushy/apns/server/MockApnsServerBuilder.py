def setServerCredentials():
'''public MockApnsServerBuilder setServerCredentials(final File certificatePemFile, final File privateKeyPkcs8File, final String privateKeyPassword)
public MockApnsServerBuilder setServerCredentials(final InputStream certificatePemInputStream, final InputStream privateKeyPkcs8InputStream, final String privateKeyPassword)
public MockApnsServerBuilder setServerCredentials(final X509Certificate[] certificates, final PrivateKey privateKey, final String privateKeyPassword)
'''
pass
def setTrustedClientCertificateChain():
'''public MockApnsServerBuilder setTrustedClientCertificateChain(final File certificatePemFile)
public MockApnsServerBuilder setTrustedClientCertificateChain(final InputStream certificateInputStream)
'''
pass
def setTrustedServerCertificateChain():
'''public MockApnsServerBuilder setTrustedServerCertificateChain(final X509Certificate... certificates)
'''
pass
def setEventLoopGroup():
'''public MockApnsServerBuilder setEventLoopGroup(final EventLoopGroup eventLoopGroup)
'''
pass
def setMaxConcurrentStreams():
'''public MockApnsServerBuilder setMaxConcurrentStreams(final int maxConcurrentStreams)
'''
pass
def setUseAlpn():
'''public MockApnsServerBuilder setUseAlpn(final boolean useAlpn)
'''
pass
def setHandlerFactory():
'''public MockApnsServerBuilder setHandlerFactory(final PushNotificationHandlerFactory handlerFactory)
'''
pass
def setListener():
'''public MockApnsServerBuilder setListener(final MockApnsServerListener listener)
'''
pass
def build():
'''public MockApnsServer build()
'''
pass
