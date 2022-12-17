def ():
    '''returns StackedRequestHandler\n\n
    (final RequestHandler2... requestHandlers)\n
    (final List<RequestHandler2> requestHandlers)\n
    '''
def beforeMarshalling():
    '''returns AmazonWebServiceRequest\n\n
    beforeMarshalling(final AmazonWebServiceRequest origRequest)\n
    '''
def beforeRequest():
    '''returns None\n\n
    beforeRequest(final Request<?> request)\n
    '''
def beforeUnmarshalling():
    '''returns HttpResponse\n\n
    beforeUnmarshalling(final Request<?> request, final HttpResponse origHttpResponse)\n
    '''
def afterResponse():
    '''returns None\n\n
    afterResponse(final Request<?> request, final Response<?> response)\n
    '''
def afterError():
    '''returns None\n\n
    afterError(final Request<?> request, final Response<?> response, final Exception e)\n
    '''
