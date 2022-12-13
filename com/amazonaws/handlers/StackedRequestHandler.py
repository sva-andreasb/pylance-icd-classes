def StackedRequestHandler():
    '''public StackedRequestHandler(final RequestHandler2... requestHandlers)
    public StackedRequestHandler(final List<RequestHandler2> requestHandlers)
    '''
def beforeMarshalling():
    '''public AmazonWebServiceRequest beforeMarshalling(final AmazonWebServiceRequest origRequest)
    '''
def beforeRequest():
    '''public void beforeRequest(final Request<?> request)
    '''
def beforeUnmarshalling():
    '''public HttpResponse beforeUnmarshalling(final Request<?> request, final HttpResponse origHttpResponse)
    '''
def afterResponse():
    '''public void afterResponse(final Request<?> request, final Response<?> response)
    '''
def afterError():
    '''public void afterError(final Request<?> request, final Response<?> response, final Exception e)
    '''
