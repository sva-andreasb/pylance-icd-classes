def HttpService():
'''public HttpService(final HttpProcessor processor, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory, final HttpRequestHandlerResolver handlerResolver, final HttpExpectationVerifier expectationVerifier, final HttpParams params)
public HttpService(final HttpProcessor processor, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory, final HttpRequestHandlerResolver handlerResolver, final HttpParams params)
public HttpService(final HttpProcessor proc, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory)
public HttpService(final HttpProcessor processor, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory, final HttpRequestHandlerMapper handlerMapper, final HttpExpectationVerifier expectationVerifier)
public HttpService(final HttpProcessor processor, final ConnectionReuseStrategy connStrategy, final HttpResponseFactory responseFactory, final HttpRequestHandlerMapper handlerMapper)
public HttpService(final HttpProcessor processor, final HttpRequestHandlerMapper handlerMapper)
'''
pass
def setHttpProcessor():
'''public void setHttpProcessor(final HttpProcessor processor)
'''
pass
def setConnReuseStrategy():
'''public void setConnReuseStrategy(final ConnectionReuseStrategy connStrategy)
'''
pass
def setResponseFactory():
'''public void setResponseFactory(final HttpResponseFactory responseFactory)
'''
pass
def setParams():
'''public void setParams(final HttpParams params)
'''
pass
def setHandlerResolver():
'''public void setHandlerResolver(final HttpRequestHandlerResolver handlerResolver)
'''
pass
def setExpectationVerifier():
'''public void setExpectationVerifier(final HttpExpectationVerifier expectationVerifier)
'''
pass
def getParams():
'''public HttpParams getParams()
'''
pass
def handleRequest():
'''public void handleRequest(final HttpServerConnection conn, final HttpContext context)
'''
pass
def HttpRequestHandlerResolverAdapter():
'''public HttpRequestHandlerResolverAdapter(final HttpRequestHandlerResolver resolver)
'''
pass
def lookup():
'''public HttpRequestHandler lookup(final HttpRequest request)
'''
pass
