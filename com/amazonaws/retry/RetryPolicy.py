def ():
    '''returns RetryPolicy\n\n
    (RetryCondition retryCondition, BackoffStrategy backoffStrategy, final int maxErrorRetry, final boolean honorMaxErrorRetryInClientConfig)\n
    '''
def getRetryCondition():
    '''returns RetryCondition\n\n
    getRetryCondition()\n
    '''
def getBackoffStrategy():
    '''returns BackoffStrategy\n\n
    getBackoffStrategy()\n
    '''
def getMaxErrorRetry():
    '''returns int\n\n
    getMaxErrorRetry()\n
    '''
def isMaxErrorRetryInClientConfigHonored():
    '''returns boolean\n\n
    isMaxErrorRetryInClientConfigHonored()\n
    '''
def shouldRetry():
    '''returns boolean\n\n
    shouldRetry(final AmazonWebServiceRequest originalRequest, final AmazonClientException exception, final int retriesAttempted)\n
    '''
def delayBeforeNextRetry():
    '''returns long\n\n
    delayBeforeNextRetry(final AmazonWebServiceRequest originalRequest, final AmazonClientException exception, final int retriesAttempted)\n
    '''
