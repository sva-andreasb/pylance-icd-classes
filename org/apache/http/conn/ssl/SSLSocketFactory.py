TLS = "String  \"TLS\""
SSL = "String  \"SSL\""
SSLV2 = "String  \"SSLv2\""
def ():
    '''returns SSLSocketFactory\n\n
    (final String algorithm, final KeyStore keystore, final String keyPassword, final KeyStore truststore, final SecureRandom random, final HostNameResolver nameResolver)\n
    (final String algorithm, final KeyStore keystore, final String keyPassword, final KeyStore truststore, final SecureRandom random, final TrustStrategy trustStrategy, final X509HostnameVerifier hostnameVerifier)\n
    (final String algorithm, final KeyStore keystore, final String keyPassword, final KeyStore truststore, final SecureRandom random, final X509HostnameVerifier hostnameVerifier)\n
    (final KeyStore keystore, final String keystorePassword, final KeyStore truststore)\n
    (final KeyStore keystore, final String keystorePassword)\n
    (final KeyStore truststore)\n
    (final TrustStrategy trustStrategy, final X509HostnameVerifier hostnameVerifier)\n
    (final TrustStrategy trustStrategy)\n
    (final SSLContext sslContext)\n
    (final SSLContext sslContext, final HostNameResolver nameResolver)\n
    (final SSLContext sslContext, final X509HostnameVerifier hostnameVerifier)\n
    (final SSLContext sslContext, final String[] supportedProtocols, final String[] supportedCipherSuites, final X509HostnameVerifier hostnameVerifier)\n
    (final javax.net.ssl.SSLSocketFactory socketfactory, final X509HostnameVerifier hostnameVerifier)\n
    (final javax.net.ssl.SSLSocketFactory socketfactory, final String[] supportedProtocols, final String[] supportedCipherSuites, final X509HostnameVerifier hostnameVerifier)\n
    '''
def createSocket():
    '''returns Socket\n\n
    createSocket(final HttpParams params)\n
    createSocket()\n
    createSocket(final Socket socket, final String host, final int port, final boolean autoClose)\n
    createSocket(final HttpContext context)\n
    '''
def connectSocket():
    '''returns Socket\n\n
    connectSocket(final Socket socket, final InetSocketAddress remoteAddress, final InetSocketAddress localAddress, final HttpParams params)\n
    connectSocket(final Socket socket, final String host, final int port, final InetAddress local, final int localPort, final HttpParams params)\n
    connectSocket(final int connectTimeout, final Socket socket, final HttpHost host, final InetSocketAddress remoteAddress, final InetSocketAddress localAddress, final HttpContext context)\n
    '''
def isSecure():
    '''returns boolean\n\n
    isSecure(final Socket sock)\n
    '''
def createLayeredSocket():
    '''returns Socket\n\n
    createLayeredSocket(final Socket socket, final String host, final int port, final HttpParams params)\n
    createLayeredSocket(final Socket socket, final String host, final int port, final boolean autoClose)\n
    createLayeredSocket(final Socket socket, final String target, final int port, final HttpContext context)\n
    '''
def setHostnameVerifier():
    '''returns None\n\n
    setHostnameVerifier(final X509HostnameVerifier hostnameVerifier)\n
    '''
def getHostnameVerifier():
    '''returns X509HostnameVerifier\n\n
    getHostnameVerifier()\n
    '''
