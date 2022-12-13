HEADER_USER_AGENT = "String  User-Agent""
HEADER_SDK_TRANSACTION_ID = "String  amz-sdk-invocation-id""
HEADER_SDK_RETRY_INFO = "String  amz-sdk-retry""
def AmazonHttpClient():
'''public AmazonHttpClient(final ClientConfiguration config)
public AmazonHttpClient(final ClientConfiguration config, final RequestMetricCollector requestMetricCollector)
public AmazonHttpClient(final ClientConfiguration config, final RequestMetricCollector requestMetricCollector, final boolean useBrowserCompatibleHostNameVerifier)
public AmazonHttpClient(final ClientConfiguration clientConfig, final ConnectionManagerAwareHttpClient httpClient, final RequestMetricCollector requestMetricCollector)
'''
pass
def getHttpRequestTimer():
'''public HttpRequestTimer getHttpRequestTimer()
'''
pass
def getClientExecutionTimer():
'''public ClientExecutionTimer getClientExecutionTimer()
'''
pass
def getResponseMetadataForRequest():
'''public ResponseMetadata getResponseMetadataForRequest(final AmazonWebServiceRequest request)
'''
pass
def execute():
'''public <T> Response<T> execute(final Request<?> request, final HttpResponseHandler<AmazonWebServiceResponse<T>> responseHandler, final HttpResponseHandler<AmazonServiceException> errorResponseHandler, final ExecutionContext executionContext)
'''
pass
def handle():
'''public T handle(final com.amazonaws.http.HttpResponse response)
'''
pass
def needsConnectionLeftOpen():
'''public boolean needsConnectionLeftOpen()
'''
pass
def executeWithTimer():
'''public <T> Response<T> executeWithTimer(final Request<?> request, final HttpResponseHandler<AmazonWebServiceResponse<T>> responseHandler, final HttpResponseHandler<AmazonServiceException> errorResponseHandler, final ExecutionContext executionContext)
'''
pass
def shutdown():
'''public void shutdown()
'''
pass
def getRequestMetricCollector():
'''public RequestMetricCollector getRequestMetricCollector()
'''
pass
def getTimeOffset():
'''public int getTimeOffset()
'''
pass
