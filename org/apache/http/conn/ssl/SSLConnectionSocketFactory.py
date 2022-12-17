TLS = "String  \"TLS\""
SSL = "String  \"SSL\""
SSLV2 = "String  \"SSLv2\""
def ():
    '''returns SSLConnectionSocketFactory\n\n
    (final SSLContext sslContext)\n
    (final SSLContext sslContext, final X509HostnameVerifier hostnameVerifier)\n
    (final SSLContext sslContext, final String[] supportedProtocols, final String[] supportedCipherSuites, final X509HostnameVerifier hostnameVerifier)\n
    (final SSLSocketFactory socketfactory, final X509HostnameVerifier hostnameVerifier)\n
    (final SSLSocketFactory socketfactory, final String[] supportedProtocols, final String[] supportedCipherSuites, final X509HostnameVerifier hostnameVerifier)\n
    (final SSLContext sslContext, final HostnameVerifier hostnameVerifier)\n
    (final SSLContext sslContext, final String[] supportedProtocols, final String[] supportedCipherSuites, final HostnameVerifier hostnameVerifier)\n
    (final SSLSocketFactory socketfactory, final HostnameVerifier hostnameVerifier)\n
    (final SSLSocketFactory socketfactory, final String[] supportedProtocols, final String[] supportedCipherSuites, final HostnameVerifier hostnameVerifier)\n
    '''
def createSocket():
    '''returns Socket\n\n
    createSocket(final HttpContext context)\n
    '''
def connectSocket():
    '''returns Socket\n\n
    connectSocket(final int connectTimeout, final Socket socket, final HttpHost host, final InetSocketAddress remoteAddress, final InetSocketAddress localAddress, final HttpContext context)\n
    '''
def createLayeredSocket():
    '''returns Socket\n\n
    createLayeredSocket(final Socket socket, final String target, final int port, final HttpContext context)\n
    '''
