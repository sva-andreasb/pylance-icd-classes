HEADER_USER_AGENT = "String  \"User-Agent\""
HEADER_SDK_TRANSACTION_ID = "String  \"amz-sdk-invocation-id\""
HEADER_SDK_RETRY_INFO = "String  \"amz-sdk-retry\""
def ():
    '''returns AmazonHttpClient\n\n
    (final ClientConfiguration config)\n
    (final ClientConfiguration config, final RequestMetricCollector requestMetricCollector)\n
    (final ClientConfiguration config, final RequestMetricCollector requestMetricCollector, final boolean useBrowserCompatibleHostNameVerifier)\n
    (final ClientConfiguration clientConfig, final ConnectionManagerAwareHttpClient httpClient, final RequestMetricCollector requestMetricCollector)\n
    '''
def getHttpRequestTimer():
    '''returns HttpRequestTimer\n\n
    getHttpRequestTimer()\n
    '''
def getClientExecutionTimer():
    '''returns ClientExecutionTimer\n\n
    getClientExecutionTimer()\n
    '''
def getResponseMetadataForRequest():
    '''returns ResponseMetadata\n\n
    getResponseMetadataForRequest(final AmazonWebServiceRequest request)\n
    '''
def handle():
    '''returns T\n\n
    handle(final com.amazonaws.http.HttpResponse response)\n
    '''
def needsConnectionLeftOpen():
    '''returns boolean\n\n
    needsConnectionLeftOpen()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def getRequestMetricCollector():
    '''returns RequestMetricCollector\n\n
    getRequestMetricCollector()\n
    '''
def getTimeOffset():
    '''returns int\n\n
    getTimeOffset()\n
    '''
