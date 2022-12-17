def ():
    '''returns HttpRequestHandlerResolverAdapter\n\n
    (final HttpProcessor processor, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory, final HttpRequestHandlerResolver handlerResolver, final HttpExpectationVerifier expectationVerifier, final HttpParams params)\n
    (final HttpProcessor processor, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory, final HttpRequestHandlerResolver handlerResolver, final HttpParams params)\n
    (final HttpProcessor proc, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory)\n
    (final HttpProcessor processor, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory, final HttpRequestHandlerMapper handlerMapper, final HttpExpectationVerifier expectationVerifier)\n
    (final HttpProcessor processor, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory, final HttpRequestHandlerMapper handlerMapper)\n
    (final HttpProcessor processor, final HttpRequestHandlerMapper handlerMapper)\n
    (final HttpRequestHandlerResolver resolver)\n
    '''
def setHttpProcessor():
    '''returns None\n\n
    setHttpProcessor(final HttpProcessor processor)\n
    '''
def setConnReuseStrategy():
    '''returns None\n\n
    setConnReuseStrategy(final ConnectionReuseStrategy connStrategy)\n
    '''
def setResponseFactory():
    '''returns None\n\n
    setResponseFactory(final HttpResponseFactory responseFactory)\n
    '''
def setParams():
    '''returns None\n\n
    setParams(final HttpParams params)\n
    '''
def setHandlerResolver():
    '''returns None\n\n
    setHandlerResolver(final HttpRequestHandlerResolver handlerResolver)\n
    '''
def setExpectationVerifier():
    '''returns None\n\n
    setExpectationVerifier(final HttpExpectationVerifier expectationVerifier)\n
    '''
def getParams():
    '''returns HttpParams\n\n
    getParams()\n
    '''
def handleRequest():
    '''returns None\n\n
    handleRequest(final HttpServerConnection conn, final HttpContext context)\n
    '''
def lookup():
    '''returns HttpRequestHandler\n\n
    lookup(final HttpRequest request)\n
    '''
