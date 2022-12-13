def HttpService():
    '''    public HttpService(final HttpProcessor processor, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory, final HttpRequestHandlerResolver handlerResolver, final HttpExpectationVerifier expectationVerifier, final HttpParams params)
    public HttpService(final HttpProcessor processor, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory, final HttpRequestHandlerResolver handlerResolver, final HttpParams params)
    public HttpService(final HttpProcessor proc, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory)
    public HttpService(final HttpProcessor processor, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory, final HttpRequestHandlerMapper handlerMapper, final HttpExpectationVerifier expectationVerifier)
    public HttpService(final HttpProcessor processor, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory, final HttpRequestHandlerMapper handlerMapper)
    public HttpService(final HttpProcessor processor, final HttpRequestHandlerMapper handlerMapper)
    '''
def setHttpProcessor():
    '''    public void setHttpProcessor(final HttpProcessor processor)
    '''
def setConnReuseStrategy():
    '''    public void setConnReuseStrategy(final ConnectionReuseStrategy connStrategy)
    '''
def setResponseFactory():
    '''    public void setResponseFactory(final HttpResponseFactory responseFactory)
    '''
def setParams():
    '''    public void setParams(final HttpParams params)
    '''
def setHandlerResolver():
    '''    public void setHandlerResolver(final HttpRequestHandlerResolver handlerResolver)
    '''
def setExpectationVerifier():
    '''    public void setExpectationVerifier(final HttpExpectationVerifier expectationVerifier)
    '''
def getParams():
    '''    public HttpParams getParams()
    '''
def handleRequest():
    '''    public void handleRequest(final HttpServerConnection conn, final HttpContext context)
    '''
def HttpRequestHandlerResolverAdapter():
    '''    public HttpRequestHandlerResolverAdapter(final HttpRequestHandlerResolver resolver)
    '''
def lookup():
    '''    public HttpRequestHandler lookup(final HttpRequest request)
    '''
