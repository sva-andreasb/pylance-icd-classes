LOGGING_AWS_REQUEST_METRIC = "boolean  true"
def ():
    '''returns AmazonWebServiceClient\n\n
    (final ClientConfiguration clientConfiguration)\n
    (final ClientConfiguration clientConfiguration, final RequestMetricCollector requestMetricCollector)\n
    '''
def setEndpoint():
    '''returns None\n\n
    setEndpoint(final String endpoint)\n
    '''
def getSignerByURI():
    '''returns Signer\n\n
    getSignerByURI(final URI uri)\n
    '''
def setRegion():
    '''returns None\n\n
    setRegion(final Region region)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def addRequestHandler():
    '''returns None\n\n
    addRequestHandler(final RequestHandler requestHandler)\n
    addRequestHandler(final RequestHandler2 requestHandler2)\n
    '''
def removeRequestHandler():
    '''returns None\n\n
    removeRequestHandler(final RequestHandler requestHandler)\n
    removeRequestHandler(final RequestHandler2 requestHandler2)\n
    '''
def setTimeOffset():
    '''returns None\n\n
    setTimeOffset(final int timeOffset)\n
    '''
def withTimeOffset():
    '''returns AmazonWebServiceClient\n\n
    withTimeOffset(final int timeOffset)\n
    '''
def getTimeOffset():
    '''returns int\n\n
    getTimeOffset()\n
    '''
def getRequestMetricsCollector():
    '''returns RequestMetricCollector\n\n
    getRequestMetricsCollector()\n
    '''
def getServiceName():
    '''returns String\n\n
    getServiceName()\n
    '''
def getEndpointPrefix():
    '''returns String\n\n
    getEndpointPrefix()\n
    '''
