DEFAULT_MAX_ERROR_RETRY = "int  3"
DYNAMODB_DEFAULT_MAX_ERROR_RETRY = "int  10"
def getDefaultRetryPolicy():
    '''    public static RetryPolicy getDefaultRetryPolicy()
    '''
def getDynamoDBDefaultRetryPolicy():
    '''    public static RetryPolicy getDynamoDBDefaultRetryPolicy()
    '''
def getDefaultRetryPolicyWithCustomMaxRetries():
    '''    public static RetryPolicy getDefaultRetryPolicyWithCustomMaxRetries(final int maxErrorRetry)
    '''
def getDynamoDBDefaultRetryPolicyWithCustomMaxRetries():
    '''    public static RetryPolicy getDynamoDBDefaultRetryPolicyWithCustomMaxRetries(final int maxErrorRetry)
    '''
def shouldRetry():
    '''    public boolean shouldRetry(final AmazonWebServiceRequest originalRequest, final AmazonClientException exception, final int retriesAttempted)
    '''
def delayBeforeNextRetry():
    '''    public final long delayBeforeNextRetry(final AmazonWebServiceRequest originalRequest, final AmazonClientException exception, final int retriesAttempted)
    public final long delayBeforeNextRetry(final AmazonWebServiceRequest originalRequest, final AmazonClientException exception, final int retriesAttempted)
    '''
