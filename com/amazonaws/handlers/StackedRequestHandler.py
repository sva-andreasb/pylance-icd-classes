def StackedRequestHandler():
'''public StackedRequestHandler(final RequestHandler2... requestHandlers)
public StackedRequestHandler(final List<RequestHandler2> requestHandlers)
'''
pass
def beforeMarshalling():
'''public AmazonWebServiceRequest beforeMarshalling(final AmazonWebServiceRequest origRequest)
'''
pass
def beforeRequest():
'''public void beforeRequest(final Request<?> request)
'''
pass
def beforeUnmarshalling():
'''public HttpResponse beforeUnmarshalling(final Request<?> request, final HttpResponse origHttpResponse)
'''
pass
def afterResponse():
'''public void afterResponse(final Request<?> request, final Response<?> response)
'''
pass
def afterError():
'''public void afterError(final Request<?> request, final Response<?> response, final Exception e)
'''
pass
