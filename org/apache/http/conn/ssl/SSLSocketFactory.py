TLS = "String  \"TLS\""
SSL = "String  \"SSL\""
SSLV2 = "String  \"SSLv2\""
def getSocketFactory():
    '''    public static SSLSocketFactory getSocketFactory()
    '''
def getSystemSocketFactory():
    '''    public static SSLSocketFactory getSystemSocketFactory()
    '''
def SSLSocketFactory():
    '''    public SSLSocketFactory(final String algorithm, final KeyStore keystore, final String keyPassword, final KeyStore truststore, final SecureRandom random, final HostNameResolver nameResolver)
    public SSLSocketFactory(final String algorithm, final KeyStore keystore, final String keyPassword, final KeyStore truststore, final SecureRandom random, final TrustStrategy trustStrategy, final X509HostnameVerifier hostnameVerifier)
    public SSLSocketFactory(final String algorithm, final KeyStore keystore, final String keyPassword, final KeyStore truststore, final SecureRandom random, final X509HostnameVerifier hostnameVerifier)
    public SSLSocketFactory(final KeyStore keystore, final String keystorePassword, final KeyStore truststore)
    public SSLSocketFactory(final KeyStore keystore, final String keystorePassword)
    public SSLSocketFactory(final KeyStore truststore)
    public SSLSocketFactory(final TrustStrategy trustStrategy, final X509HostnameVerifier hostnameVerifier)
    public SSLSocketFactory(final TrustStrategy trustStrategy)
    public SSLSocketFactory(final SSLContext sslContext)
    public SSLSocketFactory(final SSLContext sslContext, final HostNameResolver nameResolver)
    public SSLSocketFactory(final SSLContext sslContext, final X509HostnameVerifier hostnameVerifier)
    public SSLSocketFactory(final SSLContext sslContext, final String[] supportedProtocols, final String[] supportedCipherSuites, final X509HostnameVerifier hostnameVerifier)
    public SSLSocketFactory(final javax.net.ssl.SSLSocketFactory socketfactory, final X509HostnameVerifier hostnameVerifier)
    public SSLSocketFactory(final javax.net.ssl.SSLSocketFactory socketfactory, final String[] supportedProtocols, final String[] supportedCipherSuites, final X509HostnameVerifier hostnameVerifier)
    '''
def createSocket():
    '''    public Socket createSocket(final HttpParams params)
    public Socket createSocket()
    public Socket createSocket(final Socket socket, final String host, final int port, final boolean autoClose)
    public Socket createSocket(final HttpContext context)
    '''
def connectSocket():
    '''    public Socket connectSocket(final Socket socket, final InetSocketAddress remoteAddress, final InetSocketAddress localAddress, final HttpParams params)
    public Socket connectSocket(final Socket socket, final String host, final int port, final InetAddress local, final int localPort, final HttpParams params)
    public Socket connectSocket(final int connectTimeout, final Socket socket, final HttpHost host, final InetSocketAddress remoteAddress, final InetSocketAddress localAddress, final HttpContext context)
    '''
def isSecure():
    '''    public boolean isSecure(final Socket sock)
    '''
def createLayeredSocket():
    '''    public Socket createLayeredSocket(final Socket socket, final String host, final int port, final HttpParams params)
    public Socket createLayeredSocket(final Socket socket, final String host, final int port, final boolean autoClose)
    public Socket createLayeredSocket(final Socket socket, final String target, final int port, final HttpContext context)
    '''
def setHostnameVerifier():
    '''    public void setHostnameVerifier(final X509HostnameVerifier hostnameVerifier)
    '''
def getHostnameVerifier():
    '''    public X509HostnameVerifier getHostnameVerifier()
    '''
