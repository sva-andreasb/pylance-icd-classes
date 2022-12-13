TLS = "String  TLS""
SSL = "String  SSL""
SSLV2 = "String  SSLv2""
def getDefaultHostnameVerifier():
'''public static HostnameVerifier getDefaultHostnameVerifier()
'''
pass
def getSocketFactory():
'''public static SSLConnectionSocketFactory getSocketFactory()
'''
pass
def getSystemSocketFactory():
'''public static SSLConnectionSocketFactory getSystemSocketFactory()
'''
pass
def SSLConnectionSocketFactory():
'''public SSLConnectionSocketFactory(final SSLContext sslContext)
public SSLConnectionSocketFactory(final SSLContext sslContext, final X509HostnameVerifier hostnameVerifier)
public SSLConnectionSocketFactory(final SSLContext sslContext, final String[] supportedProtocols, final String[] supportedCipherSuites, final X509HostnameVerifier hostnameVerifier)
public SSLConnectionSocketFactory(final SSLSocketFactory socketfactory, final X509HostnameVerifier hostnameVerifier)
public SSLConnectionSocketFactory(final SSLSocketFactory socketfactory, final String[] supportedProtocols, final String[] supportedCipherSuites, final X509HostnameVerifier hostnameVerifier)
public SSLConnectionSocketFactory(final SSLContext sslContext, final HostnameVerifier hostnameVerifier)
public SSLConnectionSocketFactory(final SSLContext sslContext, final String[] supportedProtocols, final String[] supportedCipherSuites, final HostnameVerifier hostnameVerifier)
public SSLConnectionSocketFactory(final SSLSocketFactory socketfactory, final HostnameVerifier hostnameVerifier)
public SSLConnectionSocketFactory(final SSLSocketFactory socketfactory, final String[] supportedProtocols, final String[] supportedCipherSuites, final HostnameVerifier hostnameVerifier)
'''
pass
def createSocket():
'''public Socket createSocket(final HttpContext context)
'''
pass
def connectSocket():
'''public Socket connectSocket(final int connectTimeout, final Socket socket, final HttpHost host, final InetSocketAddress remoteAddress, final InetSocketAddress localAddress, final HttpContext context)
'''
pass
def createLayeredSocket():
'''public Socket createLayeredSocket(final Socket socket, final String target, final int port, final HttpContext context)
'''
pass
