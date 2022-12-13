def bootstrap():
    '''public static ServerBootstrap bootstrap()
    '''
def setListenerPort():
    '''public final ServerBootstrap setListenerPort(final int listenerPort)
    '''
def setLocalAddress():
    '''public final ServerBootstrap setLocalAddress(final InetAddress localAddress)
    '''
def setSocketConfig():
    '''public final ServerBootstrap setSocketConfig(final SocketConfig socketConfig)
    '''
def setConnectionConfig():
    '''public final ServerBootstrap setConnectionConfig(final ConnectionConfig connectionConfig)
    '''
def setHttpProcessor():
    '''public final ServerBootstrap setHttpProcessor(final HttpProcessor httpProcessor)
    '''
def addInterceptorFirst():
    '''public final ServerBootstrap addInterceptorFirst(final HttpResponseInterceptor itcp)
    public final ServerBootstrap addInterceptorFirst(final HttpRequestInterceptor itcp)
    '''
def addInterceptorLast():
    '''public final ServerBootstrap addInterceptorLast(final HttpResponseInterceptor itcp)
    public final ServerBootstrap addInterceptorLast(final HttpRequestInterceptor itcp)
    '''
def setServerInfo():
    '''public final ServerBootstrap setServerInfo(final String serverInfo)
    '''
def setConnectionReuseStrategy():
    '''public final ServerBootstrap setConnectionReuseStrategy(final ConnectionReuseStrategy connStrategy)
    '''
def setResponseFactory():
    '''public final ServerBootstrap setResponseFactory(final HttpResponseFactory responseFactory)
    '''
def setHandlerMapper():
    '''public final ServerBootstrap setHandlerMapper(final HttpRequestHandlerMapper handlerMapper)
    '''
def registerHandler():
    '''public final ServerBootstrap registerHandler(final String pattern, final HttpRequestHandler handler)
    '''
def setExpectationVerifier():
    '''public final ServerBootstrap setExpectationVerifier(final HttpExpectationVerifier expectationVerifier)
    '''
def setConnectionFactory():
    '''public final ServerBootstrap setConnectionFactory(final HttpConnectionFactory<? extends DefaultBHttpServerConnection> connectionFactory)
    '''
def setSslSetupHandler():
    '''public final ServerBootstrap setSslSetupHandler(final SSLServerSetupHandler sslSetupHandler)
    '''
def setServerSocketFactory():
    '''public final ServerBootstrap setServerSocketFactory(final ServerSocketFactory serverSocketFactory)
    '''
def setSslContext():
    '''public final ServerBootstrap setSslContext(final SSLContext sslContext)
    '''
def setExceptionLogger():
    '''public final ServerBootstrap setExceptionLogger(final ExceptionLogger exceptionLogger)
    '''
def create():
    '''public HttpServer create()
    '''
