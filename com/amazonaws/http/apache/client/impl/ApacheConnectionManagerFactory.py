def ApacheConnectionManagerFactory():
    '''public ApacheConnectionManagerFactory()
    '''
def create():
    '''public HttpClientConnectionManager create(final HttpClientSettings settings)
    '''
def createLayeredSocket():
    '''public Socket createLayeredSocket(final Socket socket, final String target, final int port, final HttpContext context)
    '''
def createSocket():
    '''public Socket createSocket(final HttpContext context)
    '''
def connectSocket():
    '''public Socket connectSocket(final int connectTimeout, final Socket sock, final HttpHost host, final InetSocketAddress remoteAddress, final InetSocketAddress localAddress, final HttpContext context)
    '''
def getAcceptedIssuers():
    '''public X509Certificate[] getAcceptedIssuers()
    '''
def checkServerTrusted():
    '''public void checkServerTrusted(final X509Certificate[] chain, final String authType)
    '''
def checkClientTrusted():
    '''public void checkClientTrusted(final X509Certificate[] chain, final String authType)
    '''
