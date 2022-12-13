LOGGING_AWS_REQUEST_METRIC = "boolean  true"
def AmazonWebServiceClient():
    '''public AmazonWebServiceClient(final ClientConfiguration clientConfiguration)
    public AmazonWebServiceClient(final ClientConfiguration clientConfiguration, final RequestMetricCollector requestMetricCollector)
    '''
def setEndpoint():
    '''public void setEndpoint(final String endpoint)
    '''
def getSignerByURI():
    '''public Signer getSignerByURI(final URI uri)
    '''
def setRegion():
    '''public void setRegion(final Region region)
    '''
def configureRegion():
    '''public final void configureRegion(final Regions region)
    '''
def shutdown():
    '''public void shutdown()
    '''
def addRequestHandler():
    '''public void addRequestHandler(final RequestHandler requestHandler)
    public void addRequestHandler(final RequestHandler2 requestHandler2)
    '''
def removeRequestHandler():
    '''public void removeRequestHandler(final RequestHandler requestHandler)
    public void removeRequestHandler(final RequestHandler2 requestHandler2)
    '''
def setTimeOffset():
    '''public void setTimeOffset(final int timeOffset)
    '''
def withTimeOffset():
    '''public AmazonWebServiceClient withTimeOffset(final int timeOffset)
    '''
def getTimeOffset():
    '''public int getTimeOffset()
    '''
def getRequestMetricsCollector():
    '''public RequestMetricCollector getRequestMetricsCollector()
    '''
def getServiceName():
    '''public String getServiceName()
    '''
def getEndpointPrefix():
    '''public String getEndpointPrefix()
    '''
def setServiceNameIntern():
    '''public final void setServiceNameIntern(final String serviceName)
    '''
def getSignerRegionOverride():
    '''public final String getSignerRegionOverride()
    '''
def setSignerRegionOverride():
    '''public final void setSignerRegionOverride(final String signerRegionOverride)
    '''
def withRegion():
    '''public <T extends AmazonWebServiceClient> T withRegion(final Region region)
    public <T extends AmazonWebServiceClient> T withRegion(final Regions region)
    '''
def withEndpoint():
    '''public <T extends AmazonWebServiceClient> T withEndpoint(final String endpoint)
    '''
