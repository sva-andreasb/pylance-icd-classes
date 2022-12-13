def RetryPolicy():
    '''    public RetryPolicy(RetryCondition retryCondition, BackoffStrategy backoffStrategy, final int maxErrorRetry, final boolean honorMaxErrorRetryInClientConfig)
    '''
def getRetryCondition():
    '''    public RetryCondition getRetryCondition()
    '''
def getBackoffStrategy():
    '''    public BackoffStrategy getBackoffStrategy()
    '''
def getMaxErrorRetry():
    '''    public int getMaxErrorRetry()
    '''
def isMaxErrorRetryInClientConfigHonored():
    '''    public boolean isMaxErrorRetryInClientConfigHonored()
    '''
def shouldRetry():
    '''    public boolean shouldRetry(final AmazonWebServiceRequest originalRequest, final AmazonClientException exception, final int retriesAttempted)
    '''
def delayBeforeNextRetry():
    '''    public long delayBeforeNextRetry(final AmazonWebServiceRequest originalRequest, final AmazonClientException exception, final int retriesAttempted)
    '''
