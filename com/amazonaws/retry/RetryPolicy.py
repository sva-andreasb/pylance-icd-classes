def RetryPolicy():
'''public RetryPolicy(RetryCondition retryCondition, BackoffStrategy backoffStrategy, final int maxErrorRetry, final boolean honorMaxErrorRetryInClientConfig)
'''
pass
def getRetryCondition():
'''public RetryCondition getRetryCondition()
'''
pass
def getBackoffStrategy():
'''public BackoffStrategy getBackoffStrategy()
'''
pass
def getMaxErrorRetry():
'''public int getMaxErrorRetry()
'''
pass
def isMaxErrorRetryInClientConfigHonored():
'''public boolean isMaxErrorRetryInClientConfigHonored()
'''
pass
def shouldRetry():
'''public boolean shouldRetry(final AmazonWebServiceRequest originalRequest, final AmazonClientException exception, final int retriesAttempted)
'''
pass
def delayBeforeNextRetry():
'''public long delayBeforeNextRetry(final AmazonWebServiceRequest originalRequest, final AmazonClientException exception, final int retriesAttempted)
'''
pass
