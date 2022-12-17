def ():
    '''returns ApacheConnectionManagerFactory\n\n
    ()\n
    '''
def create():
    '''returns HttpClientConnectionManager\n\n
    create(final HttpClientSettings settings)\n
    '''
def createLayeredSocket():
    '''returns Socket\n\n
    createLayeredSocket(final Socket socket, final String target, final int port, final HttpContext context)\n
    '''
def createSocket():
    '''returns Socket\n\n
    createSocket(final HttpContext context)\n
    '''
def connectSocket():
    '''returns Socket\n\n
    connectSocket(final int connectTimeout, final Socket sock, final HttpHost host, final InetSocketAddress remoteAddress, final InetSocketAddress localAddress, final HttpContext context)\n
    '''
def getAcceptedIssuers():
    '''returns X509Certificate[]\n\n
    getAcceptedIssuers()\n
    '''
def checkServerTrusted():
    '''returns None\n\n
    checkServerTrusted(final X509Certificate[] chain, final String authType)\n
    '''
def checkClientTrusted():
    '''returns None\n\n
    checkClientTrusted(final X509Certificate[] chain, final String authType)\n
    '''
